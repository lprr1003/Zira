import os
import random
import datetime
import send_mail
import sys
import time
import wish_me as wm
import webbrowser
import pywhatkit as kit #
import pygame #
import spk 
import speech_recognition as sr #
import wikipedia 
from moviepy.editor import * #
from tkinter import * 
import pyautogui #
import requests #
from cv2 import VideoCapture,imshow,waitKey,destroyAllWindows 
from bs4 import BeautifulSoup #
import speedtest #
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
# from mainui import Ui_MainWindow


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExe()

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 3    #new
            r.energy_threshold = 300

            audio = r.listen(source)

        try:
            print("Recognising...")
            query = r.recognize_google(audio,language='en-in')
            print(f"user said : {query}\n")
        except Exception as e:
            print("Something went wrong.Try again..")

        return query

    def TaskExe(self):
        wm.maen()
        while (True):
            self.query = self.listen().lower()
            if 'wikipedia' in self.query:
                spk.speak("Searching wikipedia")
                self.query = self.query.replace('wikipedia', '')
                results = wikipedia.summary(self.query, sentences=2)
                spk.speak("According to wikipedia")
                spk.speak(results)
                

            elif 'hello' in self.query:
                spk.speak("Hello ma'am")

            elif 'open google' in self.query:
                spk.speak("What should I search on google")
                cm = self.listen()
                webbrowser.open(f"{cm}")

            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")

            elif 'song' in self.query:
                spk.speak("tell me the name of song")
                name = self.listen()
                kit.playonyt(f"{name}")

            elif 'play music' in self.query:
                music_dir = "D:\parul phone\music"
                song = os.listdir(music_dir)
                rd = random.choice(song)
                os.startfile(os.path.join(music_dir,rd))

            elif 'the time' in self.query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                spk.speak(f"the time is {strtime}")

            elif 'open pycharm' in self.query:
                code_path = "D:\\newPycharm\\PyCharm Community Edition 2021.2.2\\bin\\pycharm64.exe"
                os.startfile(code_path)

            elif 'open whatsapp' in self.query:
                path = "https://web.whatsapp.com//"
                os.startfile(path)

            elif 'send mail' in self.query:
                try:
                    spk.speak("Tell me the content of mail")
                    content = self.listen()
                    spk.speak("Tell me the email id to whom you want to send the mail")
                    to = self.listen()
                    to = to.replace(' ', '') + '@gmail.com'
                    send_mail.sendemail(to, content)
                    spk.speak("Email has been sent")

                except Exception as e:
                    print(e)
                    spk.speak("Something went wrong")

            elif 'play video' in self.query:
                clip = VideoFileClip('D:\\kaam ki cheej\\wedding.mp4').resize(0.5)
                clip.preview()
                pygame.quit()

            elif 'shut down' in self.query:
                os.system("shutdown /s /t 1")

            elif 'temperature' in self.query:
                search = "temperature"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                spk.speak(f"current {search} is {temp}")

            elif 'open notepad' in self.query:
                os.system("C:\\Windows\\notepad.exe")

            elif 'send message' in self.query:
                spk.speak("Phone no. of that person")
                ph = self.listen()
                spk.speak("what message do you want to convey")
                msg = self.listen()
                kit.sendwhatmsg_instantly(f"+91{ph}", msg,15,True,4)

            elif 'take screenshot' in self.query:
                spk.speak("Please tell me the name of this file.")
                name = self.listen()
                spk.speak("Hold the screen for few seconds.")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                spk.speak("screenshot is done")

            elif 'camera' in self.query:
                cap = VideoCapture(0)
                while(True):
                    ret,img = cap.read()
                    imshow('webcam', img)
                    k = waitKey(50)
                    if k==27:
                        break;
                cap.release()
                destroyAllWindows()

            elif 'speed' and 'internet' in self.query:
                st = speedtest.Speedtest()
                dl = st.download()
                dl = dl//8
                up = st.upload()
                up = up//8
                spk.speak(f"downloading speed is {dl} bytes per second and uploading speed is {up} bytes per second")

            elif 'sleep' or 'bye' in self.query:
                spk.speak("I am going to sleep you can call me any time")
                sys.exit()