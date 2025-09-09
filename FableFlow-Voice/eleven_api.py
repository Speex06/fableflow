from elevenlabs import ElevenLabs
from config import API_KEY, VOICE_ID, MODEL_ID

client = ElevenLabs(api_key=API_KEY)

def generate_voice(text: str, filename: str, voice_settings: dict = None) -> str:
    """
    Convert input text to speech with custom settings and save as MP3.
    Returns the filename.
    """
    settings = voice_settings or {}
    audio_stream = client.text_to_speech.convert(
        voice_id=VOICE_ID,
        model_id=MODEL_ID,
        text=text,
        voice_settings={
            'stability': settings.get('stability', 0.5),
            'similarity_boost': settings.get('similarity_boost', 0.75),
            'style': settings.get('style', 0),
            'speed': settings.get('speed', 1.0)
        },
        output_format="mp3_44100_128"
    )

    with open(filename, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)
    return filename