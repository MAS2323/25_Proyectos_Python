# Install SpeechRecognition with pip install SpeechRecognition
# Install pyttsx3 with pip install pyttsx3
# https://www.amazon.es/s?k=

import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()

engine = pyttsx3.init()


def talk():

    mic = sr.Microphone()
    with mic as source:
        audio = recognizer.listen(source)

    text = recognizer.recognize_google(audio, language='es-ES')

    print(f'Has dicho: {text}')
    return text.lower()


if 'amazon' in talk():

    engine.say('Que quieres comprar en Amazon?')
    engine.runAndWait()
    text = talk()
    webbrowser.open(f'https://www.amazon.es/s?k={text}')
