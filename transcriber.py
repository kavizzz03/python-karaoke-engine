import whisper

def load_model():
    print("🔄 Loading model...")
    return whisper.load_model("base")

def transcribe_audio(model, audio_path):
    print("📝 Transcribing with timestamps...")

    result = model.transcribe(
        audio_path,
        language="en",
        task="transcribe",
        word_timestamps=True   # 🔥 IMPORTANT UPGRADE
    )

    return result["segments"]