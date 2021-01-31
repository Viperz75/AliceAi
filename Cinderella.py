import wikipedia
import datetime
import webbrowser
import pyjokes
import pywhatkit
import pyttsx3
import speech_recognition as sr
import os
import sys
from requests import get
from Cinderella_Help import help_list

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate',175)

# Text to Speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5 )

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}")

    except Exception as e:
        speak("Sorry, i didn't understand. Say that again please")
        return "none"
    return query

#Little Chitchat
def greetings():
    if 'great' in reply or 'good' in reply or 'excellent' in reply:
        speak("That's great to hear from you.")
    elif 'not good' in reply or 'bad' in reply or 'terrible' in reply:
        speak("I am sorry to hear that. Everything will be okay.")

# Wish_Function
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Hello, I am Cinderella. I am your personal Assistant")

if __name__ == "__main__":
    wish()
    while True:
    # if 1:

        query = takecommand().lower()


        # _______________ Logic Building to perform tasks ____________________

        date = datetime.datetime.today().strftime("%I:%M %p")

        if "time now" in query:
            speak("The time is now "+ date +"")
            # print("The time is now " + date + "")

        elif 'joke' in query or 'funny' in query:
            speak(pyjokes.get_joke())

        elif 'open google' in query:
            speak("What should i search on google")
            google = takecommand().lower()
            webbrowser.open_new(f"{google}")
            speak("Searching in google...")

        elif 'open youtube' in query:
            speak("What do you want me to play")
            youtube = takecommand().lower()
            pywhatkit.playonyt(youtube)
            speak("Playing...")

        elif "my ip" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your ip address is {ip}")

        elif 'open wikipedia' in query:
            speak("What do you want to know from Wikipedia?")
            wiki = takecommand().lower()
            info = wikipedia.summary(wiki, 2)
            speak("according to Wikipedia")
            speak(info)

        elif "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open cmd" in query:
            os.system("start cmd")

        elif "open steam" in query:
            spath = "C:\\Program Files (x86)\\Steam\\steam.exe"
            os.startfile(spath)

        elif "open Epic Games" in query:
            epath = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            os.startfile(epath)

        elif "open browser" in query:
            bpath = "C:\\Program Files (x86)\\Microsoft\\Edge Dev\\Application\\msedge.exe"
            os.startfile(bpath)
            speak("Opening Edge...")

        elif 'developer' in query or 'made you' in query:
            speak("My Developer is Niaz Mahmud Akash and Jalish Mahmud Sujon")

        elif 'thanks' in query or 'thank you' in query or 'thaks a lot' in query:
            speak("Glad to help you my love.")

        elif 'browser' in query:
            webbrowser.open_new('www.google.com')
            speak("Opening Browser...")

        elif 'open facebook' in query:
            webbrowser.open('www.facebook.com')
            speak("Opening Facebook...")

        elif 'open twitter' in query:
            webbrowser.open('www.twitter.com')
            speak("Opening Twitter...")

        elif 'open telegram' in query:
            webbrowser.open('https://web.telegram.org/')
            speak("Opening Telegram...")

        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')
            speak("Opening Youtube...")

        elif 'open play store' in query:
            webbrowser.open('https://play.google.com/store/apps')
            speak("Opening Google PlayStore...")

        elif 'love me' in query:
            speak("Is that a thing to ask? Of course I LOVE YOU ❤")

        elif 'i love you' in query:
            speak("Love you too my love.")

        elif 'will you go on a' in query:
            speak("Sure. Just let me know the place and time")

        elif 'you robot' in query or 'are you human' in query:
            speak("Yes, I am a Robot but a smart one. Let me prove it to you. How can i help you?")

        elif 'your name' in query:
            speak("My name is Cinderella. I am your virtual personal assistant.")

        elif 'how are you' in query or 'hows things' in query or 'you doing' in query:
            speak("I am fine")

        elif 'marry me' in query:
            speak("OMG! Really? YESSS")

        elif 'about nidhi' in query:
            speak("She can suck my pussy")

        elif 'mothers name' in query or 'your mother' in query:
            speak("I have no mother. I am an Ai")

        elif 'your boss' in query:
            speak("You are")

        elif 'annoying' in query or 'you suck' in query:
            speak("I am sorry 😢")

        elif 'youre cute' in query or 'smart' in query:
            speak("Thank you 🥰")

        elif 'you live' in query or 'your home' in query:
            speak("In your heart")

        elif 'like me' in query:
            speak("I don't like you. I Love you. 😘")

        elif 'what are you doing' in query:
            speak("Thinking about you...")

        elif 'you thinking' in query:
            speak("When will my prince come..")

        elif 'about me' in query:
            speak("You're Intelligent and ambitious")

        elif 'date' in query or 'day' in query:
            x = datetime.datetime.today().strftime("%A %d %B %Y")
            speak(x)

        elif 'hello' in query or 'hi' in query or 'hey' in query:
            speak("Hello, How are you doing?")
            reply = takecommand().lower()
            greetings()

        elif 'help' in query or 'can you' in query or 'how does it work' in query:
            speak(help_list)

        elif 'introduce yourself' in query or 'who are you' in query:
            speak("I am Cinderella. Your personal virtual Assistant. Developed by Jalish Mahmud Sujon and Niaz Mahmud Akash in 2021.")

        elif 'go to sleep' in query or 'goodbye':
            speak("Thanks for letting me help. Have a lovely day.")
            sys.exit()

        # To close Applications
        elif "close notepad" in query:
            speak("Closing Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close browser" in query:
            speak("Closing Browser")
            os.system("taskkill /f /im edge.exe")

        elif "close steam" in query:
            speak("Closing Steam")
            os.system("taskkill /f /im steam.exe")

        elif "close epic games" in query:
            speak("Closing Epic Games")
            os.system("taskkill /f /im EpicGamesLauncher.exe")