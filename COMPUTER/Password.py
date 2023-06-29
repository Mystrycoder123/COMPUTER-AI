import speech_recognition as sr
import pyttsx3

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

def Pass(pass_inp):

       password = "mystrycoder"

       passss  = str(password)

       if passss==str(pass_inp):

              Speak("Access Granted ...!")

              import Main

       else:
              Speak("Access Denied....! tell the password    with in 10 secends   or   this device will blast of   times start :  10,     9,     8,    7  , 6     ,5      ,4        ,3          ,2            ,1     Times Up!!!!!!!")

if __name__ == "__main__" :

       Speak("This Particular File Is Password Protected .")

       Speak("Kindly Provide The Password To Access .")

       passssssss = TakeCommand()

       Pass(passssssss)

