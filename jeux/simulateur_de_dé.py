import pygame
import random
from données import GestionBD as Gestion


WHITE = (255, 255, 255)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
GREY = (180, 180, 180)
DARK = (30, 30, 30)
YELLOW = (255, 215, 0)
BLUE = (60, 60, 200)


def sim_de(fenetre, compte):
    font = pygame.font.Font(None, 38)
    font_small = pygame.font.Font(None, 28)
    clock = pygame.time.Clock()
    W, H = fenetre.get_size()

    # Saisie de la mise
    texte_saisi = ""
    erreur = ""
    argent_compte = Gestion.RecupArgent(compte)
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
                    if compte != "":
                        if int(texte_saisi) > argent_compte:
                            erreur = "Erreur. Vous n’avez pas assez d’argent sur votre compte"
                        else:
                            argent2 = int(texte_saisi)
                    else:
                        erreur = "Erreur. Vous n’êtes pas connecté."

                elif event.unicode.isdigit():
                    texte_saisi += event.unicode

        fenetre.fill(DARK)
        titre = font.render("Simulateur de Dé", True, WHITE)
        fenetre.blit(titre, (W // 2 - titre.get_width() // 2, 100))

        label = font_small.render("Combien misez-vous ?", True, GREY)
        fenetre.blit(label, (W // 2 - label.get_width() // 2, 250))

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

    # Score des manches
    manche_joueurs = 0
    manche_ordi = 0

    # Fonction saisie
    def saisie_nombre(label):
        texte = ""
        erreur = ""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return None
                    elif event.key == pygame.K_BACKSPACE:
                        texte = texte[:-1]
                    elif event.key == pygame.K_RETURN:
                        try:
                            val = int(texte)
                            if val <= 0:
                                erreur = "Entrez un nombre positif."
                            else:
                                return val
                        except ValueError:
                            erreur = "Entrez un nombre valide."
                    elif event.unicode.isdigit():
                        texte += event.unicode

            fenetre.fill(DARK)
            titre = font.render("Simulation de Dés", True, WHITE)
            fenetre.blit(titre, (W // 2 - titre.get_width() // 2, 80))

            score = font_small.render(
                f"Score — Vous : {manche_joueurs}    Ordi : {manche_ordi}",
                True,
                YELLOW
            )
            fenetre.blit(score, (W // 2 - score.get_width() // 2, 150))
            lbl = font.render(label, True, GREY)
            fenetre.blit(lbl, (W // 2 - lbl.get_width() // 2, 260))
            pygame.draw.rect(fenetre, WHITE, (W // 2 - 150, 310, 300, 45), 2)
            fenetre.blit(font.render(texte, True, WHITE), (W // 2 - 140, 320))
            if erreur:
                fenetre.blit(font_small.render(erreur, True, RED), (W // 2 - 150, 370))

            fenetre.blit(
                font_small.render("Échap pour revenir", True, GREY),
                (40, H - 45)
            )

            pygame.display.flip()
            clock.tick(60)

    # Boucle des manches
    while manche_joueurs < 3 and manche_ordi < 3:
        lancers = saisie_nombre("Combien de dés lancés ?")
        if lancers is None:
            return
        face = saisie_nombre("Combien de faces par dé ?")
        if face is None:
            return

        # Tirage dynamique
        liste_joueurs = []
        liste_ordi = []
        lignes = []

        timer = 0
        index_de = 0
        animation = True

        while animation:
            dt = clock.tick(60)
            timer += dt

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            # Nouveau lancer
            if timer > 150:
                timer = 0
                if index_de < lancers:
                    de = random.randint(1, face)
                    ordi = random.randint(1, face)
                    liste_joueurs.append(de)
                    liste_ordi.append(ordi)
                    lignes.append(
                        (f"Dé {index_de + 1} — Vous : {de}    Ordi : {ordi}",WHITE))
                    index_de += 1

                else:
                    somme_joueurs = sum(liste_joueurs)
                    somme_ordi = sum(liste_ordi)
                    lignes.append((f"Total — Vous : {somme_joueurs}    Ordi : {somme_ordi}",YELLOW))
                    if somme_joueurs > somme_ordi:
                        manche_joueurs += 1
                        lignes.append(("Vous gagnez cette manche !", GREEN))
                    elif somme_ordi > somme_joueurs:
                        manche_ordi += 1
                        lignes.append(("L'ordi gagne cette manche !", RED))
                    else:
                        lignes.append(("Égalité ! Pas de point.", GREY))
                    lignes.append((f"Score — Vous : {manche_joueurs}  |  Ordi : {manche_ordi}",YELLOW))

                    animation = False

            # Affichage dynamique
            fenetre.fill(DARK)

            titre = font.render("Lancer des dés...", True, WHITE)
            fenetre.blit(titre, (W // 2 - titre.get_width() // 2, 40))
            
            marge_haut = 100
            marge_bas = 55
            ligne_h = 28
            y_depart = marge_haut
            hauteur_utilisable = fenetre.get_height() - marge_haut - marge_bas
            visible = hauteur_utilisable // ligne_h
            y = y_depart
            for msg, col in lignes[-visible:]:
                fenetre.blit(font_small.render(msg, True, col), (60, y))
                y += ligne_h

            pygame.display.flip()

        # Pause après animation
        attente = True
        while attente:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        attente = False

            fenetre.fill(DARK)
            titre = font.render("Résultat de la manche", True, WHITE)
            fenetre.blit(titre, (W // 2 - titre.get_width() // 2, 40))
            
            y = y_depart
            for msg, col in lignes[-visible:]:
                fenetre.blit(font_small.render(msg, True, col), (60, y))
                y += ligne_h

            hint = font_small.render("Entrée / Espace pour continuer",True,GREY)

            fenetre.blit(hint,(W // 2 - hint.get_width() // 2, H - 50))

            pygame.display.flip()
            clock.tick(60)

    # Fin de partie
    if manche_joueurs == 3:
        msg_fin = (f"BRAVO ! Vous avez gagné la partie ! Vous remportez {argent2 * 2}€")
        col_fin = GREEN
        Gestion.AjoutArgent(argent2 * 2, compte)

    else:
        msg_fin = (f"L'ordi a gagné la partie... Vous perdez votre mise de {argent2}€")
        col_fin = RED
        Gestion.AjoutArgent(-argent2, compte)

    attente_fin = True
    while attente_fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    attente_fin = False

        fenetre.fill(DARK)
        surf = font.render(msg_fin, True, col_fin)

        fenetre.blit(surf,(W // 2 - surf.get_width() // 2, H // 2 - 45))

        score_fin = font_small.render(f"Score final : Vous : {manche_joueurs}    Ordi : {manche_ordi}",True,YELLOW)

        fenetre.blit(score_fin,(W // 2 - score_fin.get_width() // 2, H // 2 + 20))
        hint = font_small.render("Entrée ou Échap pour revenir",True,GREY)
        fenetre.blit(hint,(W // 2 - hint.get_width() // 2, H - 45))

        pygame.display.flip()
        clock.tick(60)