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

nombre_rouge = {
    1, 3, 5, 7, 9, 12, 14, 16, 18,
    19, 21, 23, 25, 27, 30, 32, 34, 36
}


def roulette(fenetre):
    pygame.font.init()
    font = pygame.font.Font(None, 38)
    font_small = pygame.font.Font(None, 28)
    clock = pygame.time.Clock()
    W, H = fenetre.get_size()

    # ── saisie argent de départ ───────────────────────────────────────────
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

    # ── boucle principale ─────────────────────────────────────────────────
    while True:
        startmoney = argent
        bets = []
        cat_temp = None
        choix_cat = ""
        choix_montant = ""
        encore = ""
        erreur = ""
        etape = "categorie"
        phase_mise = True

        # ── phase de mise ─────────────────────────────────────────────────
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
                        # ── catégorie ──
                        if etape == "categorie":
                            c = choix_cat.strip().lower()
                            if c in ("rouge", "noir", "vert"):
                                cat_temp = c
                                etape = "montant"
                                erreur = ""
                            elif c.isdigit() and 0 <= int(c) <= 36:
                                cat_temp = int(c)
                                etape = "montant"
                                erreur = ""
                            else:
                                erreur = "Entrez un numéro (0-36) ou rouge/noir/vert."
                        # ── montant ──
                        elif etape == "montant":
                            try:
                                montant = int(choix_montant)
                                if montant <= 0:
                                    erreur = "Mise invalide."
                                elif montant > argent:
                                    erreur = "Mise supérieure à votre solde."
                                else:
                                    argent -= montant
                                    bets.append(cat_temp)
                                    bets.append(montant)
                                    choix_montant = ""
                                    choix_cat = ""
                                    cat_temp = None
                                    erreur = ""
                                    if argent == 0:
                                        phase_mise = False
                                    else:
                                        etape = "encore"
                            except ValueError:
                                erreur = "Entrez un nombre valide."
                        # ── encore ──
                        elif etape == "encore":
                            e = encore.strip().lower()
                            if e == "oui":
                                encore = ""
                                etape = "categorie"
                                erreur = ""
                            elif e == "non":
                                phase_mise = False
                            else:
                                erreur = "Tapez oui ou non."
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
            fenetre.blit(font_small.render("Mises placées :", True, GREY), (40, 90))
            for i in range(0, len(bets), 2):
                ligne = f"{bets[i]}  →  {bets[i + 1]}$"
                fenetre.blit(font_small.render(ligne, True, WHITE), (40, 120 + (i // 2) * 28))

            if etape == "categorie":
                label = "Numéro (0-36) ou couleur (rouge/noir/vert) :"
                valeur = choix_cat
            elif etape == "montant":
                label = f"Combien misez-vous ? (max {argent}$)"
                valeur = choix_montant
            else:
                label = "Encore une mise ? (oui/non)"
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
        number = random.randint(0, 36)
        if number == 0:
            color = "vert"
        elif number in nombre_rouge:
            color = "rouge"
        else:
            color = "noir"

        resultats = [f"La bille tombe sur : {number} ({color})"]
        for i in range(0, len(bets), 2):
            pari = bets[i]
            montant = bets[i + 1]
            if isinstance(pari, int) and pari == number:
                gain = montant * 36
                argent += gain
                resultats.append(f"Gagné ! Numéro de {pari} à {gain}$")
            elif isinstance(pari, str) and pari == color:
                gain = montant * 2
                argent += gain
                resultats.append(f"Gagné ! Couleur de {color} à {gain}$")
            else:
                resultats.append(f"Perdu sur {pari}.")
        resultats.append(f"Solde : de {startmoney}$ à {argent}$")

        # ── écran résultat ────────────────────────────────────────────────
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
                        if r == "oui":
                            affichage_fin = False
                        elif r == "non":
                            return
                        else:
                            erreur = "Tapez oui ou non."
                    else:
                        rejouer += event.unicode

            fenetre.fill(DARK)
            fenetre.blit(font.render("Résultat", True, WHITE), (W // 2 - 70, 30))

            couleur_cercle = GREEN if color == "green" else RED if color == "red" else (50, 50, 50)
            pygame.draw.circle(fenetre, couleur_cercle, (W // 2, 120), 50)
            num_surf = font.render(str(number), True, WHITE)
            fenetre.blit(num_surf, (W // 2 - num_surf.get_width() // 2, 100))

            for i, msg in enumerate(resultats):
                c = GREEN if "Gagné" in msg else RED if "Perdu" in msg else WHITE
                fenetre.blit(font_small.render(msg, True, c), (40, 200 + i * 32))

            if etape_fin == "fini":
                fenetre.blit(font_small.render("Plus d'argent. Entrée pour quitter.", True, RED), (40, H - 80))
            else:
                fenetre.blit(font_small.render("Rejouer ? (oui/non)", True, GREY), (40, H - 110))
                pygame.draw.rect(fenetre, WHITE, (40, H - 75, 200, 38), 2)
                fenetre.blit(font_small.render(rejouer, True, WHITE), (50, H - 68))
                if erreur:
                    fenetre.blit(font_small.render(erreur, True, RED), (40, H - 30))

            pygame.display.flip()
            clock.tick(60)