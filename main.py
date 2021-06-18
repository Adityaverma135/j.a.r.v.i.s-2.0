# Project jarvis
import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
import webbrowser
import pyaudio
import os
import time
import winsound
from playsound import playsound
import cv2
import winsound
import time

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        playsound('sound.wav')

    if hour >= 12 and hour < 16:
        speak("Good Afternoon Sir. I am your personal aasistant jarvis. How may i help you?")

    if hour >= 16 and hour < 19:
        winsound.PlaySound('sound.mp3', winsound.SND_ASYNC)

    if hour >= 19 and hour < 24:
        playsound('sound.wav')


def takecommand():
    # It takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"Sir: {query}\n")

    except Exception as e:
        print("Can you say that again")
        # speak('Can,you,say,that,again,')
        return "None"
    return query


def alarm():
    if hour == 9 and minute == 0:
        playsound("alarm.wav")

if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()

        hour = int(datetime.datetime.now().hour)
        minute = int(datetime.datetime.now().minute)
        second = int(datetime.datetime.now().second)


        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(result)
            print(result)

        if 'open google' in query:
            speak('opening google')
            webbrowser.open("www.google.com")

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("www.youtube.com")

        elif 'introduce' in query:
            playsound('intro.mp3')

        elif 'introduction' in query:
            playsound('intro.mp3')

        elif 'what is my name' in query:
            speak('you are Aditya')

        elif 'exit' in query:
            speak('ok, good bye Sir')
            os._exit()

        elif 'you are very good jarvis' in query:
            speak('its my pleasure')

        elif 'jarvis' in query:
            speak('online and ready Sir')

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")

        elif 'whatsapp' in query:
            speak('opening whatsapp')
            webbrowser.open("https://web.whatsapp.com/")

        elif 'zoom' in query:
            Path = "C:\\Users\\adity\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(Path)
            speak('opening zoom')

        elif 'shut down' in query:
            speak('shutting down')
            os.system('shutdown -s')
            os._exit()

        elif ('music') in query:
            speak('which music should I play')

        elif ('believer') in query:
            speak('playing')
            webbrowser.open("https://gaana.com/song/believer-173")

        elif ('?') in query:
            speak('playing')
            webbrowser.open("https://gaana.com/song/question-mark-44")

        elif ('mere gully mein') in query:
            speak('playing')
            webbrowser.open("https://gaana.com/song/mere-gully-mein-1")

        elif ('garmi') in query:
            speak('playing')
            webbrowser.open("https://gaana.com/song/garmi-from-street-dancer-3d-feat-varun-dhawan")

        elif ('boss') in query:
            speak('playing')
            webbrowser.open("https://gaana.com/song/boss-5")

        elif ('tera baap aaya') in query:
            speak('playing')
            webbrowser.open("https://gaana.com/song/tera-baap-aaya")

        elif ('apna time aayega') in query:
            speak('playing')
            webbrowser.open("https://gaana.com/song/apna-time-aayega")

        elif ('never say never') in query:
            speak('playing')
            webbrowser.open("https://gaana.com/song/never-say-never-acoustic-version")

        elif ('filhaal') in query:
            speak('playing')
            webbrowser.open("https://gaana.com/song/filhall")

        elif ('illegal weapon') in query:
            speak('playing')
            webbrowser.open("https://gaana.com/song/illegal-weapon-20-from-street-dancer-3d")

        elif ('function') in query:
            speak('all ,check ,and ,functioning ,properly,')

        elif ('sher aaya sher') in query:
            speak('playing')
            webbrowser.open("https://gaana.com/song/sher-aaya-sher-1")

        elif ('meeting') in query:
            speak('joining')
            webbrowser.open("https://us04web.zoom.us/j/74243354123?pwd=K0UxbDl6WFBXZXZPVitGcHVHVjB5Zz09")

        elif ('ashish chanchlani despacito') in query:
            speak('playing')
            webbrowser.open("https://www.youtube.com/watch?v=scR-7z8diUU")

        elif ('school anthem') in query:
            speak('playing')
            webbrowser.open("https://gaana.com/song/the-student-anthem")

        elif ('yalgaar') in query:
            speak('playing')
            webbrowser.open("https://www.youtube.com/watch?v=zzwRbKI2pn4")

        elif ('lata song') in query:
            speak('playing')
            webbrowser.open("https://gaana.com/artist/lata-mangeshkar")

        elif ('wake up') in query:
            speak('online, and ready sir')

        elif ('temperature') in query:
            speak('searching')
            webbrowser.open(
                "https://www.bing.com/search?q=weather+forecast&cvid=705f9a80851d4033a10a373eba9b32c1&pglt=547&FORM=ANSPA1&PC=HCTS")

        elif ('code') in query:
            speak('opening')
            Path = "C:\\Users\\Aditya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(Path)

        elif ('gaana') in query:
            speak('opening')
            webbrowser.open("www.gaana.com")

        elif ('asli hip hop') in query:
            speak('playing')
            webbrowser.open("https://gaana.com/song/asli-hip-hop")

        elif ('news') in query:
            speak('searching')
            webbrowser.open("https://aajtak.intoday.in/")

        elif ('coronavirus') in query:
            speak('searching')
            webbrowser.open("https://twitter.com/DMKanpur")

        elif ('white hat junior') in query:
            speak('opening')
            webbrowser.open(
                "https://code.whitehatjr.com/s/dashboard?jwt_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlblZlcnNpb24iOm51bGwsImlkIjoiMjY3NTJhZTAtZjk4NC00NmE5LTkwZGEtNTE2ODY5OTY4OWJjIiwiaWF0IjoxNTk3NjM5MjUxfQ.wxRhXhHznQF8zlWT3iVqitl5HUnO39633cLu4VLd2Rg&utm_source=d2_post_trial_email_send&utm_medium=email")

        elif ('message') in query:
            time_hour = datetime.datetime.now().strftime("%H")
            time_min = datetime.datetime.now().strftime("%M")
            speak('sending')



        elif ('aise') in query:
            speak('playing')
            webbrowser.open("https://gaana.com/album/nachunga-aise")


        elif ('pirate') in query:
            speak('playing')
            webbrowser.open("https://www.youtube.com/watch?v=QSWPUfNYgUs")

        elif ("welcome back") in query:
            playsound('sound.wav')


        alarm()
