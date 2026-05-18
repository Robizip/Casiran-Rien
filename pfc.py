import pygame
import random


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
GREY = (180, 180, 180)
DARK = (30, 30, 30)
YELLOW = (255, 215, 0)

def chifoumi(ecran):
    font = pygame.font.Font(None, 48)
    font_small = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()

    # ── saisie de la mise ─────────────────────────────────────────────────
    texte_saisi = ""
    erreur = ""
    argent2 = None

    while argent2 is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_BACKSPACE:
                    texte_saisi = texte_saisi[:-1]
                elif event.key == pygame.K_RETURN:
                    try:
                        val = int(texte_saisi)
                        if val <= 0:
                            erreur = "Entrez un nombre positif."
                        else:
                            argent2 = val
                    except ValueError:
                        erreur = "Entrez un nombre valide."
                elif event.unicode.isdigit():
                    texte_saisi += event.unicode

        ecran.fill(DARK)
        titre = font.render("Chifoumi", True, WHITE)
        ecran.blit(titre, (ecran.get_width() // 2 - titre.get_width() // 2, 100))

        label = font_small.render("Combien misez-vous ?", True, GREY)
        ecran.blit(label, (ecran.get_width() // 2 - label.get_width() // 2, 250))

        pygame.draw.rect(ecran, WHITE, (300, 300, 300, 45), 2)
        surf = font_small.render(texte_saisi, True, WHITE)
        ecran.blit(surf, (310, 310))

        if erreur:
            e = font_small.render(erreur, True, RED)
            ecran.blit(e, (ecran.get_width() // 2 - e.get_width() // 2, 360))

        hint = font_small.render("Échap pour revenir", True, GREY)
        ecran.blit(hint, (40, ecran.get_height() - 40))

        pygame.display.flip()
        clock.tick(60)

    pierre = "pierre"
    ciseaux = "ciseaux"
    feuille = "feuille"
    jeu = [pierre, feuille, ciseaux]
    victoire_joueur = 0
    victoire_ordi = 0
    font = pygame.font.Font(None, 50)
    boutons = {
        "pierre": pygame.Rect(100, 700, 200, 80),
        "feuille": pygame.Rect(350, 700, 200, 80),
        "ciseaux": pygame.Rect(600, 700, 200, 80)
    }
    message = ""
    running = True
    while victoire_joueur < 3 and victoire_ordi < 3 and running:
        ecran.fill((0,0,0))
        # affichage scores (remplace print)
        txt = font.render(f"Toi: {victoire_joueur} | Ordi: {victoire_ordi}", True, (255,255,255))
        ecran.blit(txt, (250, 50))
        res = font.render(message, True, (255,255,0))
        ecran.blit(res, (300, 200))
        # boutons
        for choix, rect in boutons.items():
            pygame.draw.rect(ecran, (0,0,255), rect)
            t = font.render(choix, True, (255,255,255))
            ecran.blit(t, (rect.x + 20, rect.y + 20))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                for choix, rect in boutons.items():
                    if rect.collidepoint(event.pos):
                        ordi = random.choice(jeu)
                        if choix == ordi:
                            message = "Egalite"
                        elif (choix == "pierre" and ordi == "ciseaux") \
                        or (choix == "ciseaux" and ordi == "feuille") \
                        or (choix == "feuille" and ordi == "pierre"):
                            victoire_joueur += 1
                            message = f"Vous avez gagné un point ({victoire_joueur})"
                        else:
                            victoire_ordi += 1
                            message = f"L'ordi a gagné un point ({victoire_ordi})"
    # fin du jeu (logique conservée)
    ecran.fill((0,0,0))
    if victoire_joueur == 3:
        msg = f"Vous avez gagné {argent2 * 3}, veuillez réessayer en remisant votre argent !"
    else:
        msg = f"Vous avez perdu votre mise de {argent2}, ne vous laissez pas humilier par une IA"

    font = pygame.font.Font(None, 30)
    txt = font.render(msg, True, (255,255,255))
    ecran.blit(txt, (50, 400))
    pygame.display.flip()

    pygame.time.wait(5000)