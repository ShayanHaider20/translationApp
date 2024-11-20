from flask import Flask, request, jsonify, render_template
from whisper import load_model
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import logging
import time

@app.route('/')
def index():
    return render_template('index.html')
