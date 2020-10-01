#started This project On 06-09-2020
#By Ashutosh
#Please do not copy
#Version 0.1
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import subprocess
import pyjokes
import json
from urllib.request import urlopen
import ctypes
import winshell
import time
import smtplib
import requests
import urllib.request
import re
import pyautogui
import datealm
import psutil
import pyperclip
import clipboard
import pyowm
#from lsHotword import ls
from googletrans import Translator
import wolframalpha
try:
    app = wolframalpha.Client("api id")
except Exception:
    print('some feature are not working')  

emails = {
    "admin": "recepint email id"
}

city="your city"

#speech to text
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  #print(voices[0].id)    

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
         speak("Good AfterNoon Sir!")
    else:
         speak("Good Evening Sir!")

    name =("how may i help you")
    speak("I am your Personal Assistant") 
    speak(name) 

def takeCommand():
    #take microphone input from user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.energy_threshold = 4000
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception:
        print('Your last  command could\'t be heard')
        speak("Sir please say that again")
        return "None"

    return query

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak('the current date is')
    speak(date)
    speak(month)
    speak(year)

def screenshot():
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("shift")
    pyautogui.press("i")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("shift")

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at" +usage +"Percentage")

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("your email", "your pass")
    server.sendmail("your email", to, content)
    server.close()

def languagetranslator():
    try:
        trans=Translator()
        speak("Say the language to translate in")
        language=takeCommand().replace(" ","")
        speak("What to translate")
        content=takeCommand()
        t=trans.translate(text=content,dest=language)
        speak(f"{t.origin} in {t.dest} is{t.text}")
    except:
        speak("Unable to translate")

def weather_info():
    owm=pyowm.OWM('eece000de5e319b3c94c04b2d1bc9b15')
    location=owm.weather_at_place(f'{city}')
    weather=location.get_weather()
    temp=weather.get_temperature('celsius')
    humidity=weather.get_humidity()
    date=datetime.datetime.now().strftime("%A:%d:%B:%Y")
    current_temp=temp['temp']
    maximum_temp=temp['temp_max']
    min_temp=temp['temp_min']
    speak(f'The current temperature on {city} is {current_temp} degree celsius ')
    speak(f'The estimated maximum temperature for today {date} on {city} is {maximum_temp} degree celcius')
    speak(f'The estimated minimum temperature for today {date} on {city} is {min_temp} degree celcius')
    speak(f'The air is {humidity}% humid today')

def convert():
    trans=Translator()
    speak("Say the language to translate in")
    language=takeCommand().replace(" ","")
    pyautogui.keyDown("ctrl")
    pyautogui.press("c")
    pyautogui.keyUp("ctrl")
    tobespoken=pyperclip.paste()
    content=tobespoken
    t=trans.translate(text=content,dest=language)
    speak(f"{t.origin} in {t.dest} is{t.text}")

