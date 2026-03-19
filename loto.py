import pygame
import random

def loto_update(fenetre, event, data):
    font = pygame.font.Font(None, 30)

    boutons = data["boutons"]
    numeros = data["numeros"]
    complementaire = data["complementaire"]
    resultat = data["resultat"]

    # clic souris
    if event and event.type == pygame.MOUSEBUTTONDOWN:
        for rect, num in boutons:
            if rect.collidepoint(event.pos):
                if len(numeros) < 5 and num not in numeros:
                    numeros.append(num)
                elif len(numeros) == 5:
                    data["complementaire"] = num

    # touche espace
    if event and event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            if len(numeros) == 5 and complementaire:
                gagnants = random.sample(range(1,50),5)
                comp = random.randint(1,10)
                bons = set(numeros) & set(gagnants)
                data["resultat"] = (gagnants, comp, bons)

    # affichage
    fenetre.fill((0,0,0))

    for rect, num in boutons:
        pygame.draw.rect(fenetre, (100,100,100), rect)
        txt = font.render(str(num), True, (255,255,255))
        fenetre.blit(txt, (rect.x+10, rect.y+10))

    txt = font.render(f"{numeros} + {complementaire}", True, (255,255,255))
    fenetre.blit(txt, (50, 650))

    if resultat:
        gagnants, comp, bons = resultat
        t1 = font.render(f"Gagnants: {gagnants} + {comp}", True, (255,255,255))
        fenetre.blit(t1, (50,700))

        t2 = font.render(f"Bons: {list(bons)}", True, (255,255,255))
        fenetre.blit(t2, (50,750))