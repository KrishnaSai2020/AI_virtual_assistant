from Run_Commands import run_commands
from modules.User_Input import get_user_command
from Skills import greet, search_wikipedia, youtube
from .modules.AI_Speech import speak

if __name__ == '__main__':
    print("Loading your AI personal assistant {insert name here}")
    speak("Loading your AI personal assistant")
    greet()

    while True:
        speak("Hello how can I help?")
        statement = get_user_command().lower()
        if statement == 0:
            continue

        run_commands(statement)

        if "good bye" in statement or "ok bye" in statement:
            # create a sleeping function here for it too sleep but not turn off
            pass

        elif 'shut down' or 'goodnight' in statement:
            speak('your personal assistant <name> is shutting down,Good bye')
            print('your personal assistant <name> is shutting down,Good bye')
            break
