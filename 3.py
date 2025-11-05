from gtts import gTTS
from pygame import *
import os
import time
import random

def text_to_speech(phrase: str, lang: str = "uk") -> str:
    # Add random number to the file name to make file unique
    filename = f"voice_{random.randint(1000, 9999)}.mp3"

    # Create object with text in gTTS
    tts = gTTS(phrase, lang=lang)
    tts.save(filename)
    
    # Start mixer, load file and play
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()

    # Every 0.5s check if audio is playing
    while mixer.music.get_busy():
        time.sleep(0.5)

    return filename


def delete_file(filename: str) -> bool:
    try:
        # Unload audio and quit
        mixer.music.unload()
        mixer.quit()
        # Delete file
        os.remove(filename)
        return True
    except Exception as e:
        print(f"Помилка при видаленні файлу: {e}")
        return False

while True:
    langNumber = int(input("Оберіть мову: \n1 - англійська\n2 - українська\n3 - німецька\n4 - вийти\n"))
    lang = 'en'

    if langNumber == 1:
        lang = 'en'
    elif langNumber == 2:
        lang = 'uk'
    elif langNumber == 3:
        lang = 'de'
    elif langNumber == 4:
        break
    else:
        print("Мова не знайдена. Оберіть будь ласка знову")
        continue

    phrase = input("Введіть фразу для озвучки: ")

    file: str = text_to_speech(phrase, lang)
    success: bool = delete_file(file)
    print(f"Файл видалено: {success}")