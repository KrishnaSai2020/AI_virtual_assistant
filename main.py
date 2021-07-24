import SpeechRecognition as sr
from modules import Speak
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests


def greeting():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        Speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif 12 <= hour < 18:
        Speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        Speak("Hello,Good Evening")
        print("Hello,Good Evening")


def get_user_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio, language='en-in')
            print(f"user said:{command}\n")

        except Exception as e:
            Speak("Pardon me, please say that again")
            return "None"
        return statement


print("Loading your AI personal assistant {insert name here}")
Speak("Loading your AI personal assistant")
greeting()

if __name__ == '__main__':

    while True:
        Speak("Tell me how can I help you now?")
        statement = get_user_command().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            Speak('your personal assistant G-one is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            break
