from .modules.AI_Speech import speak
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


def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif 12 <= hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def search_wikipedia(statement):
    speak('Searching Wikipedia...')
    statement = statement.replace("wikipedia", "")
    result = wikipedia.summary(statement, sentences=3)
    speak("According to Wikipedia")
    print(result)
    speak(result)


def youtube():
    webbrowser.open_new_tab("https://www.youtube.com")
    speak("opened youtube")
    time.sleep(5)
