import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class call_voice:
    @staticmethod
    def wishme():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak('Good Morning!')
        elif hour>=12 and hour<18:
            speak('Good Afternoon!')
        else:
          speak('Good Evening!')
        speak('Welcome to our food order system')

class call_login(call_voice):
    @staticmethod
    def wishme():
        speak("Welcome to login sir. Please enter your username and password")

class voice_signup(call_voice):
    @staticmethod
    def wishme():
        speak("Welcome to signup new user. Please enter your information which is asked!!!")

class voice_loginadmin(call_voice):
    @staticmethod
    def wishme():
        speak("Welcome boss. Please enter your username and password for verification!!!")

class voice_system(call_voice):
    @staticmethod
    def wishme():
        speak("Sir, Click on personal information to see your information")
        speak("or Click on about us to see our team")
        speak("or Click to order food for your meal")

class voice_menu(call_voice):
    @staticmethod
    def wishme():
        speak("Sir, tell us want you want to eat. We have all special meals")

class voice_pizza(call_voice):
    @staticmethod
    def wishme():
        speak("Sir, here you go with different pizza tastes. Place your order")

class voice_burger(call_voice):
    @staticmethod
    def wishme():
        speak("Sir, here you go with different burger tastes. Place your order")

class voice_biryani(call_voice):
    @staticmethod
    def wishme():
        speak("Sir, here you go with different biryani tastes. Place your order")

class voice_paratharoll(call_voice):
    @staticmethod
    def wishme():
        speak("Sir, here you go with different paratha roll tastes. Place your order")
class voice_admin(call_voice):
    @staticmethod
    def wishme():
        speak("Sir, How are you!!!")
        speak("Sir, you can get reports of users and bills")