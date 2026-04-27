import time
import sys
import os

from transcriber import load_model, transcribe_audio
from player import play_audio
from utils import print_lyrics

sys.stdout.reconfigure(encoding='utf-8')

AUDIO_FILE = "songs/song.mp3"

def main():
    print("🚀 Advanced Karaoke Engine Starting...")

    if not os.path.exists(AUDIO_FILE):
        print("❌ File not found")
        return

    model = load_model()
    segments = transcribe_audio(model, AUDIO_FILE)

    player = play_audio(AUDIO_FILE)

    print("\n🎵 Playing with Advanced Sync...\n")

    start_time = time.time()

    for seg in segments:
        # wait until correct moment
        while time.time() - start_time < seg["start"]:
            time.sleep(0.01)

        print_lyrics(seg["text"])

    # wait until audio ends
    while player.is_playing():
        time.sleep(1)

    print("\n✅ Finished")

if __name__ == "__main__":
    main()