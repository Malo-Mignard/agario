
# v1 : pareil mais au moins on peut sortir du programme
# avec la touche 'q', ou avec la souris en fermant la fenêtre


#!/usr/bin/env python
import pygame as pg
from random import randint
import numpy as np

def main():
    clock = pg.time.Clock()

    # on initialise pygame et on crée une fenêtre de 640x640 pixels
    pg.init()
    screen = pg.display.set_mode((640, 640))

    # On donne un titre à la fenetre
    pg.display.set_caption("agario")

    blanc = (255, 255, 255)
    rouge = (255,0,0)

    
    position = (320,320)

    done = False
    while not done:
        clock.tick(150)
        
        screen.fill((0,0,0)) #fond noir
        
        #quadrillage
        x1 = 0 
        y1 = 0 
        x2 = 16*40
        y2 = 0
        for i in range(16):
            y1 = 40*i
            y2 = 40*i
            pg.draw.line(screen, blanc, (x1, y1), (x2, y2))
    
        x1 = 0 
        y1 = 0 
        x2 = 0 
        y2 = 16*40
        for i in range(16):
            x1 = 40*i
            x2 = 40*i        
            pg.draw.line(screen, blanc, (x1, y1), (x2, y2)) #fin quadrillage
        
        
        direction = pg.math.Vector2.normalize(pg.math.Vector2(pg.mouse.get_pos()[0]-position[0],pg.mouse.get_pos()[1]-position[1]))
        pg.draw.circle(screen, rouge, np.add(position,direction), 80)
        
        position = np.add(position,direction)

        
        
        
        
        
        
        
        
        # enfin on met à jour la fenêtre avec tous les changements
        pg.display.update()

        # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
        # ici donc tous les évènements survenus durant la seconde précédente
        for event in pg.event.get():
            # chaque évênement à un type qui décrit la nature de l'évênement
            # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
            if event.type == pg.QUIT:
                done = True
            # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
            elif event.type == pg.KEYDOWN:
                # si la touche est "Q" on veut quitter le programme
                if event.key == pg.K_q:
                    done = True

    pg.quit()


# if python says run, then we should run
if __name__ == "__main__":
    main()

