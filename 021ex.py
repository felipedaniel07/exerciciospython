#Codigo está um pouco diferente pois eu do futuro vim e arrumei pois o som não saia :)
import pygame
pygame.init()
pygame.mixer.music.load('moonlight.mp3')
pygame.mixer.music.play()
pygame.event.wait()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
