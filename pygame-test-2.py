# -*- coding: utf-8 -*-

print "début du programme..."
import pygame
from pygame.locals import *
import os
import time

# Before you can do much with pygame, you will need to initialize it
pygame.init()
clock = pygame.time.Clock()

def init_screen(taille, boolFS, nbColors): 
    return pygame.display.set_mode(taille,boolFS*FULLSCREEN, nbColors)

def main():
    Fullscreen=False
    screen = init_screen((640, 480), Fullscreen, 16)
    pygame.display.set_caption("Hello !")
    print(os.getcwd())
    img2points = pygame.image.load("deux-points.jpg").convert()
    digit=[]
    for i in range(10):
        digit.append(pygame.image.load(`i`+".jpg").convert())
    loop = True
    heure=""
    while loop:
        hh = "%02d:%02d:%02d"%(time.localtime()[3:6])
        if heure != hh:
            print "======================"
            heure=hh
            x = 240
            y = 100
            for c in list(heure):
                x+=1
                if c==':':
                    screen.blit(img2points, (x, y))
                    x += img2points.get_width()
                else:
                    screen.blit(digit[(ord(c)-ord('0')) % 10], (x, y))
                    x += digit[(ord(c)-ord('0')) % 10].get_width()
        else:
            print "."
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == KEYDOWN:
                if event.key == K_f:
                    Fullscreen = not Fullscreen
                    screen = init_screen((640, 480), Fullscreen, 16)
                if event.key == K_q:
                    loop=False
                print "touche frappée [%c]"%(event.key)
         # Actualisation de l'affichage
        pygame.display.update()
        # 10 fps
        clock.tick(1)

 
if __name__ == '__main__':
    main()
    print "fin du prg."
