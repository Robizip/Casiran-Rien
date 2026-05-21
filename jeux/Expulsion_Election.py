import pygame
import random
from données import GestionBD as Gestion

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
YELLOW = (255, 255, 0)
GREY = (180, 180, 180)
DARK = (30, 30, 30)

def bataillepolitique(fenetre,compte):
    font = pygame.font.Font(None, 48)
    font_small = pygame.font.Font(None, 32)
    font_verysmall = pygame.font.Font(None,25)
    clock = pygame.time.Clock()
     # Saisie de la mise
    texte_saisi = ""
    erreur = ""
    argent2 = None

    argent_compte = Gestion.RecupArgent(compte)

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
                        if compte != "" :
                            if int(texte_saisi) > argent_compte :
                                erreur = "Erreur. Vous n’avez pas assez d’argent sur votre compte"
                            else :
                                argent2 = int(texte_saisi)
                        else :
                            erreur = "Erreur. Vous n’êtes pas connecté."
                elif event.unicode.isdigit():
                    texte_saisi += event.unicode

        fenetre.fill(DARK)
        titre = font.render("Bataille politique", True, WHITE)
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


    listecombattant = [
        "Zemmour", "Macron", "Melenchon", "Bardella",
        "MarineLepen", "JeanMarieLepen", "NicolaSarkozy", "FrançoisHollande",
    ]

    # Phase 1 : Choix du personnage
    texte_saisi = ""
    erreur = ""

    saisie_en_cours = True
    while saisie_en_cours:
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
                    match = next((c for c in listecombattant if c.lower() == texte_saisi.lower()), None)
                    if match:
                        choix = match
                        saisie_en_cours = False
                    else:
                        erreur = "Nom introuvable, vérifiez l'orthographe."
                else:
                    texte_saisi += event.unicode

        fenetre.fill(DARK)

        # titre
        titre = font.render("Bataille Politique — Choisissez votre combattant", True, WHITE)
        fenetre.blit(titre, (fenetre.get_width() // 2 - titre.get_width() // 2, 40))

        # liste des combattants
        label = font_small.render("Combattants disponibles :", True, GREY)
        fenetre.blit(label, (80, 100))
        for i, nom in enumerate(listecombattant):
            t = font_small.render(f"• {nom}", True, WHITE)
            fenetre.blit(t, (80 + (i // 4) * 400, 130 + (i % 4) * 35))

        # champ de saisie
        pygame.draw.rect(fenetre, WHITE, (200, 360, 500, 45), 2)
        saisi_surface = font_small.render(texte_saisi, True, WHITE)
        fenetre.blit(saisi_surface, (210, 370))

        label2 = font_small.render("Entrez un nom puis appuyez sur Entrée :", True, GREY)
        fenetre.blit(label2, (200, 330))

        if erreur:
            err_surf = font_small.render(erreur, True, RED)
            fenetre.blit(err_surf, (200, 415))

        echap = font_small.render("Échap pour revenir au menu", True, GREY)
        fenetre.blit(echap, (40, fenetre.get_height() - 45))

        pygame.display.flip()
        clock.tick(60)

    # Phase 2 : COMBAT DYNAMIQUE
    possiblemort = [
        "meurt en glissant sur une flaque",
        "meurt en prétant allégence à Irsraël",
        "a bu trop de boisson splashbot",
        "se prend un coup du crâne à lylian",
        "s'est fait 3 couronnes",
        "quitte ce monde cruel",
        "se perd sur 4chan",
        "se fait harceler par Amin Saadi",
        "s'endort paisiblement",
        "se prend le coin de la table",
        "a trop pratiqué l'ABR",
        "se fait compresser en .zip",
        "commence sa carrière de modérateur discord",
        "s'est fait cancel",
        "a été retrouvé sur les fichiers Epstein",
        "meurt",
        "pleure sur la musique de TiboInshape",
        "s'étouffe avec un bouzelouf",
        "se prend un contrôle de Juan Jose Trivess Segura",
        "se perd dans sa récursivité",
        "se fait juger par Charles",
        "finit dans la voiture de Nordahl Lelandais",
        "finit sous la terrasse de Xavier Dupont de Ligonnès",
        "finit fan de Hazbin hotel",
        "défend les lolis sur Reddit",
        "se reconvertit en influenceur OnlyFacts",
        "intègre la plèbe",
        "rate le cours de NSI",
        "part danser avec King Nasir",
        "s'est fait Charlie Kirk",
        "doit aller prendre sa douche",
        "se fait appeler par sa maman",
        "rentre chez eux en pleurant",
        "a de la diarhée dans les chaussettes",
        "se fait rachetté par Elon Musk",
        "s'est pris une JFK",
        "a détourné un peu d'argent",
        "esquive ses impots à Malte",
        "se fait caillasser par Mazza",
        "part en soirée avec le petit Grégory",
        "se fait manger par une pastabox poulet de la cafet",
        "meurt d'une overdose de crème au chocolat",
        "est passé sur l'axe Y",
    ]

    combattant = {
        p: [random.randint(10, 20), random.randint(1, 5), random.randint(0, 6)]
        for p in listecombattant
    }

    dead = []
    messages = [f"Vous avez choisi {choix} !"]
    tours = 0
    timer = 0
    combat_fini = False

    running = True

    while running:
        dt = clock.tick(60)
        timer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # Système tour par tour
        if not combat_fini and timer > 1200:
            timer = 0
            tours += 1
            messages.append("")
            messages.append(f"--- Tour {tours} ---")

            random.shuffle(listecombattant)

            for z in listecombattant:
                if z in dead:
                    continue

                possible = [c for c in listecombattant if c != z and c not in dead]
                if not possible:
                    continue

                cible = random.choice(possible)

                if random.randint(0, 10) <= combattant[cible][2]:
                    messages.append(f"{z} attaque {cible} mais {cible} esquive.")
                else:
                    combattant[cible][0] -= combattant[z][1]

                    if combattant[cible][0] <= 0:
                        dead.append(cible)
                        messages.append(f"{z} attaque {cible} et {cible} {random.choice(possiblemort)}.")
                    else:
                        messages.append(f"{z} attaque {cible} — {combattant[z][1]} dégâts, il reste {combattant[cible][0]} PV.")


            if len(dead) >= len(listecombattant) - 1:
                combat_fini = True
                gagnant = next((c for c in listecombattant if c not in dead), None)

                messages.append("")
                messages.append("----- FIN DU COMBAT -----")

                if gagnant:
                    messages.append(f"Vainqueur : {gagnant}")

                    if gagnant == choix:
                        messages.append(f"Vous avez parié sur le bon cheval ! Vous gagnez {argent2 * 8} €")
                        Gestion.AjoutArgent(argent2*8,compte)
                    else:
                        messages.append(f"Vous perdez votre mise de {argent2} €")
                        Gestion.AjoutArgent(-argent2,compte)

        # Affichage
        fenetre.fill(DARK)

        marge = 75
        hauteur_utilisable = fenetre.get_height() - marge
        ligne_h = 28
        visible = hauteur_utilisable // ligne_h
        y = 20

        for msg in messages[-visible:]: # Magie dynamique
            if "et" in msg :
                fenetre.blit(font_verysmall.render(msg, True, RED), (40, y))
            elif "esquive" in msg :
                fenetre.blit(font_verysmall.render(msg, True, GREY), (40, y))
            elif "Vainqueur" in msg :
                fenetre.blit(font_verysmall.render(msg, True, YELLOW), (40, y))
            else :
                fenetre.blit(font_verysmall.render(msg, True, WHITE), (40, y))
            y += ligne_h

        if not combat_fini:
            txt = "Combat en cours..."
        else:
            txt = "Combat terminé (ESC pour quitter)"

        fenetre.blit(font_small.render(txt, True, GREY), (40, fenetre.get_height() - 50))

        pygame.display.flip()