import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load(r"Catfish.mp3")
pygame.mixer.music.play()
stop_the_alarm = input()
if stop_the_alarm.isprintable():
    pygame.mixer.music.stop()
if pygame.mixer.get_busy():
    time.sleep(1)