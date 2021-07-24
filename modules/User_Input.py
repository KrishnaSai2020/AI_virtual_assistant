import speech_recognition as sr
from modules.AI_Speech import speak


def get_command(self):
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    with mic as s:
        audio = r.listen(s, timeout=5)
        r.adjust_for_ambient_noise(s)

    try:
        speech = r.recognize_google(audio)
        return speech

    except sr.UnknownValueError:
        speak("please try again,")

    except sr.WaitTimeoutError as e:
        speak("please try again")
