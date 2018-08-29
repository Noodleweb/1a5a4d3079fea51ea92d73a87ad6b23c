import pygame, sys

black = (0,0,0)
white = (255,255,255)
green = (0,200,0)
red = (255,0,0)

width = 800
height = 600


backgroundImg = pygame.image.load("background.png")
backgroundImg = pygame.transform.scale(backgroundImg, (500, 400))
img = pygame.image.load("playbutt.png")
img = pygame.transform.scale(img, (120, 100))

pygame.display.set_mode((width, height))
pygame.display.set_caption('mp3basic')

mp3display = pygame.display.set_mode((800, 600))

#Gör ny font för som läggs till på mp3display
pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 60)
text = font.render("Dopest MP3 player", True, white)

from pygame import *

mixer.init()

mixer.music.load('Chipsound.ogg')
mixer.music.set_volume(0.5)
mixer.music.play(0)




b = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mp3display.fill((0,0,b)) #Ger bakgrundsfärg till mp3display
    mp3display.blit(backgroundImg, (150, 125,)) #Lägger en bild på en mp3 spelare
    mp3display.blit(img,(150,125,))
    mp3display.blit(text, (width/2 - text.get_rect().width/2, height/2 -300))

    #Loopar genom blåa färger från 0 till 150
    if b == 150:
        b1 = -1
    elif b == 0:
        b1 = 1
    b = b+b1
    pygame.display.update()