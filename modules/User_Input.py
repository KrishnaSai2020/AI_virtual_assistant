import SpeechRecognition as Sr
from modules.AI_Speech import speak


def get_user_command():
    r = Sr.Recognizer()
    with Sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio, language='en-UK')
            print(f"{command}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return command
