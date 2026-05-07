import pygame
import random #type: ignore
from loto import loto as loto_run
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
DARK = (30, 30, 30)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
GREY = (180, 180, 180)

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
button_create = pygame.Rect(10, 180, 200, 60)
button_connect = pygame.Rect(10, 100, 200, 60)
button_menu = pygame.Rect(300, 250, 300, 80)
button_loto = pygame.Rect(300, 80, 300, 80)
button_blackjack = pygame.Rect(300, 200, 300, 80)
button_chifoumi = pygame.Rect(300, 320, 300, 80)
button_roulette = pygame.Rect(300, 440, 300, 80)
button_bp = pygame.Rect(300, 560, 300, 80)
button_bm = pygame.Rect(300, 680, 300, 80)
button_de = pygame.Rect(300, 800, 300, 80)
button_argent = pygame.Rect(60, 130, 200, 80)
input_argent = pygame.Rect(60, 230, 200, 40)
input_pseudo = pygame.Rect(200, 200, 500, 40)
input_mdp = pygame.Rect(200, 260, 500, 40)
input_nom = pygame.Rect(200, 320, 500, 40)
input_prenom = pygame.Rect(200, 380, 500, 40)
button_valider_connect = pygame.Rect(200, 330, 220, 50)
button_valider_create = pygame.Rect(200, 450, 220, 50)

