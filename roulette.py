import pygame
import random

WHITE = (255, 255, 255)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
GREY = (180, 180, 180)
DARK = (30, 30, 30)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 215, 0)


def roulette(fenetre):
    font = pygame.font.Font(None, 38)
    font_small = pygame.font.Font(None, 28)
    clock = pygame.time.Clock()
    W, H = fenetre.get_size()
    # ── saisie de la mise totale ───────────────────────────────────────────
    texte_saisi = ""
    erreur = ""
    argent = None
    while argent is None:
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
                            argent = val
                    except ValueError:
                        erreur = "Entrez un nombre valide."
                elif event.unicode.isdigit():
                    texte_saisi += event.unicode
        fenetre.fill(DARK)
        titre = font.render("Roulette", True, WHITE)
        fenetre.blit(titre, (W // 2 - titre.get_width() // 2, 100))
        label = font_small.render("Combien avez-vous en poche ?", True, GREY)
        fenetre.blit(label, (W // 2 - label.get_width() // 2, 220))
        pygame.draw.rect(fenetre, WHITE, (W // 2 - 150, 270, 300, 45), 2)
        fenetre.blit(font_small.render(texte_saisi, True, WHITE), (W // 2 - 140, 280))
        if erreur:
            fenetre.blit(font_small.render(erreur, True, RED), (W // 2 - 150, 330))
        fenetre.blit(font_small.render("Échap pour revenir", True, GREY), (40, H - 40))
        pygame.display.flip()
        clock.tick(60)
    # ── boucle principale du jeu ───────────────────────────────────────────
    while True:
        startmoney = argent
        bet = []
        # ── phase de mise ─────────────────────────────────────────────────
        choix_cat = ""       # "red" / "black" / numéro str
        choix_montant = ""
        erreur = ""
        etape = "categorie"  # "categorie" -> "montant" -> "encore"
        encore = ""
        phase_mise = True
        while phase_mise:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        if etape == "categorie":
                            choix_cat = choix_cat[:-1]
                        elif etape == "montant":
                            choix_montant = choix_montant[:-1]
                        elif etape == "encore":
                            encore = encore[:-1]
                    elif event.key == pygame.K_RETURN:
                        if etape == "categorie":
                            c = choix_cat.strip().lower()
                            if c in ("red", "black"):
                                bet.append(c)
                                etape = "montant"
                                erreur = ""
                            elif c.isdigit() and 0 <= int(c) <= 37:
                                bet.append(int(c))
                                etape = "montant"
                                erreur = ""
                            else:
                                erreur = "Entrez un nombre (0-37) ou 'red'/'black'."
                        elif etape == "montant":
                            try:
                                bb = int(choix_montant)
                                if bb <= 0 or bb > argent:
                                    erreur = "Mise invalide ou supérieure à votre solde."
                                else:
                                    argent -= bb
                                    bet.append(bb)
                                    choix_montant = ""
                                    erreur = ""
                                    if argent == 0:
                                        phase_mise = False
                                    else:
                                        etape = "encore"
                            except ValueError:
                                erreur = "Entrez un nombre valide."
                        elif etape == "encore":
                            e = encore.strip().lower()
                            if e == "yes":
                                choix_cat = ""
                                encore = ""
                                etape = "categorie"
                            elif e == "no":
                                phase_mise = False
                            else:
                                erreur = "Tapez 'yes' ou 'no'."
                    else:
                        if etape == "categorie":
                            choix_cat += event.unicode
                        elif etape == "montant":
                            if event.unicode.isdigit():
                                choix_montant += event.unicode
                        elif etape == "encore":
                            encore += event.unicode
            fenetre.fill(DARK)
            fenetre.blit(font.render("Roulette", True, WHITE), (W // 2 - 80, 30))
            fenetre.blit(font_small.render(f"Solde : {argent}$", True, YELLOW), (40, 30))
            # mises en cours
            fenetre.blit(font_small.render("Mises placées :", True, GREY), (40, 90))
            for i in range(0, len(bet), 2):
                ligne = f"  {bet[i]}  →  {bet[i+1]}$"
                fenetre.blit(font_small.render(ligne, True, WHITE), (40, 115 + (i // 2) * 28))
            # champ actif
            if etape == "categorie":
                label = "Pariez sur un numéro (0-37) ou une couleur (red/black) :"
                valeur = choix_cat
            elif etape == "montant":
                label = f"Combien misez-vous ? (max {argent}$)"
                valeur = choix_montant
            else:
                label = "Encore une mise ? (yes/no)"
                valeur = encore
            fenetre.blit(font_small.render(label, True, GREY), (40, 420))
            pygame.draw.rect(fenetre, WHITE, (40, 460, 400, 40), 2)
            fenetre.blit(font_small.render(valeur, True, WHITE), (50, 470))
            if erreur:
                fenetre.blit(font_small.render(erreur, True, RED), (40, 515))
            fenetre.blit(font_small.render("Échap pour revenir", True, GREY), (40, H - 40))
            pygame.display.flip()
            clock.tick(60)
        # ── tirage ────────────────────────────────────────────────────────
        number = random.randint(0, 37)
        if number == 0:
            color = "green"
        elif number in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
            color = "red"
        else:
            color = "black"
        resultats = [f"La bille tombe sur : {number} ({color})"]
        for z in range(0, len(bet), 2):
            if bet[z] == number:
                gain = bet[z+1] * 36
                argent += gain
                resultats.append(f"Gagné ! Numéro {bet[z]} — {bet[z+1]}$ → {gain}$")
            elif str(bet[z]) == color:
                gain = bet[z+1] * 2
                argent += gain
                resultats.append(f"Gagné ! Couleur {color} — {bet[z+1]}$ → {gain}$")
            else:
                resultats.append(f"Perdu sur {bet[z]}.")
        resultats.append(f"Solde : {startmoney}$ → {argent}$")
        # ── affichage résultat ─────────────────────────────────────────────
        rejouer = ""
        erreur = ""
        etape_fin = "rejouer" if argent > 0 else "fini"
        affichage_fin = True
        while affichage_fin:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        rejouer = rejouer[:-1]
                    elif event.key == pygame.K_RETURN:
                        if etape_fin == "fini":
                            return
                        r = rejouer.strip().lower()
                        if r == "yes":
                            affichage_fin = False  # relance la boucle principale
                        elif r == "no":
                            return
                        else:
                            erreur = "Tapez 'yes' ou 'no'."
                    else:
                        rejouer += event.unicode
            fenetre.fill(DARK)
            fenetre.blit(font.render("Résultat", True, WHITE), (W // 2 - 70, 30))
            couleur_num = GREEN if color == "green" else RED if color == "red" else (50, 50, 50)
            num_surf = font.render(str(number), True, WHITE)
            pygame.draw.circle(fenetre, couleur_num, (W // 2, 120), 50)
            fenetre.blit(num_surf, (W // 2 - num_surf.get_width() // 2, 100))
            for i, msg in enumerate(resultats):
                c = GREEN if "Gagné" in msg else RED if "Perdu" in msg else WHITE
                fenetre.blit(font_small.render(msg, True, c), (40, 200 + i * 32))
            if etape_fin == "fini":
                fenetre.blit(font_small.render("Plus d'argent. Appuyez sur Entrée pour quitter.", True, RED), (40, H - 80))
            else:
                fenetre.blit(font_small.render("Rejouer ? (yes/no)", True, GREY), (40, H - 110))
                pygame.draw.rect(fenetre, WHITE, (40, H - 75, 200, 38), 2)
                fenetre.blit(font_small.render(rejouer, True, WHITE), (50, H - 68))
                if erreur:
                    fenetre.blit(font_small.render(erreur, True, RED), (40, H - 30))
            pygame.display.flip()
            clock.tick(60)
import time
argent = int(input("argent totale"))