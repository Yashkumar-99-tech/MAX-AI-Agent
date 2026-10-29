import asyncio
import edge_tts
import pygame
import tempfile
import os

VOICE = "en-US-AriaNeural"

# Initialize mixer only once
pygame.mixer.init()


async def generate_voice(text, filename):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(filename)


def speak(text):

    if not text:
        return

    text = str(text)

    print(f"\n🔊 MAX : {text}")

    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_path = temp.name
    temp.close()

    asyncio.run(generate_voice(text, temp_path))

    pygame.mixer.music.load(temp_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)

    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

    try:
        os.remove(temp_path)
    except:
        pass