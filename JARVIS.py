import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import random as r
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello Sumo.  I  Am  Jarvis.  How can i help You")  # Desktop  Assistant . Please Tell Me How Can I Help You")


def takeCommand():
    # it takes microphone input from user and returns speak output


    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

        print(f"User Said: {query}\n")


    except Exception as e:

        print(e)
        print("Say that again Please...")

        return "None"
    return query

def sentmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sumon3455.ms@gmail.com','01733978064')
    server.sendmail('sumon3455.ms@gmail.com',to,content)
    server.close()



if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()

        # logic for exicuting task on query

        if 'wikipedia' in query:
            print("Searching Wikipedia..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("ACcording to wikipedia")
            print(f"{results}\n")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com',new=1)
        elif 'open google' in query:
            webbrowser.open('google.com',new=1)

        elif 'open my friend' in query:
            webbrowser.open("stackoverflow.com",new=1)

        elif 'play music' in query:
            #music_dir = 'C:\\Users\\user\\Downloads\\failling.mp3'
            music_dir = 'your-path-to-music-folder'
            songs = os.listdir(music_dir)
            songs_list = list(songs)
            random_song = r.choice(songs_list)
            os.startfile(os.path.join(music_dir, random_song))
            
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"Sumon time is {strtime}")

        elif 'play fifa' in query:
            open_fifa = 'D:\\Games\\FIFA 17\\stp-fifa17.exe'
            os.startfile(os.path.join(open_fifa))

        elif 'email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "sumon3255.ms@gmail.com"
                sentmail(to,content)
                speak("email has been sent")
   
            except Exception as e:
                print(e)
                speak("Sorry  Sumon. I am not able to sent this email")
        elif 'bye' in query:
                  exit()

