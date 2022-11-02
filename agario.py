#!/usr/bin/env python
import pygame as pg
from random import randint
import numpy as np

def main():
    clock = pg.time.Clock()

    taille_fen = 40*16
    # on initialise pygame et on crée une fenêtre de 640x640 pixels
    pg.init()
    screen = pg.display.set_mode((taille_fen, taille_fen))

    # On donne un titre à la fenetre
    pg.display.set_caption("agario")

    blanc = (255, 255, 255)
    rouge = (255,0,0)
    vert = (0,255,0)
    bleu = (0,0,255)
    violet = (238,130,238)
    rose = (255,192,203)
    orange = (255,128,0)

    position = pg.math.Vector2((taille_fen//2,taille_fen//2)) #initialisation position blop
    rayon = 50 #rayon du blop
    rayon_fruit = 10 #rayon du fruit
    rayon_mechant = 15

    def position_fruit():
        return (randint(rayon_fruit,taille_fen-rayon_fruit),randint(rayon_fruit,taille_fen-rayon_fruit)) #générateur de position aléatoire
    
    #initialisation des positions des fruits    
    pos_fruit1 = position_fruit()
    pos_fruit4 = position_fruit()
    pos_fruit3 = position_fruit()
    pos_fruit2 = position_fruit()
    
    pos_mechant = position_fruit()
    
    done = False
    while not done:
        clock.tick(150)
        
        screen.fill((0,0,0)) #fond noir
        
        #quadrillage
        x1 = 0 
        y1 = 0 
        x2 = taille_fen
        y2 = 0
        for i in range(taille_fen//40):
            y1 = 40*i
            y2 = 40*i
            pg.draw.line(screen, blanc, (x1, y1), (x2, y2))
    
        x1 = 0 
        y1 = 0 
        x2 = 0 
        y2 = taille_fen
        for i in range(taille_fen//40):
            x1 = 40*i
            x2 = 40*i        
            pg.draw.line(screen, blanc, (x1, y1), (x2, y2)) #fin quadrillage
        
        #le blop suit la souris 
        direction = pg.math.Vector2.normalize(pg.math.Vector2(pg.mouse.get_pos()[0]-position[0],pg.mouse.get_pos()[1]-position[1]))
        pg.draw.circle(screen, rouge, np.add(position,direction), rayon)
        position = np.add(position,direction)

        #manger des fruits et apparition
        pg.draw.circle(screen,vert,pos_fruit4,rayon_fruit)
        pg.draw.circle(screen,violet,pos_fruit3,rayon_fruit)
        pg.draw.circle(screen,rose,pos_fruit2,rayon_fruit)
        pg.draw.circle(screen,bleu,pos_fruit1,rayon_fruit)
        
        #déplacements du méchant
        direction_mechant = pg.math.Vector2.normalize(pg.math.Vector2(position[0]-pos_mechant[0],position[1]-pos_mechant[1]))
        pg.draw.circle(screen, orange, np.add(pos_mechant, direction_mechant), rayon_mechant)
        pos_mechant = np.add(pos_mechant,direction_mechant/2)

        #manger les fruits 
        if np.sqrt((position[0] - pos_fruit1[0])**2 + (position[1] - pos_fruit1[1])**2) <= (rayon-rayon_fruit):
            pos_fruit1 = position_fruit()
            rayon+=2
        
        if np.sqrt((position[0] - pos_fruit2[0])**2 + (position[1] - pos_fruit2[1])**2) <= (rayon-rayon_fruit):
            pos_fruit2 = position_fruit()
            rayon+=2
        
        if np.sqrt((position[0] - pos_fruit3[0])**2 + (position[1] - pos_fruit3[1])**2) <= (rayon-rayon_fruit):
            pos_fruit3 = position_fruit()
            rayon+=2
        
        if np.sqrt((position[0] - pos_fruit4[0])**2 + (position[1] - pos_fruit4[1])**2) <= (rayon-rayon_fruit):
            pos_fruit4 = position_fruit()
            rayon+=2

        #si le méchant touche le blop et que le blop n'est pas trop gros la taille du blop est divisée par 2
        if rayon <= 4*rayon_mechant and np.sqrt((position[0] - pos_mechant[0])**2 + (position[1] - pos_mechant[1])**2) <= (rayon):
            rayon = rayon//2

        #si la taille est 4 fois ou plus supérieure à celle du méchant, on peut le manger et le méchant réapparait plus gros
        if rayon > 4*rayon_mechant and np.sqrt((position[0] - pos_mechant[0])**2 + (position[1] - pos_mechant[1])**2) <= (rayon):
            rayon += 2
            pos_mechant = position_fruit()
            rayon_mechant += 5

        #si le rayon est trop petit le jeu s'arrête
        if rayon <= 5 :
            done = True

        #la taille du blop est indiquée par le nom de la fenetre 
        pg.display.set_caption(f'taille blop = {rayon}')
        
        
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

