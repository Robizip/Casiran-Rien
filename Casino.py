import pygame
import random #type: ignore
from loto import loto_update  
# from blackjack import menu, blackjack
# from bandit_manchot import machine_sous
# from Expulsion_Election import bataillepolitique
# from pfc import chifoumi
# from roulette import *
# from simulateur_de_dé import sim_de
# from Texas_Holdem import *
pygame.init()

# couleurs
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# fenêtre
fenetre = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Menu Jeux")

# fond
fond = pygame.image.load('sino.jpg')
fond = fond.convert()
fond = pygame.transform.scale(fond, fenetre.get_size())

# font
font = pygame.font.Font(None, 36)

# boutons menu
button_menu = pygame.Rect(300, 250, 200, 80)
button_jeu1 = pygame.Rect(300, 250, 200, 80)

# préparation des boutons loto (1 à 49)
boutons = []
for i in range(49):
    x = 50 + (i % 7) * 100
    y = 50 + (i // 7) * 80
    boutons.append((pygame.Rect(x, y, 60, 50), i+1))

# données du loto
loto_data = {
    "boutons": boutons,
    "numeros": [],
    "complementaire": None,
    "resultat": None
}

# état du programme
etat = "menu_principal"

running = True
while running:
    # boucle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # menu interactions
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if etat == "menu_principal":
                if button_menu.collidepoint(event.pos):
                    etat = "menu_jeux"
            elif etat == "menu_jeux":
                if button_jeu1.collidepoint(event.pos):
                    etat = "Loto"

        # retour menu avec ESC
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                etat = "menu_principal"

        # interactions loto
        if etat == "Loto":
            loto_update(fenetre, event, loto_data)

    # affichage fond
    fenetre.blit(fond, (0, 0))

    # menu principal
    if etat == "menu_principal":
        pygame.draw.rect(fenetre, BLUE, button_menu)
        text = font.render("Jeux disponibles", True, WHITE)
        fenetre.blit(text, (button_menu.x + 30, button_menu.y + 25))

    # menu jeux
    elif etat == "menu_jeux":
        pygame.draw.rect(fenetre, BLUE, button_jeu1)
        text = font.render("Lancer Jeu 1", True, WHITE)
        fenetre.blit(text, (button_jeu1.x + 40, button_jeu1.y + 25))

    # loto
    elif etat == "Loto":
        loto_update(fenetre, None, loto_data)  # affichage continu

    # actualiser
    pygame.display.flip()

pygame.quit()