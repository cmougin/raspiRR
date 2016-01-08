# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import time

wifi_images = {
              "default":"wifi.png",
              "W1":"wifiOn.png"
          }

bell_images = {

              "default":"bell.png",
              "B1":"bellOn.png"
          }
          
fondecran = {
                "default":"background.png"
          }  
          
horloge_images = {
                "default":"horloge.png",
                "0":"0.png",
                "1":"1.png",
                "2":"2.png",
                "3":"3.png",
                "4":"4.png",
                "5":"5.png",
                "6":"6.png",
                "7":"7.png",
                "8":"8.png",
                "9":"9.png"
        }      
        
def load_pictures(icone_files, dimensions=(0,0)):
    icone={}
    for key in icone_files:
        if (dimensions == (0,0)):
            icone[key] = pygame.image.load(icone_files[key]).convert()
        else:
            icone[key] = pygame.transform.scale(
            pygame.image.load(icone_files[key]).convert(),
            dimensions)
#        print "icone[%s] loaded."%(key)
    return(icone)

class Picto:
    def __init__(self, ihm, icones, position):
        self.icones = icones
        self.position = position
        self.ihm = ihm
        
    def display(self, screen):
        ihm.rectangles.blit(self, self.icones["default"], self.position)
        
    def clicked(self):
        print "icone clicked"
    
class Horloge:
    def __init__(self, ihm):
        self.clock = Picto(ihm, load_pictures(horloge_images), (4, 76))
        self.heure = "0000"
        self.ihm = ihm
        
    def display(self, screen):
        hhmm = "%02d%02d"%(time.localtime()[3:5])
        ihm.rectangles.blit(self, self.clock.icones["default"], (4, 76))
        ihm.rectangles.blit(self, self.clock.icones[hhmm[0]], (79, 115))
        ihm.rectangles.blit(self, self.clock.icones[hhmm[1]], (129, 115))
        ihm.rectangles.blit(self, self.clock.icones[hhmm[2]], (200, 115))
        ihm.rectangles.blit(self, self.clock.icones[hhmm[3]], (249, 115))
        self.heure = hhmm

    def clicked(self):
        print "horloge clicked"
    
class Rectangles:
    def __init__(self, ihm):
        self.rectangles = []
        self.ihm = ihm
        
    def add(self, rectangle, callback):
        self.rectangles.append((rectangle, callback))
        
    def raz(self):
        self.rectangles=[]
        
    def blit(self, callback, image, position):
        self.add(Rect(position, image.get_size()), callback)
        ihm.screen.blit(image, position)
        
    def click(self, position):
        for rect, callback in self.rectangles:
            if rect.collidepoint(position):
                callback.clicked()
 
class IHM:
    def __init__(self):
        self.Fullscreen = False
        self.screen = self.init_screen((480, 320), self.Fullscreen, 16)
        pygame.display.set_caption(u"IHM en cours d'initialisation...")
        self.background = load_pictures(fondecran, (480,320))["default"]
        self.wifi = Picto(self, load_pictures(wifi_images, (64, 50)), (0, 270))
        self.bell = Picto(self, load_pictures(bell_images, (53, 50)), (0, 14))
        self.horloge = Horloge(self)
        self.rectangles=Rectangles(self)
        pygame.display.update()
            
    def init_screen(self, taille, boolFS, nbColors): 
        return pygame.display.set_mode(taille,boolFS*FULLSCREEN, nbColors)

    def run_for_ever(self):
        loop = True
        pygame.display.set_caption(u"running !")
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                elif event.type == KEYDOWN:
                    if event.key == K_f:
                        self.Fullscreen = not self.Fullscreen
                        self.screen = self.init_screen((640, 480), 
                                                       self.Fullscreen, 16)
                    elif event.key == K_q:
                        loop=False
                    print "touche frappée [%c]"%(event.key)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print "mouse clicked in (%d,%d)"%(event.pos)
                    self.rectangles.click(event.pos)
             # Actualisation de l'affichage
            self.screen.blit(self.background, (0, 0))
            self.rectangles.raz()
            self.wifi.display(self.screen)
            self.bell.display(self.screen)
            self.horloge.display(self.screen)
            pygame.display.update()
            clock.tick(1000)
 
if __name__ == '__main__':
    print "début du programme..."
    passed,failed = pygame.init()
    clock = pygame.time.Clock()
    ihm = IHM()
    ihm.run_for_ever()
    print "fin du prg."
    

