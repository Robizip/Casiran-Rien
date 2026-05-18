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


def blackjack(fenetre):
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

        fenetre.fill(DARK)
        titre = font.render("Blackjack Lite", True, WHITE)
        fenetre.blit(titre, (fenetre.get_width() // 2 - titre.get_width() // 2, 100))

        label = font_small.render("Combien misez-vous ?", True, GREY)
        fenetre.blit(label, (fenetre.get_width() // 2 - label.get_width() // 2, 250))

        pygame.draw.rect(fenetre, WHITE, (300, 300, 300, 45), 2)
        surf = font_small.render(texte_saisi, True, WHITE)
        fenetre.blit(surf, (310, 310))

        if erreur:
            e = font_small.render(erreur, True, RED)
            fenetre.blit(e, (fenetre.get_width() // 2 - e.get_width() // 2, 360))

        hint = font_small.render("Échap pour revenir", True, GREY)
        fenetre.blit(hint, (40, fenetre.get_height() - 40))

        pygame.display.flip()
        clock.tick(60)

    # ── jeu ───────────────────────────────────────────────────────────────
    def nouveau_jeu():
        carte = [
            1,2,3,4,5,6,7,8,9,10,10,10,10,
            1,2,3,4,5,6,7,8,9,10,10,10,10,
            1,2,3,4,5,6,7,8,9,10,10,10,10,
            1,2,3,4,5,6,7,8,9,10,10,10,10,
        ]
        nb = random.randint(0, 51)
        premiere = carte[nb]
        carte.pop(nb)
        return carte, premiere

    carte, premiere = nouveau_jeu()
    hit = premiere
    x = 1
    lost = 0
    win = 0
    messages = [f"Mise : {argent2}€", f"Première carte : {premiere}  —  Total : {hit}"]
    partie_finie = False
    resultat_final = None

    button_tire = pygame.Rect(200, 700, 180, 55)
    button_reste = pygame.Rect(520, 700, 180, 55)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and not partie_finie:
                if button_tire.collidepoint(event.pos):
                    nb = random.randint(1, 51 - x)
                    cartejouer = carte[nb]
                    carte.pop(nb)
                    x += 1
                    hit += cartejouer
                    messages.append(f"Vous tirez : {cartejouer}  —  Total : {hit}")
                    if hit > 20:
                        partie_finie = True

                elif button_reste.collidepoint(event.pos):
                    nb = random.randint(1, 51 - x)
                    cartejouer = carte[nb]
                    carte.pop(nb)
                    hit += cartejouer
                    messages.append(f"Vous restez. Dernière carte : {cartejouer}  —  Total : {hit}")
                    if hit < 22:
                        lost = 1
                    elif hit > 21:
                        win = 1
                    partie_finie = True

            elif event.type == pygame.MOUSEBUTTONDOWN and partie_finie:
                # clic n'importe où pour revenir
                return

        # calcul du résultat
        if partie_finie and resultat_final is None:
            if hit == 21:
                resultat_final = ("Blackjack ! Jackpot !", YELLOW, argent2 * 3)
            elif hit < 21 and lost != 1 or win == 1:
                resultat_final = ("Vous gagnez !", GREEN, argent2 * 2)
            elif hit > 21 or lost == 1:
                resultat_final = ("Dommage, vous perdez tout...", RED, 0)

        fenetre.fill(DARK)

        # messages
        for i, msg in enumerate(messages):
            s = font_small.render(msg, True, WHITE)
            fenetre.blit(s, (60, 60 + i * 38))

        if resultat_final:
            texte, couleur, gain = resultat_final
            r = font.render(texte, True, couleur)
            fenetre.blit(r, (fenetre.get_width() // 2 - r.get_width() // 2, 500))
            g = font_small.render(f"Argent final : {gain}€", True, couleur)
            fenetre.blit(g, (fenetre.get_width() // 2 - g.get_width() // 2, 570))
            hint = font_small.render("Cliquez pour revenir au menu", True, GREY)
            fenetre.blit(hint, (fenetre.get_width() // 2 - hint.get_width() // 2, 630))
        else:
            pygame.draw.rect(fenetre, BLUE, button_tire)
            fenetre.blit(font_small.render("Tirer", True, WHITE), (button_tire.x + 50, button_tire.y + 15))
            pygame.draw.rect(fenetre, BLUE, button_reste)
            fenetre.blit(font_small.render("Rester", True, WHITE), (button_reste.x + 45, button_reste.y + 15))

        hint2 = font_small.render("Échap pour revenir", True, GREY)
        fenetre.blit(hint2, (40, fenetre.get_height() - 45))

        pygame.display.flip()
        clock.tick(60)