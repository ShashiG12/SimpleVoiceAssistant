import speech_recognition as sr
import os
import pyttsx3 as tts
import subprocess
import datetime
import webbrowser
import sys

engine = tts.init()
listener = sr.Recognizer()

def speak(audio):
        engine.say(audio)
        engine.runAndWait()
        engine.stop()

def time():
        Time = datetime.datetime.now().strftime("%I:%M")
        return Time

def youtubePlay(searchQuery):
        webbrowser.get().open('https://www.youtube.com/results?search_query=' + searchQuery)

def listen(ask = False):
        with sr.Microphone() as source:
                if ask:
                        print(ask)
                voice = listener.listen(source)
                text = ''
                try:
                        text = listener.recognize_google(voice).lower()
                        print(text)
                except sr.UnknownValueError:
                        print("Sorry I didn't get that")
                except sr.RequestError:
                        print("Sorry I can't help right now")
                return text

def respond(text):
        if 'open chrome' in text:
                speak("Opening Chrome")
                subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        if 'open overwatch' in text:
                speak("Opening Overwatch")
                subprocess.Popen('C:\Program Files (x86)\Overwatch\Overwatch Launcher.exe')
        if "what's the time" in text:
                speak("it is" + time())
        if 'search' in text:
                speak("what do you want to search for?")
                search = listen("what do you want to search for?")
                speak("here's what I found")
                webbrowser.get().open('https://google.com/search?q=' + search)
        if (('play' in text) and ('in youtube' in text)):
                text = text.replace('play', '')
                text = text.replace('in youtube', '')
                speak("playing" + text)
                youtubePlay(text)
        
print("listening...")
text = listen()
respond(text)




