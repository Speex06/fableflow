import os

# Load your ElevenLabs API key from environment or fallback to placeholder
API_KEY = os.environ.get("ELEVENLABS_API_KEY", "sk_eb01a65cb5925bc46340cfad3f2eb2d87346f5910046977d")
VOICE_ID = os.environ.get("ELEVENLABS_VOICE_ID", "wELY8EqoVXN9wDhQ5vGB")
MODEL_ID = os.environ.get("ELEVENLABS_MODEL_ID", "eleven_multilingual_v2")

# Flask settings
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "supersecretkey")