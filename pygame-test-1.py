# -*- coding: utf-8 -*-
"""

"""

print "début du programme..."

import pygame

# Before you can do much with pygame, you will need to initialize it
pygame.init()

print(pygame.font.get_fonts())
clock = pygame.time.Clock()
 
CIEL = 0, 200, 255
ORANGE = 255, 100, 0
 
def main():
    fenetre = pygame.display.set_mode((640, 480))
 
    loop = True
    while loop:
        background = pygame.Surface(fenetre.get_size())
        background.fill(CIEL)
 
        # Définition de la police
        bigText = pygame.font.SysFont('niagarasolid', 36)
 
        # Définition du texte
        # render(text, antialias, rgb color tuple)
        title_text = bigText.render(u"Maître Corbeau sur un arbre perché",
                                    True, ORANGE)
        # Position: horizontal au centre , vertical = 50
        # Le centre du texte est au centre quelque soit le texte
        # Le texte est inscrit dans un rectangle
        textpos = title_text.get_rect()
        # Placement du texte en x et y
        textpos.centerx = fenetre.get_rect().centerx
        textpos.centery = 50
 
        # Collage du texte sur le fond
        background.blit(title_text, textpos)
 
        # Ajout du fond dans la fenêtre
        fenetre.blit(background, (0, 0))
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
 
        # Actualisation de l'affichage
        pygame.display.flip()
        # 10 fps
        clock.tick(10)
 
if __name__ == '__main__':
    main()
    print "fin du prg."