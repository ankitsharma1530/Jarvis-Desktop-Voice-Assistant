import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
print(voices)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good morning Sir")
    elif(hour>=12 and hour<18):
        speak("Good afternoon Sir")
    else:
        speak("Good evening ! Sir")
    speak("This is, roger here. How may i help you ?")
# take command accept the user voice message 
# and return the string format of our user voice message
def takecommand():
    # this is the input we are going to take from the user microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #pause thersold is actually the time of given by the jarvis to you to speak
        
        r.pause_threshold = 1 
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("User said",query)
    except Exception as e:
        print("Say that again please sir")
        return "None"
    return query
    

if __name__ == "__main__":
    wishme()
    if(1):
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open geeks for geeks' in query:
            webbrowser.open("geeksforgeeks.org")
        elif 'the current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'visual studio code' in query:
        #these are my systems path
            codePath1 = "C:\\Users\\sharm\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath1)
        elif 'open brave' in query:
        #these are my systems path
            codePath2 = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codePath2)
