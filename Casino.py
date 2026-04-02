import pygame
import random #type: ignore
from loto import loto_update  
from pfc import chifoumi as chifoumi_run
from blackjack import blackjack as blackjack_run
from roulette import roulette as roulette_run
from bandit_manchot import machine_sous as machine_sous_run
from simulateur_de_dé import sim_de as sim_de_run
from Expulsion_Election import bataillepolitique as bataillepolitique_run
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
button_menu = pygame.Rect(300, 250, 300, 80)
button_loto = pygame.Rect(300, 80, 300, 80)
button_blackjack = pygame.Rect(300, 200, 300, 80)
button_chifoumi = pygame.Rect(300, 320, 300, 80)
button_roulette = pygame.Rect(300, 440, 300, 80)
button_bp = pygame.Rect(300, 560, 300, 80)
button_bm = pygame.Rect(300, 680, 300, 80)
button_de = pygame.Rect(300, 800, 300, 80)

boutons = []
for i in range(49):
    x = 50 + (i % 7) * 100
    y = 50 + (i // 7) * 80
    boutons.append((pygame.Rect(x, y, 60, 50), i+1))

loto_data = {
    "boutons": boutons,
    "numeros": [],
    "complementaire": None,
    "resultat": None
}

etat = "menu_principal"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if etat == "menu_principal":
                if button_menu.collidepoint(event.pos):
                    etat = "menu_jeux"
            elif etat == "menu_jeux":
                if button_loto.collidepoint(event.pos):
                    etat = "loto"
                elif button_chifoumi.collidepoint(event.pos):
                    chifoumi_run(fenetre)
                elif button_blackjack.collidepoint(event.pos):
                    blackjack_run(fenetre)
                elif button_roulette.collidepoint(event.pos):
                    roulette_run(fenetre)
                elif button_bp.collidepoint(event.pos):
                   bataillepolitique_run(fenetre) 
                elif button_bm.collidepoint(event.pos):
                    machine_sous_run(fenetre)
                elif button_de.collidepoint(event.pos):
                    sim_de_run(fenetre)
            elif etat == "loto":
                loto_update(fenetre, event, loto_data)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                etat = "menu_principal"
    fenetre.blit(fond, (0, 0))
    if etat == "menu_principal":
        pygame.draw.rect(fenetre, BLUE, button_menu)
        text = font.render("Accéder aux jeux", True, WHITE)
        fenetre.blit(text, (button_menu.x + 40, button_menu.y + 25))
    
    elif etat == "menu_jeux":
        pygame.draw.rect(fenetre, BLUE, button_loto)
        pygame.draw.rect(fenetre, BLUE, button_blackjack)
        pygame.draw.rect(fenetre, BLUE, button_chifoumi)
        pygame.draw.rect(fenetre, BLUE, button_roulette)
        pygame.draw.rect(fenetre, BLUE, button_bp)
        pygame.draw.rect(fenetre, BLUE, button_bm)
        pygame.draw.rect(fenetre, BLUE, button_de)
        fenetre.blit(font.render("Loto", True, WHITE), (button_loto.x + 110, button_loto.y + 25))
        fenetre.blit(font.render("Blackjack", True, WHITE), (button_blackjack.x + 80, button_blackjack.y + 25))
        fenetre.blit(font.render("Chifoumi", True, WHITE), (button_chifoumi.x + 80, button_chifoumi.y + 25))
        fenetre.blit(font.render("Roulette", True, WHITE), (button_roulette.x + 80, button_roulette.y + 25))
        fenetre.blit(font.render("Bataille Politique", True, WHITE), (button_bp.x + 80, button_bp.y + 25))
        fenetre.blit(font.render("Bandit Manchot", True, WHITE), (button_bm.x + 80, button_bm.y + 25))
        fenetre.blit(font.render("Simulateur de dé", True, WHITE), (button_de.x + 80, button_de.y + 25))

    elif etat == "loto":
        loto_update(fenetre, None, loto_data)
    pygame.display.flip()

pygame.quit()