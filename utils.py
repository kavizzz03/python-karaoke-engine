import time

def print_lyrics(text):
    text = str(text).strip()

    print("\n🎤 ", end="", flush=True)

    for c in text:
        print(c, end="", flush=True)
        time.sleep(0.01)  # faster = better sync feel

    print()