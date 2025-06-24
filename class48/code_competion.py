import datetime
import time
import pygame

def set_alarm():
    times = input("What time do you want your alarm at? \n The format is, HH:MM:SS : ")
    print("Your alarm has been set sucessfully at :",times)
    go_alarm(times) 

def buzz_alarm():
    print("BUZzZZzZ")
    pygame.mixer.init()
    pygame.mixer.music.load("C:\Krish\Every single python program\python classes\mixkit-trumpet-fanfare-2293.wav")
    pygame.mixer.music.play()
    pygame.mixer.music.get_busy()
    time.sleep(1)

def go_alarm(times):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    while current_time < times:
        print(current_time)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == times:
            buzz_alarm()
            break
        time.sleep(1)      
        
set_alarm()

