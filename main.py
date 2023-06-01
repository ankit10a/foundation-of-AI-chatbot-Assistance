import os
import smtplib
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import winshell
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)  
    if hour >= 0 and hour <12:
        speak("Good Morning !")  
    elif hour>=12 and hour <18:
        speak("Good Afternoon")
    else :
        speak('Good Evening !')
    
    speak("I am bot. Please tell me how may I help you")

def takeCommand():
    print("check")
    #It takes microphone input from the user and returns string output
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recog.pause_threshold = 1
        recog.adjust_for_ambient_noise(source, duration=0.2)
        audio = recog.listen(source)
    
    try: 
        print("Recognizing....")
        query = recog.recognize_google(audio, language="en-in")
        print(query)
        print(f"User Said:{query}\n")
    
    except Exception as e:
        # print("err--.",e)
        print("say That again Please....")
        speak("say That again Please....")
        return ""
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ankit.dublin@gmail.com', 'Ankit@@10')
    server.sendmail('ankit.dublin@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    # speak("Welcome How May I help you?")
    wishMe()
    while True:
        str = takeCommand()
        query = str.lower()

        if "wikipedia" in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif ('open browser' in query or 'open google' in query):
            webbrowser.open("google.com")
        elif "who are you" in query or "define yourself" in query:
            speak("Hello, I am an Assistant. Your Assistant. I am here to make your life easier. You can command me to perform various tasks such as asking questions or opening applications etcetera")
        elif "made you" in query or "created you" in query:
            speak("I was created by Ankit")
        elif "your name" in query:
            speak("My name is Assistant")
        elif "who am i" in query:
            speak("You must probably be a human")
        elif "why do you exist" in query or "why did you come to this word" in query:
            speak("It is a secret")
        elif "how are you" in query:
            speak("I am awesome, Thank you")
            speak("How are you?")
        elif "fine" in query or "good" in query:
            speak("It's good to know that your fine")
        elif 'tell time' in query or 'whats the time' in query or 'current time' == query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif "open" in query:
            if "chrome" in query:
                speak("Opening Google Chrome")
                os.startfile(
                    r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                )
            elif "word" in query or 'docs' in query:
                speak("Opening Microsoft Word")
                os.startfile(
                    "C:\Program Files\Microsoft Office\Office16\WINWORD.EXE"
                    )
            elif "excel" in query:
                speak("Opening Microsoft Excel")
                os.startfile(
                    "C:\Program Files\Microsoft Office\Office16\EXCEL.EXE"
                    )
            elif "powerpoint" in query or "ppt" in query:
                speak('Opening Microsoft PowerPoint')
                os.startfile("C:\Program Files\Microsoft Office\Office16\POWERPNT.exe")
            elif 'code Editor' in query or ('code ' in query) or 'visual code studio' in query:
                path = "C:\\Users\\ankit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(path)
            elif "youtube" in query:
                speak("Opening Youtube")
                webbrowser.open("https://youtube.com/")
            elif "google" in query:
                speak("Opening Google")
                webbrowser.open("https://google.com/")
            elif "stackoverflow" in query.lower():
                speak("Opening StackOverFlow")
                webbrowser.open("https://stackoverflow.com/")
            else:
                speak("Application not available") 
        elif "youtube" in query.lower():
            ind = query.lower().split().index("youtube")
            search = query.split()[ind + 1:]
            webbrowser.open(
                "http://www.youtube.com/results?search_query=" +
                "+".join(search)
            )
            speak("Opening on youtube"+"".join(search))
        elif "search" in query.lower():
            ind = query.lower().split().index("search")
            search = query.split()[ind + 1:]
            webbrowser.open(
                "https://www.google.com/search?q=" + "+".join(search))
            speak("Searching " + "".join(search) + " on google")
        elif 'visual code studio' in query or 'vs code' in query:
            path = "C:\\Users\\ankit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif "joke" in query:
            speak (pyjokes.get_joke())
        elif "empty recycle bin" in query:
            winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
            speak("Recycle Bin Emptied")

        elif 'email to yourself' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ankit.dublin@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Ankit. I am not able to send this email")    
        elif 'terminate yourself' in query or 'exit program' in query:
            speak('program terminated')
            break