if __name__== "__main__":
    wishMe()
    
    while True:
       query = takeCommand().lower()
       # Logic for executing tasks based on query
       if 'wikipedia' in query or 'details about' in query or 'tell me about' in query or 'who is' in query:
           speak('Searching Wikipedia....')
           query = query.replace("wikipedia", "")
           query = query.replace("details about", "")
           query = query.replace("tell me about", "")
           query = query.replace("who is", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           speak(results)

       elif 'where is' in query or 'jarvis where is' in query:
           query = query.replace("where is","")
           query = query.replace("jarvis where is","")
           location = query
           speak('Just a second sir, showing you were is' +location)
           url = 'https://www.google.nl/maps/place/' + location + '/&amp;'
           webbrowser.get().open(url)
        
      # To open Webcam
      elif "open camera" in query:
           cap = cv2.VideoCapture(0)
           while True:
               ret, img = cap.read()
               cv2.imshow('webcam', img)
               k = cv2.waitKey(50)
               if k==27:
                   break;
           cap.release()
           cv2.destroyAllWindows()
            
       elif 'check my internet connection' in query or 'am I connected to internet' in query:
           hostname="google.co.in"
           response=os.system("ping -c 1" +hostname)
           if response==0:
               speak("Sir Internet is disconnected")
           else:
               speak("sir you are connected to internet")

       elif 'next window' in query or 'switch back' in query:
           pyautogui.keyDown("alt")
           pyautogui.press("tab")
           time.sleep(1)
           pyautogui.keyUp("alt")
           speak("window switched")

       elif 'previous window' in query or 'last window' in query:
           pyautogui.keyDown("alt")
           pyautogui.press("tab")
           time.sleep(1)
           pyautogui.keyUp("alt")
           speak("anything else sir?")

       elif 'switch window' in query:
           pyautogui.keyDown("alt")
           pyautogui.press("tab")
           speak("which one")
           query = takeCommand()
           if 'next' in query:
               pyautogui.press("right")
               pyautogui.keyUp("alt")
               speak('window switched')
           if "don't switch" in query or 'go back' in query:
               pyautogui.press("left")
               pyautogui.keyUp("alt")
               speak("window switched")

       elif 'close current window' in query:
           pyautogui.keyDown("alt")
           pyautogui.press("f4")
           pyautogui.keyUp("alt")

       elif 'minimise this window' in query or 'minimize current window' in query or 'minimize this' in query or 'minimise current window' in query:
           pyautogui.keyDown("win")
           pyautogui.press("down")
           pyautogui.keyUp("win")
           speak("Current window has been minimized")

       elif 'minimize all windows' in query or 'minimise all' in query or 'minimize all' in query or 'minimize all' in query:
           try:
               os.system('''powershell -command "(new-object -com shell.application).minimizeall()"''')
               speak("all windows minimized")
           except Exception as e:
               speak("Sir there are no windows to minimize")

       elif 'maximize window' in query or 'fullscreen' in query or 'maximise window' in query or 'maximise' in query:
           try:
               pyautogui.keyDown("win")
               pyautogui.press("up")
               pyautogui.keyUp("win")
               speak("This window is now on fullscreen")
           except Exception as e:
               speak("No windows to maximize")

       elif 'type' in query:
           query = query.split(" ")
           lenght=len(query)
           term=query[1:lenght]
           pyautogui.typewrite(' '.join(term))

       elif 'date' in query:
           date()

       elif 'time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"the time is {strTime}")

       elif 'translate' in query:
           languagetranslator()
           
       elif 'convert selected' in query:
           convert()

       elif 'search' in query:
            query = query.replace("search", "")
            url = f"https://www.google.com/search?q={query}"
            webbrowser.get().open(url)
            speak("Here is what I got form search result" + query)

       elif 'open youtube' in query:
           speak('Ok sir Opening Youtube')
           webbrowser.open("https://.youtube.com/")
           speak("Sir what would u like to Watch on youtube?")
           query = takeCommand()
           if 'search' in query:
               query = query.replace("search", "")
               url = f"https://www.youtube.com/results?search_query={query}"
               webbrowser.open(url)
               speak("I've searched for" +query +"in youtube")
           if 'will do it myself' in query or 'leave it' in query or 'no':
               speak("As You like sir!")

       elif 'recently closed tabs' in query or 'recently closed tabs' in query:
           try:
               pyautogui.keyDown("ctrl")
               pyautogui.keyDown("shift")
               pyautogui.press("T")
               pyautogui.keyUp("ctrl")
               pyautogui.keyUp("shift")
               speak("Recently closed tabs has been opened")
           except Exception as e:
               speak("No recent tabs found")

       elif 'open chrome' in query:
           try:
               speak('opening chrome')
               codepath = "chrome.exe"
               os.startfile(codepath)
           except Exception as e:
               speak("Chrome Not found")

       elif 'close chrome' in query:
           os.system("taskkill /f /im chrome.exe")
           speak('chrome has been closed')

       elif 'open spotify' in query or 'play music on spotify' in query:
           speak ('As u like sir ')
           codepath = "spotify.exe"
           os.startfile(codepath)

       elif 'close spotify' in query:
           os.system("taskkill /f /im spotify.exe")
           speak('spotify closed')
           
       elif 'play music' in query:
           music_dir = 'C:\\Users\\multi\\Music'
           songs = os.listdir(music_dir)
           rd = random.choice(songs)
           print(songs)
           for songs in songs:
               if songs.endswith('.mp3'):
                   os.startfile(os.path.join(music_dir, songs))

       elif 'some upgrade' in query or 'open code' in query or 'want to update you' in query or 'Open visual studio' in query:
           try:
               codepath = "Code.exe"
               os.startfile(codepath)
               speak('opening')
           except Exception as e:
               speak("Visual code not found in your computer")

       elif 'close code' in query or 'close visual studio' in query:
           os.system("taskkill /f /im Code.exe")
           speak('code has been closed')

       elif 'open premiere pro' in query:
           try:               
               codepath = "C:\\Program Files\\Adobe\\Adobe Premiere Pro 2020\\Adobe Premiere Pro.exe" 
               os.startfile(codepath)
               speak('opening Premiere pro')
           except Exception as e:
               speak('Sir Premiere pro not found in your computer')

       elif 'joke' in query or 'make me laugh' in query:
            speak(pyjokes.get_joke())

       elif 'who made you' in query or 'who created you' in query:
            speak("I have been created by Ashutosh.")

       elif 'remember' in query:
           speak("what should I remember?")
           query = takeCommand()
           speak("you said me to remember that" +query)
           remember = open('query.txt','w')
           remember.write(query)
           remember.close()

       elif 'do you know anything' in query:
           try:
               remember = open('query.txt','r')
               speak("you said me to remember that" +remember.read())
           except Exception as e:
               speak("sir you didn't said anything to remember")
    
       elif 'make a note' in query or 'write down' in query:
           speak("What would you like me to note down?")
           note_text = takeCommand()
           note(note_text)
           speak("I've made a note of that. Anything else?")
           query = takeCommand()
           if "no" in query:
               speak('ok sir')
           if "yes" in query:
               speak('Go on sir')

       elif 'calculate' in query:     
            app_id = "Q539P8-JQHRU4WLJU" 
            client = wolframalpha.Client(app_id) 
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

       elif 'weather of' in query:
            api_key="your api id"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            query = query.replace("weather of", "")
            city_name = query
            speak("weather of" +city_name +"is")
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

       elif 'email' in query:
           try:
               speak("Whom U would like to send email")
               name = takeCommand()
               to = emails[name]
               speak("What should i say?")
               content = takeCommand()
               speak("Confirm, yes or no")
               mailconfig = takeCommand()
               flag = 0
               while flag != 1:
                   if "yes" in mailconfig:
                       sendEmail(to, content)
                       speak("Email has been sent succesfully")
                       flag = 1
                   elif "no" in mailconfig:
                       speak("Ok sir request has been cancelled")
                       break
                   else:
                       speak("Unable to confirm, please say again")
                       break
           except Exception as e:
               speak("Could not send email")

       elif 'lock window' in query or 'lock the system' in query:
           try:
               speak("locking the device")
               ctypes.windll.user32.LockWorkStation()
           except Exception as e:
               speak("Sir windows is already locked")

       elif 'empty recycle bin' in query or 'clean recycle bin' in query:
           try:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin is cleaned")
           except Exception as e:
               speak("Recycle bin is already cleaned")

       elif 'cpu usage' in query or 'cpu uses' in query or 'check my cpu' in query:
           cpu()

       elif 'alarm' in query:
           datealm.alarm(query)

       elif 'take screenshot' in query:
           screenshot()
           speak('Screenshot saved in radeon relive')

       elif 'how are you' in query or 'how are you doing' in query:
           speak("am fine sir, what about you?")
           query = takeCommand()
           if 'am also good' in query or 'am also fine' in query or 'healthy' in query or 'fine' in query:
               speak("wow")
           if 'not fine' in query or 'not well' in query or 'not good' in query or 'felling low' in query or 'not in mood' in query:
               speak("sad to hear that sir, how may I change your mood, May i play music for You?")
               query = takeCommand()
               if 'ok' in query or 'sure' in query or 'hmm' in query or 'alright' in query or 'yeah' in query or 'play music' in query:
                   speak('ok sir playing music for you')
                   music_dir = 'C:\\Users\\multi\\Music'
                   songs = os.listdir(music_dir)
                   rd = random.choice(songs)
                   print(songs)
                   for songs in songs:
                       if songs.endswith('.mp3'):
                           os.startfile(os.path.join(music_dir, songs))
               elif "no" in query or "it's ok" in query or "don't play" in query or 'nope' in query:
                   speak("Ok sir as You like!")

       elif 'goodbye' in query or 'see you jarvis' in query or 'jarvis down' in query or 'jarvis shutdown' in query or 'bye jarvis' in query or 'keep quiet' in query:
           speak("Do You want me to shutdown")
           query = takeCommand()
           if 'no' in query or 'cancel' in query:
               speak("Process cancelled")
           if 'yes' in query or 'yep' in query or 'shutdown' in query:
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    speak("Have a Nice day sir!")
                    exit()
                elif hour>=18 and hour<24:
                    speak("Ok, good Night sir")
                    exit()
       #ls.lsHotword_loop()
