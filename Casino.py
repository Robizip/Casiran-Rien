import pygame
import données.GestionBD as Gestion
from jeux.loto import loto as loto_run
from jeux.chifoumi import chifoumi as chifoumi_run
from jeux.blackjack import blackjack as blackjack_run
from jeux.roulette import roulette as roulette_run
from jeux.bandit_manchot import machine_sous as machine_sous_run
from jeux.simulateur_de_dé import sim_de as sim_de_run
from jeux.Expulsion_Election import bataillepolitique as bataillepolitique_run

pygame.init()

# couleurs
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLUE2 = (0, 0, 215)
BLUE3 = (37,131,175)
DARK = (30, 30, 30)
RED = (200, 50, 50)
RED2 = (150, 0, 0)
GREEN = (50, 200, 50)
GREY = (180, 180, 180)
GREY2 = (120, 120, 120)

# fenêtre
fenetre = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Menu Jeux")

# fond
fond = pygame.image.load('images/sino.jpg')
fond = fond.convert()
fond = pygame.transform.scale(fond, fenetre.get_size())

# font
font = pygame.font.Font(None, 36)

# compte
compte_connecte = ""

# argent
argent_compte = 0

# boutons
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
button_valider_argent = pygame.Rect(350, 330, 200, 45)
input_argent_popup = pygame.Rect(350, 270, 200, 40)
input_pseudo = pygame.Rect(200, 140, 500, 40)
input_mdp = pygame.Rect(200, 220, 500, 40)
input_nom = pygame.Rect(200, 300, 500, 40)
input_prenom = pygame.Rect(200, 380, 500, 40)
button_valider_connect = pygame.Rect(200, 290, 220, 50)
button_valider_create = pygame.Rect(200, 450, 220, 50)
coin_compte = pygame.Rect(620,0,500,80)

# variables
etat = "menu_principal"
champ_actif = None
pseudo_creation = ""
mot_de_passe_creation = ""
message_creation = ""
pseudo_connexion = ""
mot_de_passe_connexion = ""
message_connexion = ""
nom = ""
prenom = ""
argent = ""
running = True
popup_ouvert = False
curseur_visible = True
timer_curseur = 0
reajustement = 0

