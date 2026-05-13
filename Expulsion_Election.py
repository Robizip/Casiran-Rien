import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
GREY = (180, 180, 180)
DARK = (30, 30, 30)

def bataillepolitique(fenetre):
    font = pygame.font.Font(None, 32)
    font_small = pygame.font.Font(None, 26)
    clock = pygame.time.Clock()

    listecombattans = [
        "Zemmour", "Macron", "Melenchon", "Bardella",
        "MarineLepen", "JeanMarieLepen", "NicolaSarkozy", "FrançoisHollande",
    ]

    # ── Phase 1 : saisie du choix ──────────────────────────────────────────
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
                    match = next((c for c in listecombattans if c.lower() == texte_saisi.lower()), None)
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
        for i, nom in enumerate(listecombattans):
            t = font_small.render(f"• {nom}", True, WHITE)
            fenetre.blit(t, (80 + (i // 4) * 400, 130 + (i % 4) * 35))

        # champ de saisie
        pygame.draw.rect(fenetre, WHITE, (200, 360, 500, 45), 2)
        saisi_surface = font.render(texte_saisi, True, WHITE)
        fenetre.blit(saisi_surface, (210, 370))

        label2 = font_small.render("Entrez un nom puis appuyez sur Entrée :", True, GREY)
        fenetre.blit(label2, (200, 330))

        if erreur:
            err_surf = font_small.render(erreur, True, RED)
            fenetre.blit(err_surf, (200, 415))

        echap = font_small.render("Échap pour revenir au menu", True, GREY)
        fenetre.blit(echap, (80, fenetre.get_height() - 40))

        pygame.display.flip()
        clock.tick(60)

    # ── Phase 2 : combat ───────────────────────────────────────────────────
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
        "se fait juger par Charle",
        "finit dans la voiture de Nordahl Lelandais",
        "finit sous la terrasse de Xavier Dupont de Ligonnès",
        "fini fan de Hazbin hotel",
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
    ]

    combattans = {}
    for personne in listecombattans:
        combattans[personne] = [random.randint(10, 20), random.randint(1, 5), random.randint(0, 6), 0]

    dead = []
    messages = [f"Vous avez choisi {choix} ! Que le combat commence !"]
    tours = 0
    scroll_offset = 0

    # génération de tous les messages du combat d'un coup
    while len(dead) < 8:
        messages.append("")
        messages.append(f"Tour {tours}")
        random.shuffle(listecombattans)

        for z in listecombattans:
            if z not in dead:
                combattanspossible = [c for c in listecombattans if c != z and c not in dead]
                if not combattanspossible:
                    continue
                cible = random.choice(combattanspossible)

                if random.randint(0, 10) <= combattans[cible][2]:
                    messages.append(f"{z} attaque {cible}, mais {cible} esquive !")
                else:
                    combattans[cible][0] -= combattans[z][1]
                    if combattans[cible][0] < 1:
                        if cible not in dead:
                            dead.append(cible)
                        messages.append(f"{z} attaque {cible}, et {cible} {random.choice(possiblemort)} !")
                    else:
                        messages.append(
                            f"{z} attaque {cible} — {combattans[z][1]} dégâts, il reste {combattans[cible][0]} PV."
                        )

        tours += 1
        if len(dead) == 7:
            break

    gagnant = next((c for c in listecombattans if c not in dead), None)
    messages.append("")
    if gagnant is None:
        messages.append("Erreur : pas de gagnant.")
    else:
        messages.append(f"Le grand vainqueur est {gagnant} !")
        if gagnant == choix:
            messages.append("Vous avez parié sur le bon cheval !")
        else:
            messages.append("Dommage, vous perdez !")

    # affichage du log scrollable
    ligne_h = 28
    visible = (fenetre.get_height() - 80) // ligne_h

    affichage = True
    while affichage:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    affichage = False
                elif event.key == pygame.K_DOWN:
                    scroll_offset = min(scroll_offset + 1, max(0, len(messages) - visible))
                elif event.key == pygame.K_UP:
                    scroll_offset = max(scroll_offset - 1, 0)
            if event.type == pygame.MOUSEWHEEL:
                scroll_offset -= event.y
                scroll_offset = max(0, min(scroll_offset, max(0, len(messages) - visible)))

        fenetre.fill(DARK)

        for i, msg in enumerate(messages[scroll_offset:scroll_offset + visible]):
            couleur = GREEN if "vainqueur" in msg or "parié sur" in msg else RED if "meurt" in msg or "quitte" in msg or "s'est" in msg or "compresser" in msg or "cancel" in msg or "Epstein" in msg or "discord" in msg or "ABR" in msg or "paisiblement" in msg or "table" in msg or "4chan" in msg or "lylian" in msg or "couronnes" in msg or "splashbot" in msg or "allégence" in msg or "glissant" in msg or "Saadi" in msg else WHITE
            surf = font_small.render(msg, True, couleur)
            fenetre.blit(surf, (40, 20 + i * ligne_h))

        hint = font_small.render("Flèches ou Molette pour faire défiler  |  Échap pour revenir", True, GREY)
        fenetre.blit(hint, (40, fenetre.get_height() - 35))

        pygame.display.flip()
        clock.tick(60)