import pygame
import random

def chifoumi(ecran):
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
                            message = f"Tu as gagné un point ({victoire_joueur})"

                        else:
                            victoire_ordi += 1
                            message = f"Tu as perdu ({victoire_ordi})"

    # fin du jeu (logique conservée)
    ecran.fill((0,0,0))
    if victoire_joueur == 3:
        msg = "T'as gagné"
    else:
        msg = "T'as perdu"

    txt = font.render(msg, True, (255,255,255))
    ecran.blit(txt, (350, 400))
    pygame.display.flip()

    pygame.time.wait(2000)