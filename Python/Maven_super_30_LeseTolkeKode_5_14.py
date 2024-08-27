python
#required modules
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import sys
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Logger setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize text-to-speech engine
moon = pyttsx3.init('sapi5')
voices = moon.getProperty('voices')
moon.setProperty('voice', voices[0].id)

# Defining functions
def speak(audio):
    moon.say(audio)
    moon.runAndWait()

def Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        speak("I didn't catch that. Could you please repeat?")
    except sr.RequestError as e:
        speak("Sorry, I am having trouble connecting to the service.")
        logger.error(f"Error with speech recognition: {e}")
    return None

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
    speak("How can the Moon help you?")

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
        server.sendmail(os.getenv('EMAIL_USER'), to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        speak("Mail not sent due to some error!")
        logger.error(f"Failed to send email: {e}")

def open_webpage(url, name):
    try:
        speak(f"Opening {name}")
        webbrowser.open(url)
    except Exception as e:
        speak(f"Sorry, I couldn't open {name}")
        logger.error(f"Failed to open {name}: {e}")

def play_music():
    music_dir = 'D:\\Songs'
    if os.path.exists(music_dir):
        songs = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]
        if songs:
            song = random.choice(songs)
            speak(f"Playing {song}")
            os.startfile(os.path.join(music_dir, song))
        else:
            speak("No songs found in the directory.")
    else:
        speak("Music directory does not exist.")

def open_ide(ide_name):
    ides = {
        "netbeans": "C:\\Program Files\\NetBeans 8.2\\bin\\netbeans64.exe",
        "thonny": "C:\\Users\\Madhav\\AppData\\Local\\Programs\\Thonny\\thonny.exe",
        "pycharm": "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe",
        "vscode": "C:\\Users\\Madhav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    }

    ide_name = ide_name.lower()
    for key, value in ides.items():
        if key in ide_name:
            if os.path.exists(value):
                speak(f"Starting {key.capitalize()}...")
                os.startfile(value)
            else:
                speak(f"{key.capitalize()} not found.")
            return
    speak("IDE not recognized. Please try again.")

# Main body of the code
if __name__ == "__main__":
    wishMe()

    while True:
        query = Command()

        if query is None:
            continue

        if 'wikipedia' in query or 'what is' in query or 'who is' in query or 'define' in query or 'definition' in query or 'meaning' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            open_webpage("https://www.youtube.com", "YouTube")

        elif 'open google' in query:
            open_webpage("https://www.google.com", "Google")

        elif 'open stackoverflow' in query:
            open_webpage("https://www.stackoverflow.com", "StackOverflow")

        elif 'play music' in query:
            play_music()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'coding' in query or 'code' in query:
            speak("Which IDE do you want to use, sir?")
            ide_query = Command()
            if ide_query:
                open_ide(ide_query)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = Command()
                to = os.getenv('EMAIL_TO')
                sendEmail(to, content)
            except Exception as e:
                speak("Mail not sent due to some error!")
                logger.error(f"Error in email function: {e}")

        elif 'name' in query:
            speak('I am Moon')

        else:
            speak("SORRY? How can I help you?")