import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import subprocess
import time
import sys
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


myJoke = pyjokes.get_joke(language="en", category="neutral")


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning Sir')
    elif 12 <= hour < 16:
        speak('Good Afternoon Sir')
    else:
        speak('Good Evening Sir')


print("Loading your AI personal assistant Jeeves")
speak("Loading your AI personal assistant Jeeves")
print('Jeeves is loaded and ready to go')
speak('Jeeves is loaded and ready to go')
wish_me()
speak('I am your personal assistant whose name is Jeeves. How can I help you?')


# noinspection PyBroadException
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        statement = r.recognize_google(audio, language='en-in')
        print(f"User said: {statement}\n")
    except Exception:
        print("Say that again please...")
        return "None"
    return statement


if __name__ == "__main__":
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...please wait')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("wikipedia says")
            print(results)
            speak(results)
        elif 'tell me a joke' in query:
            speak(myJoke)
            print(myJoke)
            time.sleep(10)
        elif "who are you" in query:
            speak("Sir I am Jeeves, your personal assistant")
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
        elif 'open google' in query:
            webbrowser.open('https://www.google.co.in/')
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now sir")
            time.sleep(5)
        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now sir")
            time.sleep(5)
        elif 'open gmail' in query:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now sir")
            time.sleep(5)
        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)
        elif 'exit' in query:
            speak("Thank you for using Jeeves Sir")
            sys.exit()
        elif "log off" in query or "sign out" in query:
            speak("Logging Off")
            subprocess.call(["shutdown", "/l"])

            time.sleep(10)