# Boucle principale 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # si on clique avec la souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            if etat == "menu_principal":
                if button_menu.collidepoint(event.pos):
                    etat = "menu_jeux"
                elif button_connect.collidepoint(event.pos):
                    etat = "connexion"
                elif button_create.collidepoint(event.pos):
                    etat = "creation"

            elif etat == "menu_jeux":
                if popup_ouvert: # Interactions dans le popup "ajouter de l'argent"
                    if input_argent_popup.collidepoint(event.pos):
                        champ_actif = "argent"
                    elif button_valider_argent.collidepoint(event.pos):
                        if compte_connecte and argent.isdigit():
                            montant = int(argent)
                            # Argent en base
                            Gestion.AjoutArgent(argent,compte_connecte)
                            
                            # Mise à jour de l'affichage du solde
                        argent_compte = Gestion.RecupArgent(compte_connecte)
                    argent = ""
                    popup_ouvert = False
                    champ_actif = None
                else:
                    # Boutons du menu des jeux
                    if button_argent.collidepoint(event.pos):
                        popup_ouvert = True
                        champ_actif = "argent"
                    elif button_loto.collidepoint(event.pos):
                        loto_run(fenetre,compte_connecte)
                    elif button_chifoumi.collidepoint(event.pos):
                        chifoumi_run(fenetre,compte_connecte)
                    elif button_blackjack.collidepoint(event.pos):
                        blackjack_run(fenetre,compte_connecte)
                    elif button_roulette.collidepoint(event.pos):
                        roulette_run(fenetre,compte_connecte)
                    elif button_bp.collidepoint(event.pos):
                        bataillepolitique_run(fenetre,compte_connecte)
                    elif button_bm.collidepoint(event.pos):
                        machine_sous_run(fenetre,compte_connecte)
                    elif button_de.collidepoint(event.pos):
                        sim_de_run(fenetre,compte_connecte)
                    
                    # Update?
                    argent_compte = Gestion.RecupArgent(compte_connecte)

            elif etat == "connexion":
                if input_pseudo.collidepoint(event.pos):
                    champ_actif = "pseudo_connexion"
                elif input_mdp.collidepoint(event.pos):
                    champ_actif = "mdp_connexion"
                elif button_valider_connect.collidepoint(event.pos):
                    # Vérification du pseudo et mot de passe
                    verif = Gestion.ConnexionCompte(pseudo_connexion, mot_de_passe_connexion)
                    if verif : # Si la connexion réussit
                        message_connexion = "Vous êtes connecté :D Appuyez sur Échap."
                        compte_connecte = pseudo_connexion
                        argent_compte = Gestion.RecupArgent(compte_connecte)
                    else:
                        message_connexion = "Pseudo ou mot de passe incorrect."
                        compte_connecte = ""
                    pseudo_connexion = ""
                    mot_de_passe_connexion = ""

            elif etat == "creation":
                if input_nom.collidepoint(event.pos):
                    champ_actif = "nom"
                elif input_prenom.collidepoint(event.pos):
                    champ_actif = "prenom"
                elif input_pseudo.collidepoint(event.pos):
                    champ_actif = "pseudo_creation"
                elif input_mdp.collidepoint(event.pos):
                    champ_actif = "mdp_creation"
                elif button_valider_create.collidepoint(event.pos):
                    # Bout de code gérant la création d’un compte.
                    verification_unicité = Gestion.VerificationCompte(pseudo_creation)
                    if verification_unicité : # pseudo déjà utilisé
                        message_creation = "Erreur, le pseudo est déjà pris. Réessayez."
                        reajustement = 0
                    else :
                        if all([pseudo_creation, mot_de_passe_creation, nom, prenom]):
                            Gestion.CreationCompte(pseudo_creation, mot_de_passe_creation, nom, prenom)
                            message_creation = "Votre compte a été créé. Appuyez sur Échap et connectez-vous."
                            reajustement = -100
                        else :
                            message_creation = "Au moins un champ n’a pas été rempli. Véfifiez."
                            reajustement = 0
        # Si on utilise le clavier
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if popup_ouvert:
                    popup_ouvert = False
                    champ_actif = None
                else:
                    etat = "menu_principal"
            elif champ_actif: # Partie du code pour gérer les zones de textes dans Pygames.
                if event.key == pygame.K_BACKSPACE:
                    if champ_actif == "pseudo_creation":
                        pseudo_creation = pseudo_creation[:-1]
                    elif champ_actif == "pseudo_connexion":
                        pseudo_connexion = pseudo_connexion[:-1]
                    elif champ_actif == "mdp_creation":
                        mot_de_passe_creation = mot_de_passe_creation[:-1]
                    elif champ_actif == "mdp_connexion":
                        mot_de_passe_connexion = mot_de_passe_connexion[:-1]
                    elif champ_actif == "nom":
                        nom = nom[:-1]
                    elif champ_actif == "prenom":
                        prenom = prenom[:-1]
                    elif champ_actif == "argent":
                        argent = argent[:-1]
                        argent_compte = int(argent) if argent else 0
                # Insertion des caractères 
                elif event.unicode:
                    if champ_actif == "pseudo_creation":
                        pseudo_creation += event.unicode
                    elif champ_actif == "pseudo_connexion":
                        pseudo_connexion += event.unicode
                    elif champ_actif == "mdp_creation":
                        mot_de_passe_creation += event.unicode
                    elif champ_actif == "mdp_connexion":
                        mot_de_passe_connexion += event.unicode
                    elif champ_actif == "nom":
                        if event.unicode.isalpha():
                            nom += event.unicode
                    elif champ_actif == "prenom":
                        if event.unicode.isalpha():
                            prenom += event.unicode
                    elif champ_actif == "argent":
                        if event.unicode.isdigit():
                            argent += event.unicode

    # Affichage
    fenetre.blit(fond, (0, 0))

    if etat == "menu_principal":
        pygame.draw.rect(fenetre, WHITE, button_menu)
        pygame.draw.rect(fenetre, DARK, button_connect)
        pygame.draw.rect(fenetre, DARK, button_create)
        texte_connexion = font.render("Se connecter", True, WHITE)
        texte_creation = font.render("Créer un compte", True, WHITE)
        fenetre.blit(texte_connexion, texte_connexion.get_rect(center=button_connect.center))
        fenetre.blit(texte_creation, texte_creation.get_rect(center=button_create.center))
        texte = font.render("Accéder aux jeux", True, DARK)
        fenetre.blit(texte, texte.get_rect(center=button_menu.center))
        # Code du coin pour afficher le nom du compte et l’argent.
        pygame.draw.rect(fenetre,GREY2, coin_compte)
        fenetre.blit(font.render(f"Compte : {compte_connecte}",True,WHITE), (coin_compte.x + 10, coin_compte.y + 5))
        fenetre.blit(font.render(f"Argent : {argent_compte} €",True,WHITE), (coin_compte.x + 10, coin_compte.y + 45))

    elif etat == "connexion":
        pygame.draw.rect(fenetre, WHITE, input_pseudo)
        pygame.draw.rect(fenetre, WHITE, input_mdp)
        fenetre.blit(font.render("Pseudo :", True, BLUE2), (200, 115))
        fenetre.blit(font.render("Mot de passe :", True, BLUE2), (200, 190))
        # Affichage du champ pseudo avec curseur clignotant
        texte = pseudo_connexion
        if champ_actif == "pseudo_connexion" and curseur_visible:
            texte += "|"
        # Mot de passe masqué
        fenetre.blit(font.render(texte, True, DARK), (210, 145))
        texte = "*" * len(mot_de_passe_connexion)

        if champ_actif == "mdp_connexion" and curseur_visible:
            texte += "|"
        fenetre.blit(font.render(texte, True, DARK), (210, 225))
        pygame.draw.rect(fenetre, DARK, button_valider_connect)
        texte_connexion = font.render("Se connecter", True, WHITE)
        fenetre.blit(texte_connexion, texte_connexion.get_rect(center=button_valider_connect.center))

        pygame.draw.rect(fenetre,GREY2, coin_compte)
        fenetre.blit(font.render(f"Compte : {compte_connecte}",True,WHITE), (coin_compte.x + 10, coin_compte.y + 5))
        fenetre.blit(font.render(f"Argent : {argent_compte} €",True,WHITE), (coin_compte.x + 10, coin_compte.y + 45))
        
        if message_connexion != "":
            texte_message_connexion = font.render(message_connexion, True, WHITE)
            fenetre.blit(texte_message_connexion, (button_valider_connect.x, button_valider_connect.y + 70))

    elif etat == "creation":
        pygame.draw.rect(fenetre, WHITE, input_nom)
        pygame.draw.rect(fenetre, WHITE, input_prenom)
        pygame.draw.rect(fenetre, WHITE, input_pseudo)
        pygame.draw.rect(fenetre, WHITE, input_mdp)
        fenetre.blit(font.render("Nom :", True, BLUE2), (200, 270))
        fenetre.blit(font.render("Prénom :", True, BLUE2), (200, 350))
        fenetre.blit(font.render("Pseudo :", True, BLUE2), (200, 115))
        fenetre.blit(font.render("Mot de passe :", True, BLUE2), (200, 190))
        texte = nom
        if champ_actif == "nom" and curseur_visible:
            texte += "|"
        fenetre.blit(font.render(texte, True, DARK), (210, 305))
        texte = prenom
        if champ_actif == "prenom" and curseur_visible:
            texte += "|"
        fenetre.blit(font.render(texte, True, DARK), (210, 385))
        texte = pseudo_creation
        if champ_actif == "pseudo_creation" and curseur_visible:
            texte += "|"
        fenetre.blit(font.render(texte, True, DARK), (210, 145))
        # Mot de passe masqué
        texte = "*" * len(mot_de_passe_creation)
        if champ_actif == "mdp_creation" and curseur_visible:
            texte += "|"
        fenetre.blit(font.render(texte, True, DARK), (210, 225))
        pygame.draw.rect(fenetre, DARK, button_valider_create)
        fenetre.blit(font.render("Créer", True, WHITE), (button_valider_create.x + 70, button_valider_create.y + 12))

        pygame.draw.rect(fenetre,GREY2, coin_compte)
        fenetre.blit(font.render(f"Compte : {compte_connecte}",True,WHITE), (coin_compte.x + 10, coin_compte.y + 5))
        fenetre.blit(font.render(f"Argent : {argent_compte} €",True,WHITE), (coin_compte.x + 10, coin_compte.y + 45))

        if message_creation != "" :
            texte_message_creation = font.render(message_creation, True, WHITE)
            fenetre.blit(texte_message_creation,(button_valider_create.x + reajustement,button_valider_create.y + 70))


    elif etat == "menu_jeux":
        # Boutons des jeux
        pygame.draw.rect(fenetre, BLUE3, button_loto)
        pygame.draw.rect(fenetre, BLUE3, button_blackjack)
        pygame.draw.rect(fenetre, BLUE3, button_chifoumi)
        pygame.draw.rect(fenetre, BLUE3, button_roulette)
        pygame.draw.rect(fenetre, BLUE3, button_bp)
        pygame.draw.rect(fenetre, BLUE3, button_bm)
        pygame.draw.rect(fenetre, BLUE3, button_de)
        pygame.draw.rect(fenetre, RED2, button_argent)
        texte = font.render("Loto", True, WHITE)
        fenetre.blit(texte, texte.get_rect(center=button_loto.center))
        texte = font.render("Blackjack Lite", True, WHITE)
        fenetre.blit(texte, texte.get_rect(center=button_blackjack.center))
        texte = font.render("Chifoumi", True, WHITE)
        fenetre.blit(texte, texte.get_rect(center=button_chifoumi.center))
        texte = font.render("Roulette", True, WHITE)
        fenetre.blit(texte, texte.get_rect(center=button_roulette.center))
        texte = font.render("Bataille Politique", True, WHITE)
        fenetre.blit(texte, texte.get_rect(center=button_bp.center))
        texte = font.render("Bandit Manchot", True, WHITE)
        fenetre.blit(texte, texte.get_rect(center=button_bm.center))
        texte = font.render("Simulateur de dé", True, WHITE)
        fenetre.blit(texte, texte.get_rect(center=button_de.center))
        texte = font.render("Argent", True, WHITE)
        fenetre.blit(texte, texte.get_rect(center=button_argent.center))

        pygame.draw.rect(fenetre,GREY2, coin_compte)
        fenetre.blit(font.render(f"Compte : {compte_connecte}",True,WHITE), (coin_compte.x + 10, coin_compte.y + 5))
        fenetre.blit(font.render(f"Argent : {argent_compte} €",True,WHITE), (coin_compte.x + 10, coin_compte.y + 45))

        if popup_ouvert: 
            # Bouton pour rentrer de l'argent
            overlay = pygame.Surface((900, 900), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            fenetre.blit(overlay, (0, 0))
            popup_rect = pygame.Rect(200, 200, 500, 250)
            pygame.draw.rect(fenetre, DARK, popup_rect)
            pygame.draw.rect(fenetre, WHITE, popup_rect, 3)
            fenetre.blit(font.render("Ajouter de l'argent", True, WHITE), (270, 220))
            fenetre.blit(font.render("Montant :", True, GREY), (220, 275))
            pygame.draw.rect(fenetre, WHITE, input_argent_popup)
            texte = argent
            if champ_actif == "argent" and curseur_visible:
                texte += "|"
            fenetre.blit(font.render(texte, True, DARK), (input_argent_popup.x + 10, input_argent_popup.y + 5))
            pygame.draw.rect(fenetre, GREEN, button_valider_argent)
            fenetre.blit(font.render("Valider", True, WHITE), (button_valider_argent.x + 55, button_valider_argent.y + 10))
            fenetre.blit(font.render("Échap pour fermer", True, RED), (270, 390))
    # Clignotement du curseur
    timer_curseur += 1
    if timer_curseur >= 30:
        curseur_visible = not curseur_visible
        timer_curseur = 0

    pygame.display.flip()

pygame.quit()