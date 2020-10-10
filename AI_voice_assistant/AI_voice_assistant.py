import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
import random

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
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing............')
        query = r.recognize_google(audio, language='en-pak')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please.........")
        return "None"
    return query

wishme()
while True:
    query = takeCommand().lower()
    if 'wikipedia' in query:
        print("Sreaching Wikipedia")
        query = query.replace("Wikipedia", "")
        results = wikipedia.summary(query, sentences=5)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open facebook' in query:
        webbrowser.open("facebook.com")

    elif 'open gaana' in query:
        webbrowser.open("gaana.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open github' in query:
        webbrowser.open("github.com")
    elif 'play music' in query:
        music_dir = "D:\\MUSICON\\trending audio"
        songs = os.listdir(music_dir)
        print(songs)
        songs = random.random()
        os.startfile(os.path.join(music_dir, songs))
