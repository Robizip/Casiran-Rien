import pygame
import random

WHITE = (255, 255, 255)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
GREY = (180, 180, 180)
DARK = (30, 30, 30)
YELLOW = (255, 215, 0) 


def machine_sous(fenetre):
    font = pygame.font.Font(None, 38)
    font_big = pygame.font.Font(None, 90)
    font_small = pygame.font.Font(None, 28)
    clock = pygame.time.Clock()
    W, H = fenetre.get_size()
    symboles = [":)", "Ø", ":(", "•", "€", "$", "#", "&", "<>", "7"]
    tirage = None
    message = ""
    couleur_msg = WHITE
    button_jouer = pygame.Rect(W // 2 - 100, H - 150, 200, 55)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_SPACE:
                    tirage = [random.choice(symboles) for _ in range(3)]
                    unique = list(set(tirage))
                    if len(unique) == 1:
                        if unique[0] == "7":
                            message = " JACKPOT !!! "
                            couleur_msg = YELLOW
                        else:
                            message = f"Bravo, 3 {unique[0]} identiques !"
                            couleur_msg = GREEN
                    elif len(unique) == 2:
                        message = "Deux symboles identiques, pas mauvais !"
                        couleur_msg = WHITE
                    else:
                        message = "Perdu, réessaie !"
                        couleur_msg = RED
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_jouer.collidepoint(event.pos):
                    tirage = [random.choice(symboles) for _ in range(3)]
                    unique = list(set(tirage))
                    if len(unique) == 1:
                        if unique[0] == "7":
                            message = " JACKPOT !!! "
                            couleur_msg = GREEN
                        else:
                            message = f"Bravo, 3 ({unique[0]})  identiques ! vous gagnez 500€"
                            couleur_msg = GREEN
                    elif len(unique) == 2:
                        message = "Deux symboles identiques, pas mauvais ! Vous gagnez 25€"
                        couleur_msg = WHITE
                    else:
                        message = "Perdu, réessaie !"
                        couleur_msg = RED
        fenetre.fill(DARK)
        titre = font.render("Bandit Manchot", True, WHITE)
        fenetre.blit(titre, (W // 2 - titre.get_width() // 2, 60))
        # rouleaux
        pygame.draw.rect(fenetre, (50, 50, 70), (W // 2 - 220, 180, 440, 130), border_radius=12)
        if tirage:
            for i, s in enumerate(tirage):
                sym = font_big.render(s, True, WHITE)
                fenetre.blit(sym, (W // 2 - 160 + i * 140, 195))
        else:
            points = font_big.render("? | ? | ?", True, GREY)
            fenetre.blit(points, (W // 2 - points.get_width() // 2, 195))
        # résultat
        if message:
            msg_surf = font.render(message, True, couleur_msg)
            fenetre.blit(msg_surf, (W // 2 - msg_surf.get_width() // 2, 370))
        # bouton
        pygame.draw.rect(fenetre, (80, 80, 180), button_jouer, border_radius=8)
        fenetre.blit(font.render("JOUER", True, WHITE), (button_jouer.x + 48, button_jouer.y + 12))
        hint = font_small.render("Clic ou Espace pour jouer  |  Échap pour revenir", True, GREY)
        fenetre.blit(hint, (W // 2 - hint.get_width() // 2, H - 45))
        pygame.display.flip()
        clock.tick(60)