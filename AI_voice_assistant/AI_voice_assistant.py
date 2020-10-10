import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak('I am AI machine sir, Please tell me how may i help you')
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...........')
        audio = r.listen(source)
    try:
        print('Recognizing............')
        query = r.recognize_google(audio, language='en-uk')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please.........")
        return "None"
    return query

wishme()
takeCommand()
