import datetime
import time
import pygame

def set_alarm():
    times = input("What time do you want your alarm at? \n The format is, hh:mm:ss : ")
    print("Your alarm has been set sucessfully at :",times)
    go_alarm(times)

# def alarm_tick(): 
#     pygame.mixer.init()
#     pygame.mixer.music.load("C:\Krish\Every single python program\python classes\icking-clock-sound-effect-1-mp3-edition-264451.mp3")
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         time.sleep(1)

def buzz_alarm():
    print("BUZzZZzZ")
    pygame.mixer.init()
    # pygame.mixer.music.load("mixkit-trumpet-fanfare-2293.wav")
    pygame.mixer.music.load("C:\Krish\Every single python program\python classes\skibidi-toilet.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    print("Helo")

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

