import pygame #type: ignore
from pygame import *
from loto import loto

pygame.init()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

fenetre = pygame.display.set_mode((900, 900))

fond = image.load('sino.jpg')
fond = fond.convert()
fond = pygame.transform.scale(fond, fenetre.get_size())

font = pygame.font.Font(None, 36)

button_menu = pygame.Rect(300,250,200,80)
button_jeu1 = pygame.Rect(300,250,200,80)

etat = "menu_principal"


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if etat == "menu_principal":
                if button_menu.collidepoint(event.pos):
                    etat = "menu_jeux"
            elif etat == "menu_jeux":
                if button_jeu1.collidepoint(event.pos):
                    etat = "Loto"
    fenetre.blit(fond, (0,0))
    if etat == "menu_principal":
        pygame.draw.rect(fenetre, BLUE, button_menu)
        text = font.render("Jeux disponibles", True, WHITE)
        fenetre.blit(text,(button_menu.x+30,button_menu.y+25))
    elif etat == "menu_jeux":
        pygame.draw.rect(fenetre, BLUE, button_jeu1)
        text = font.render("Lancer Jeu 1", True, WHITE)
        fenetre.blit(text,(button_jeu1.x+40,button_jeu1.y+25))
    elif etat == "Loto":
        loto()

    display.flip()  

pygame.quit()