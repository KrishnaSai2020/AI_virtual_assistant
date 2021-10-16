import Skills
from modules.User_Input import get_command
from modules.AI_Speech import speak


def run_command(command):
    if command == "What can you do":
        pass

    A = ["hi", "hello", "hey", "hai", "hey dream", "hi dream", "hello dream"]
    if command in A:
       greet()

    if speech == "who are you":
        speak("I'm insert name here")
        speak("your personal assistant")

    B = ["what day is it", "what day is today", "what day is this"]
    if command in B:
        tell_day()

    C = ["what month is it", "what month is this"]
    if command in C:
        tell_month()

    D = ["what time is it", "what is the time", "time please", ]
    if command in D:
        tell_time()

    if command[0:6] == "Google":
        search(speech[7:])

    if speech[0:7] == "YouTube":
        play_tube(speech[8:])

    if speech == "open Chrome":
        open_chrome()

    if speech[0:9] == "Wikipedia":
        search_wiki(speech[10:])

    E = ["bye", "bye", "shutdown", "quit", "goodbye", "Goodbye"]
    if speech in C:
        shut()
    else:
        speak("I am sorry couldn't perform the task you specified")
