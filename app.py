from flask import Flask, request, jsonify, render_template
from whisper import load_model
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import logging
import time
from pydub import AudioSegment

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to attempt loading the Whisper model with retries
def load_whisper_model():
    retries = 3
    for attempt in range(retries):
        try:
            model = load_model("base")
            logging.info("Whisper model loaded successfully.")
            return model
        except Exception as e:
            logging.error(f"Attempt {attempt+1} to load Whisper model failed: {e}")
            time.sleep(2)  # Wait before retrying
    logging.error("Failed to load Whisper model after several attempts.")
    return None

# Load Whisper model with retry mechanism
whisper_model = load_whisper_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    if 'audio' not in request.files:
        logging.warning("No audio file provided in the request.")
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']
    target_language = request.form.get('target_language', 'es')

    # File validation (audio type and size)
    allowed_extensions = ['webm', 'mp3', 'wav']
    max_file_size = 10 * 1024 * 1024  # 10 MB
    if audio_file.filename.split('.')[-1] not in allowed_extensions:
        return jsonify({"error": "Invalid file type. Allowed types: webm, mp3, wav."}), 400

    if len(audio_file.read()) > max_file_size:
        return jsonify({"error": "File is too large. Maximum size is 10MB."}), 400

    # Reset the file stream after size check
    audio_file.seek(0)

    audio_path = "temp_audio.webm"
    output_audio_path = "static/translated_audio.mp3"

    try:
        # Save the audio file temporarily
        audio_file.save(audio_path)

        # Ensure the Whisper model is loaded
        if whisper_model is None:
            raise RuntimeError("Whisper model is not available.")

        # Transcribe audio using Whisper
        result = whisper_model.transcribe(audio_path)
        transcript = result.get("text", "")
        if not transcript:
            raise ValueError("Transcription failed or returned empty text.")

        # Translate text using Deep Translator
        translator = GoogleTranslator(source='auto', target=target_language)
        translated_text = translator.translate(transcript)
        if not translated_text:
            raise ValueError("Translation failed or returned empty text.")

        # Convert translated text to speech using gTTS
        tts = gTTS(translated_text, lang=target_language)
        tts.save(output_audio_path)

        logging.info("Audio processed successfully.")
        return jsonify({
            "transcript": transcript,
            "translated_text": translated_text,
            "audio_path": output_audio_path
        })

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": f"Sorry, we couldn't process your request. Please try again later. Error: {str(e)}"}), 500

    finally:
        # Cleanup: Remove the temporary input audio file
        if os.path.exists(audio_path):
            os.remove(audio_path)
            logging.info("Temporary audio file removed.")

if __name__ == '__main__':
    # Ensure that the app runs securely in production
    app.run(debug=False, host='127.0.0.1', port=5000) # Enables HTTPS (for production, use a proper certificate)
