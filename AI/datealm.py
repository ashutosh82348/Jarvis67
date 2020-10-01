import datefinder
import winsound
import datetime
import os
from playsound import playsound


def alarm(text):
    dTimeA = datefinder.find_dates(text)
    for mat in dTimeA:
        print(mat)
    stringA = str(mat)
    timeA = stringA[11:]
    hourA = timeA[:-6]
    hourA = int(hourA)
    minA = timeA[3:-3]
    minA = int(minA)


    while True:
        if hourA == datetime.datetime.now().hour:
            if minA == datetime.datetime.now().minute:
                print("alarm is running")
                playsound('D:\\Projects\\AI\\alarm05.mp3',winsound.SND_LOOP)
            elif minA<datetime.datetime.now().minute:
                break

#alarm("set alarm at time am/pm")