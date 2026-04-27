import vlc
import time

def play_audio(audio_path):
    instance = vlc.Instance()
    player = instance.media_player_new()

    media = instance.media_new(audio_path)
    player.set_media(media)

    player.play()

    time.sleep(1)  # allow start

    return player