# variables
etat = "menu_principal"
champ_actif = None
pseudo = ""
mot_de_passe = ""
nom = ""
prenom = ""
argent = ""
argent_compte = 0
running = True
popup_ouvert = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if etat == "menu_principal":
                if button_menu.collidepoint(event.pos):
                    etat = "menu_jeux"
                elif button_connect.collidepoint(event.pos):
                    etat = "connexion"
                elif button_create.collidepoint(event.pos):
                    etat = "creation"

            elif etat == "menu_jeux":
                
                if popup_ouvert:

        # Fond transparent sombre
                    overlay = pygame.Surface((800, 600))
                    overlay.set_alpha(180)
                    overlay.fill((0, 0, 0))
                    fenetre.blit(overlay, (0, 0))

        # Fenêtre popup
                    popup_rect = pygame.Rect(200, 150, 400, 250)

                    pygame.draw.rect(fenetre, GREY, popup_rect)
                    pygame.draw.rect(fenetre, WHITE, popup_rect, 3)

        # Texte popup
                    title = font.render("ARGENT", True, WHITE)
                    fenetre.blit(title, (350, 180))

                    msg = font.render("Combien d'argent voulez vous ajouté à votre compte ?", True, WHITE)
                    fenetre.blit(msg, (320, 260))

                    close = font.render("Echap pour fermer", True, RED)
                    fenetre.blit(close, (270, 340))
                    
                elif button_argent.collidepoint(event.pos):
                    champ_actif = "argent"
                    popup_ouvert = True
                elif input_argent.collidepoint(event.pos):
                    champ_actif = "argent"
                elif button_loto.collidepoint(event.pos):
                    loto_run(fenetre)
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
                

            elif etat == "connexion":
                if input_pseudo.collidepoint(event.pos):
                    champ_actif = "pseudo"
                elif input_mdp.collidepoint(event.pos):
                    champ_actif = "mdp"
                elif button_valider_connect.collidepoint(event.pos):
                    pass            

            elif etat == "creation":
                if input_nom.collidepoint(event.pos):
                    champ_actif = "nom"
                elif input_prenom.collidepoint(event.pos):
                    champ_actif = "prenom"
                elif input_pseudo.collidepoint(event.pos):
                    champ_actif = "pseudo"
                elif input_mdp.collidepoint(event.pos):
                    champ_actif = "mdp"
                elif button_valider_create.collidepoint(event.pos):
                    pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                etat = "menu_principal"
            elif champ_actif:
                if event.key == pygame.K_BACKSPACE:
                    if champ_actif == "pseudo":
                        pseudo = pseudo[:-1]
                    elif champ_actif == "mdp":
                        mot_de_passe = mot_de_passe[:-1]
                    elif champ_actif == "nom":
                        nom = nom[:-1]
                    elif champ_actif == "prenom":
                        prenom = prenom[:-1]
                    elif champ_actif == "argent":
                        argent = argent[:-1]
                elif event.unicode:
                    if champ_actif == "pseudo":
                        pseudo += event.unicode
                    elif champ_actif == "mdp":
                        mot_de_passe += event.unicode
                    elif champ_actif == "nom":
                        nom += event.unicode
                    elif champ_actif == "prenom":
                        prenom += event.unicode
                    elif champ_actif == "argent":
                        if event.unicode.isdigit():
                            argent += event.unicode
                            # variable reliée à la future base de donnée
                            argent_compte = int(argent)

    fenetre.blit(fond, (0, 0))

    if etat == "menu_principal":
        pygame.draw.rect(fenetre, BLUE, button_menu)
        pygame.draw.rect(fenetre, DARK, button_connect)
        pygame.draw.rect(fenetre, DARK, button_create)
        fenetre.blit(font.render("Se connecter", True, WHITE), (button_connect.x + 20, button_connect.y + 15))
        fenetre.blit(font.render("Créer un compte", True, WHITE), (button_create.x + 5, button_create.y + 15))
        fenetre.blit(font.render("Accéder aux jeux", True, WHITE), (button_menu.x + 50, button_menu.y + 25))

    elif etat == "connexion":
        pygame.draw.rect(fenetre, WHITE, input_pseudo)
        pygame.draw.rect(fenetre, WHITE, input_mdp)
        fenetre.blit(font.render("Pseudo :", True, BLUE), (200, 170))
        fenetre.blit(font.render("Mot de passe :", True, BLUE), (200, 230))
        fenetre.blit(font.render(pseudo, True, BLUE), (210, 205))
        fenetre.blit(font.render("*" * len(mot_de_passe), True, BLUE), (210, 265))
        pygame.draw.rect(fenetre, RED, button_valider_connect)
        fenetre.blit(font.render("Se connecter", True, WHITE), (button_valider_connect.x + 20, button_valider_connect.y + 12))

    elif etat == "creation":
        pygame.draw.rect(fenetre, WHITE, input_nom)
        pygame.draw.rect(fenetre, WHITE, input_prenom)
        pygame.draw.rect(fenetre, WHITE, input_pseudo)
        pygame.draw.rect(fenetre, WHITE, input_mdp)
        fenetre.blit(font.render("Nom :", True, BLUE), (200, 290))
        fenetre.blit(font.render("Prénom :", True, BLUE), (200, 350))
        fenetre.blit(font.render("Pseudo :", True, BLUE), (200, 170))
        fenetre.blit(font.render("Mot de passe :", True, BLUE), (200, 230))
        fenetre.blit(font.render(nom, True, BLUE), (210, 325))
        fenetre.blit(font.render(prenom, True, BLUE), (210, 385))
        fenetre.blit(font.render(pseudo, True, BLUE), (210, 205))
        fenetre.blit(font.render("*" * len(mot_de_passe), True, GREY), (210, 265))
        pygame.draw.rect(fenetre, DARK, button_valider_create)
        fenetre.blit(font.render("Créer", True, WHITE), (button_valider_create.x + 70, button_valider_create.y + 12))

    elif etat == "menu_jeux":
        pygame.draw.rect(fenetre, BLUE, button_loto)
        pygame.draw.rect(fenetre, BLUE, button_blackjack)
        pygame.draw.rect(fenetre, BLUE, button_chifoumi)
        pygame.draw.rect(fenetre, BLUE, button_roulette)
        pygame.draw.rect(fenetre, BLUE, button_bp)
        pygame.draw.rect(fenetre, BLUE, button_bm)
        pygame.draw.rect(fenetre, BLUE, button_de)
        pygame.draw.rect(fenetre, RED, button_argent)
        fenetre.blit(font.render(argent, True, BLUE), (input_argent.x + 10, input_argent.y + 5))
        fenetre.blit(font.render("Loto", True, WHITE), (button_loto.x + 80, button_loto.y + 25))
        fenetre.blit(font.render("Blackjack Lite", True, WHITE), (button_blackjack.x + 55, button_blackjack.y + 25))
        fenetre.blit(font.render("Chifoumi", True, WHITE), (button_chifoumi.x + 80, button_chifoumi.y + 25))
        fenetre.blit(font.render("Roulette", True, WHITE), (button_roulette.x + 80, button_roulette.y + 25))
        fenetre.blit(font.render("Bataille Politique", True, WHITE), (button_bp.x + 30, button_bp.y + 25))
        fenetre.blit(font.render("Bandit Manchot", True, WHITE), (button_bm.x + 45, button_bm.y + 25))
        fenetre.blit(font.render("Simulateur de dé", True, WHITE), (button_de.x + 35, button_de.y + 25))
        fenetre.blit(font.render("Argent", True, WHITE), (button_argent.x + 40, button_argent.y + 25))

    pygame.display.flip()

pygame.quit()