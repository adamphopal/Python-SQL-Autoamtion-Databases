from gtts import gTTS 
import os
from playsound import playsound
from util import time_it


@time_it
def get_audio():
    audio = input("enter name for mp3 file, example:voice.mp3")
    file = open("draft.txt", "r").read().replace("\n", " ")
    language = 'en'
    speech = gTTS(text = str(file), lang = language, slow = False)
    speech.save(audio)
 #   os.system("start voice.mp3")
  #  playsound(audio)



get_audio()

