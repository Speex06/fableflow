import os
import time
from flask import Blueprint, render_template, request, flash, redirect, url_for, send_from_directory
from eleven_api import generate_voice

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    audio_filename = None
    if request.method == 'POST':
        # Get user input
        text = request.form.get('text', '').strip()
        if not text:
            flash('Please enter text to convert.', 'warning')
            return redirect(url_for('main.index'))

        # Collect voice parameters
        stability = float(request.form.get('stability', 50)) / 100
        similarity = float(request.form.get('similarity', 75)) / 100
        speed = float(request.form.get('speed', 1.0))
        style = float(request.form.get('style_exaggeration', 0)) / 100

        # Generate unique filename
        timestamp = int(time.time())
        audio_filename = f"output_{timestamp}.mp3"

        # Generate and save audio
        voice_settings = {
            'stability': stability,
            'similarity_boost': similarity,
            'style': style,
            'speed': speed
        }
        generate_voice(text, audio_filename, voice_settings)

    # List all generated MP3s sorted by latest
    audio_files = [f for f in os.listdir(os.getcwd()) if f.endswith('.mp3')]
    audio_files.sort(key=lambda fn: os.path.getmtime(fn), reverse=True)

    return render_template('index.html', audio_filename=audio_filename, audio_files=audio_files)

@bp.route('/audio/<path:filename>')
def serve_audio(filename):
    # Serve the generated audio file
    return send_from_directory(os.getcwd(), filename)