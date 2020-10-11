import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import cv2
import time
rom PIL import ImageGrab

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
            music_dir = 'C:\\Users\\user\\Downloads\\failling.mp3'
            os.startfile(os.path.join(music_dir))
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
         elif "show battery status" in query:
            battery=psutil.sensors_battery()
            percent = str(battery.percent)
            plugged=battery.power_plugged
            #plugged = "Plugged In" if plugged else "Not Plugged In"
            if plugged:
                plug='plugged'
            else:
                plug='not plugged'
            per = int(percent)
            # plugged = "Plugged In" if plugged else "Not Plugged In"
            if plugged:
                plug = "plugged"
            else:
                plug = "not_plugged"

            if plug == 'not_plugged' and per <= 30:
                speak("Sir your battery is ")
                speak(percent)
                speak("sir please pluggin your charger because your battery is low ")
            elif plug == 'plugged' and battery > 20:
                speak("Sir your battery is ")
                speak(percent)
            elif plug == 'not_plugged' and per > 20:
                speak("Sir your battery is ")
                speak(percent)
            elif plug == 'plugged' and battery <= 20:
                speak("Sir your battery is ")
                speak(percent)
                speak("sir your battery is low dont remove your charger")
            elif plug == 'plugged' and battery == 100:
                speak("Sir your battery is ")
                speak(percent)
                speak("sir your battery is full please remove charger ")
            else:
                print(percent)
                elif "camera" in query or "take a photo" in query:

            speak("Note : sir if you want to capture the image the press on spacebar")
            # 1.creating a video object
            video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

            # 2. Variable
            a = 0
            # 3. While loop
            while True:
                a = a + 1
                # 4.Create a frame object
                check, frame = video.read()
                # 5.show the frame!
                cv2.imshow("Capturing", frame)
                # 6.for playing
                key = cv2.waitKey(1)

                if key%256 == 32: #32 ascii value of sapcebar
                    break
            # 7. image saving
            for i in range(100):
                drive_letter = "C:\\Users\\ravi singh\\PycharmProjects\\Camera_Img\\"
                folder_name = r'downloaded-files'
                folder_time = datetime.datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
                extention = '.jpg'
                folder_to_save_files = drive_letter + folder_name + folder_time + extention

                showPic = cv2.imwrite(folder_to_save_files, frame)
                print(folder_to_save_files)
                print(showPic)
                break
            # 8. shutdown the camera
            video.release()
            cv2.destroyAllWindows()
                elif "take a screenshot" in query or "take screenshot" in query:
            snapshot=ImageGrab.grab()
            drive_letter = "C:\\Users\\ravi singh\\PycharmProjects\\Screenshot\\"
            folder_name = r'downloaded-files'
            folder_time = datetime.datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
            extention = '.jpg'
            folder_to_save_files = drive_letter + folder_name + folder_time + extention
            snapshot.save(folder_to_save_files)
            speak("done sir")
        elif 'bye' in query:
                  exit()

