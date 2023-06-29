from types import coroutine
import pyttsx3
import datetime
import speech_recognition as sr
import pyjokes
from Features import GoogleSearch
from win10toast import ToastNotifier
#from wolframalpha import wolframalpha
from Features import Temp
from DataBase.HomeAuto.SmartBulb import Activate
import webbrowser
from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
 

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("Good Morning!")

    elif hour>=12 and hour<18:
        Speak("Good Afternoon!")   

    else:
        Speak("Good Evening!")  

    Speak("I am Computer . Please tell me how may I help you")       



def run_computer():

    while True:

        query = TakeCommand()

        if 'google search' in query:
            Query = query.replace("computer","")
            query = Query.replace("google search","")
            GoogleSearch(query)
        
        elif 'joke' in query:
         Speak(pyjokes.get_joke())

        elif 'youtube search' in query:
            Query = query.replace("computer","")
            query = Query.replace("youtube search","")
            from Features import YouTubeSearch
            YouTubeSearch(query)

        elif 'set alarm' in query:
            from Features import Alarm
            Alarm(query)

        elif 'download the video' in query:
            from Features import DownloadYouTube
            DownloadYouTube()
            
        elif 'speed test' in query:
            from Features import SpeedTest
            SpeedTest()

        elif "what's your name"  in query:
            Speak("My name is COMPUTER")
            print("My name is COMPUTER")
        elif "where are you from"  in query:
            Speak("I am from the world of Technology")
            print("I am from the world of Technology")  
        elif "how old are you"  in query:
            Speak("I am 0,1")
            print("I am 0,1")
        elif "who created you"  in query:
            Speak("I was developed by  Jeffrin Chandra")
            print("I was developed by  Jeffrin Chandra")          

        elif 'open google' in query:
            webbrowser.open("google.com")
            Speak("opening google")


        elif 'open chrome' in query:
            startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
            Speak("opening chrome") 

        
            
           


        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            Speak("opening whatsapp!")


        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
            Speak("opening instagram!")


        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
            Speak("opening facebook!")


        elif "today new's" in query:
            webbrowser.open("https://tamil.news18.com/")
            Speak("dicovering news!")


        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            Speak("opening Youtube!")


        elif 'open telegram' in query:
            webbrowser.open("https://web.telegram.org/k/")
            Speak("opening telegram!")    


        elif 'whatsapp message' in query:

            name = query.replace("whatsapp message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            Name = str(name)
            Speak(f"Whats The Message For {Name}")
            MSG = TakeCommand()
            from Automations import WhatsappMsg
            WhatsappMsg(Name,MSG)

        elif 'call' in query:
            from Automations import WhatsappCall
            name = query.replace("call ","")
            name = name.replace("computer ","")
            Name = str(name)
            WhatsappCall(Name)

        elif 'show chat' in query:
            Speak("With Whom ?")
            name = TakeCommand()
            from Automations import WhatsappChat
            WhatsappChat(name)

        elif 'space news' in query:


            Speak("Tell Me The Date For News Extracting Process .")

            Date = TakeCommand()

            from Features import DateConverter

            Value = DateConverter(Date)

            from Nasa import NasaNews

            NasaNews(Value)

        elif 'about' in query:
            from Nasa import Summary
            query = query.replace("computer ","")
            query = query.replace("about ","")
            Summary(query)

        elif 'mars images' in query:

            from Nasa import MarsImage

            MarsImage()

        elif 'track iss' in query:

            from Nasa import IssTracker

            IssTracker()

        elif 'near earth' in query:
            from Nasa import Astro
            from Features import DateConverter
            Speak("Tell Me The Starting Date .")
            start = TakeCommand()
            start_date = DateConverter(TakeCommand)
            Speak("And Tell Me The End Date .")
            end = TakeCommand()
            end_date = DateConverter(end)
            Astro(start_date,end_date=end_date)

        elif 'my location' in query:

            from Features import My_Location

            My_Location()

        elif 'where is' in query:

            from Automations import GoogleMaps
            Place = query.replace("where is ","")
            Place = Place.replace("computer" , "")
            GoogleMaps(Place)

        elif 'online class' in query:

            from Automations import OnlinClass

            Speak("Tell Me The Name Of The Class .")

            Class = TakeCommand()

            OnlinClass(Class)

        elif 'write a note' in query:

            from Automations import Notepad

            Notepad()

        elif 'dismiss' in query:

            from Automations import CloseNotepad

            CloseNotepad()

        elif 'time table' in query:

            from Automations import TimeTable

            TimeTable()
          

        elif 'activate the bulb' in query:
            Activate()

            Speak("Should I Start Or Close The Bulb ?")

            step = TakeCommand()

            if 'close' in step:

                from DataBase.HomeAuto.SmartBulb import CloseLight

                CloseLight()

            elif 'start' in step:

                from DataBase.HomeAuto.SmartBulb import StartLight

                StartLight()

        elif 'corona cases' in query:

            from Features import CoronaVirus

            Speak("Which Country's Information ?")

            cccc = TakeCommand()

            CoronaVirus(cccc)

        if 'new tab' in query:

          press_and_release('ctrl + t')

        elif 'close tab' in query:

          press_and_release('ctrl + w')

        elif 'new window' in query:

          press_and_release('ctrl + n')

        
        else:

            from DataBase.ChatBot.ChatBot import ChatterBot

            reply = ChatterBot(query)

            Speak(reply)
  

            if 'bye computer' in query:

                break

            elif 'exit computer' in query:

                break

            elif 'shutdown' in query:

                break
            elif 'command 10 code 10 self distract' in query:

                break
            elif 'temprature' in query:   
              Temp(query) 
            
            #else:
            #    
            #  Result =wolframalpha(query)
            #  Speak(Result)     

while True:
      wishMe()           
      run_computer()
            
