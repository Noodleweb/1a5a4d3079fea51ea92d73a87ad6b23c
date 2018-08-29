import pygame, sys

black = (0,0,0)
white = (255,255,255)
green = (0,200,0)
red = (255,0,0)

img = pygame.image.load("playbutt.png")


pygame.display.set_mode((800, 600))
pygame.display.set_caption('mp3basic')

mp3display = pygame.display.set_mode((800, 600))

from pygame import *



mixer.init()

mixer.music.load('Chipsound.ogg')
mixer.music.set_volume(0.5)
mixer.music.play(0)





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mp3display.blit(img,(150,125,))
    pygame.display.update()