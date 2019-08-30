import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import sys
import math
import re
import urllib
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import requests
import random
import pyowm
import time
import wolframalpha
from pygame import mixer

url = 'https://samples.openweathermap.org/data/2.5/weather?id=665004&appid=0118c4ca922a0d0d17c775e858bcf161'
chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Heisenberg Sir. I stand to serve, Temporarily.")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("degi.nandor@gmail.com", "deginandor")
    server.sendmail("degi.nandor@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        if "where is" in query:
            query = query.split(" ")
            location = query[2]
            speak("Hold on, I will show you where " + location + " is.")
            os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query)
            speak("According to Wikipedia")
            speak(results) 

        elif 'current weather' "how the weather looks like" "weather" in query:
                owm = pyowm.OWM('0118c4ca922a0d0d17c775e858bcf161')
                observation = owm.weather_at_place("Targu-Mures, RO")
                w = observation.get_weather()
                temperature = w.get_temperature('celsius')
                tomorrow = pyowm.timeutils.tomorrow()
                speak(w)
                speak(temperature)
                speak(tomorrow)
                speak('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (
                    observation, temperature['temp_max'], temperature['temp_min'], tomorrow['temp_max'], tomorrow['temp_min']))

        elif 'open' in query:
            reg_ex = re.search('open (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                url = 'https://www.' + domain + '.com'
                webbrowser.open(url)
                speak('The website you have requested has been opened for you, Sir.')
            else:
                pass

#MATH------------------------------

        elif "what\'s the value of pi" in query:
            pi = math.pi
            speak("The approximate value of PI is " + str(math.pi) )

        elif "calculate" in query:

            app_id = "degi.nandor@gmail.com"
            client = wolframalpha.Client(app_id)

            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            speak("The answer is " + answer)
#MATH---------------------------------------
#        elif "open youtube" in query:
#             speak('The website you have requested has been opened for you, Sir.')
#             time.sleep(1)
#             webbrowser.get(chrome).open("youtube.com")

#        elif "open github" in query:
#             speak('The website you have requested has been opened for you, Sir.')
#             time.sleep(1)
#             webbrowser.get(chrome).open("github.com")

#        elif "open google" in query:
#             speak('The website you have requested has been opened for you, Sir.')
#             time.sleep(1)
#             webbrowser.get(chrome).open("google.com")

#        elif "open twitch" in query:
#             speak('The website you have requested has been opened for you, Sir.')
 #            time.sleep(1)
#             webbrowser.get(chrome).open("twitch.tv")

#        elif "open my website" in query:
#             speak('The website you have requested has been opened for you, Sir.')
#             time.sleep(1)
#             webbrowser.get(chrome).open("hunguy.cf")

        elif "play music" in query:
            music_dir = "C:\\Users\\degin\\Documents\\Alkotások\\Folyamatban levő projectjeim\\8D AUDIO\\kesz"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "what\'s up" in query:
            speak('Just Chilling.')

        elif "Who is your creator" or "Who created you" in query:
            speak("The person who created me is named Dégi Nándor.\n")
            speak("I was created in May 28 in 2019.")

        elif "what\'s your name?" in query:
            speak("my name is Heisenberg, sir and i was created by Dégi Nándor")

        elif "the time" or "what is the time right now" in query:
            now = datetime.datetime.now()
            speak('Current time is %d hours %d minutes' %(now.hour, now.minute))

        elif "open atom" in query:
            path = "C:\\Users\\degin\\AppData\\Local\\atom\\atom.exe"
            os.startfile(path)

        elif 'news for today' or "tell me the news for today" in query:
            try:
                news_url="https://news.google.com/news/rss"
                Client=urlopen(news_url)
                xml_page=Client.read()
                Client.close()
                soup_page=soup(xml_page,"xml")
                news_list=soup_page.findAll("item")
                for news in news_list[:15]:
                    speak(news.title.text.encode('utf-8'))
            except Exception as e:
                    print(e)

        elif "email" in query:
            print('proba')
