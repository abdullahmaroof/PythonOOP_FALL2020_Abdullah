import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
import random
song = {"Dark side": "D:\\MUSICON\\english\\Alan Walker - Darkside.mp3"}
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
    speak('I am AI machine sir')
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...........')
        r.pause_threshold = 0.5
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
speak("Sir tell me your name for verfication")
query = takeCommand().lower()
if 'abdullah' in query:
    speak("Sir abdullah, please tell your verification code")
    query = takeCommand().lower()
    if '1101' in query:
        speak("Sir abdullah, thank you for verification. pkease tell me how may i help you")
        while True:
        #if 1:
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

            elif 'open ghana' in query:
                webbrowser.open("gaana.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open github' in query:
                webbrowser.open("github.com")

            elif 'open stack over flow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'open zoom' in query:
                webbrowser.open("zoom.com")

            elif 'play music' in query:
                music_dir = "D:\\MUSICON\\trending audio"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[8]))

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"Sir, the time is {strTime}")
                speak(f"Sir, the time is {strTime}")

            elif 'open python' in query:
                pathPYcharm = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2\\bin\\pycharm64.exe"
                os.startfile(pathPYcharm)
    else:
        speak("Abdullah sir, your code is wrong. Please verify again")
        speak("If verification code is wrong again, I will shut down system and report it as a security threat")

else:
    speak("You are not my Abdullah sir, I cannot follow your commands")
    speak("I think you are a hacker")
    speak("I am shuting down my all systems")