# 🌍 Medical Translator App 🏥

## 📝 Overview
The **Medical Translator App** is a Flask-based web application that enables users to 🎤 record audio, 📝 transcribe it into text, 🌎 translate the transcription into a selected language, and 🔊 play back the translated text as speech. The app utilizes **OpenAI Whisper**, **Google Translator**, and **gTTS (Google Text-to-Speech)** to facilitate seamless multilingual communication.

## 🚀 Features
- 🎙 **Record audio** directly from the browser.
- 📝 **Transcribe speech** using **Whisper**.
- 🌎 **Translate** transcribed text into multiple languages using **Google Translator**.
- 🔊 **Convert text to speech** using **gTTS**.
- 💻 **User-friendly web interface** for easy interaction.
- 🔐 **Secure and efficient backend processing**.

## 🛠 Technologies Used
- 🏗 **Flask** (Web Framework)
- 🗣 **Whisper** (Speech-to-Text)
- 🌍 **Google Translator API** (Text Translation)
- 🎵 **gTTS** (Text-to-Speech)
- 🎨 **JavaScript** (Frontend)
- 🖌 **HTML & CSS** (UI Design)

## 📥 Installation & Setup
### 📌 Prerequisites
Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

### 📌 Steps to Run the Application
```bash
# 🛠 Clone the repository
git clone https://github.com/yourusername/medical-translator.git
cd medical-translator

# 🏗 Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

# 📦 Install dependencies
pip install -r requirements.txt

# 🚀 Run the Flask app
python app.py
```

### 🌐 Access the App
```
http://127.0.0.1:5000/
```
