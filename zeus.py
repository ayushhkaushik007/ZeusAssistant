import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss!")   

    else:
        speak("Good Evening Boss!")  

    speak("I am Zeus. At Your Command.")       

def takeCommand():
  

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Interpreting...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Ayush said: {query}\n")

    except Exception as e:
     
        speak("Pardon please...")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

     
        if 'wikipedia' in query:
            speak('Exploring Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(" Wikipedia Says")
            print(results)
            speak(results)

        elif 'start youtube' in query:
            webbrowser.open("youtube.com")

        elif 'start google' in query:
            webbrowser.open("google.com")

    

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Boss, the time is {strTime}")

        else:
             speak("Out Of Bounds. Thankyou Boss ")
