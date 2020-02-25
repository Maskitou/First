# Alarm
# 1.- Показывать сейчасшнее время
# 2.- Включать музыку в определённое время
# 3.- Запускаться через службу windows
# https://pythonru.com/moduli/modul-time-v-python#Python-timegmtime - time
# https://all-python.ru/osnovy/modul-datetime.html - datetime
# https://younglinux.info/tkinter/window - tkinter windows
import datetime
import time
from turtle import *
a = datetime.datetime.today()
if a.hour == 5:
    print("Welcome to the Programm Dive, Maxim")
seconds =  a.second
minutes = a.minute
hours = a.hour
if a.hour == 18:
    exec(open(r'D:\My_new_updated_project\venv\Some_new_directory\Music_for_alarm.py').read())
    t1 = Turtle()
    while True:
        t1.clear()
        t1.write(str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2),
                 font=("arial", 50, 'normal'))
        seconds += 1
        time.sleep(1)
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1