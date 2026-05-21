import pygame
import random
from données import GestionBD as Gestion


WHITE = (255, 255, 255)
GREY = (100, 100, 120)
DARK = (30, 30, 30)
YELLOW = (255, 215, 0)
GREEN = (50, 200, 50)
RED = (200, 50, 50)
BLUE = (60, 60, 200)
HIGHLIGHT = (200, 160, 0)
 
 
def loto(fenetre,compte):
    font = pygame.font.Font(None, 30)
    font_small = pygame.font.Font(None, 24)
    font_big = pygame.font.Font(None, 42)
    clock = pygame.time.Clock()
    W, H = fenetre.get_size()
    argent_compte = Gestion.RecupArgent(compte)

    # Grille des boutons 
    boutons = []
    for i in range(49):
        x = 50 + (i % 7) * 110
        y = 60 + (i // 7) * 75 
        boutons.append((pygame.Rect(x, y, 80, 55), i + 1))
    
    numeros = [] # Liste des numéros tirés
    complementaire = None
    resultat = None # Résultat du Loto
 
    button_lancer = pygame.Rect(W // 2 - 100, 640, 200, 50)
    button_reset = pygame.Rect(W // 2 - 100, 700, 200, 40)
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_SPACE and len(numeros) == 6:
                    resultat = None
                    pool = list(range(1, 50))
                    gagnants = random.sample(pool, 5)
                    pool_comp = [n for n in pool if n not in gagnants]
                    comp = random.choice(pool_comp) # Numéro complémentaire
                    bons = set(numeros[:5]) & set(gagnants) # 5 numéros principaux
                    bon_comp = numeros[5] == comp
                    nb = len(bons)
                    if nb == 5 and bon_comp: # Tout juste
                        msg = "JACKPOT !!!"
                    elif nb == 5:
                        msg = "Rang 2 — 5 bons numéros !"
                    elif nb == 4 and bon_comp:
                        msg = "Rang 3 — 4 bons + complémentaire !"
                    elif nb == 4:
                        msg = "Rang 4 — 4 bons numéros"
                    elif nb == 3 and bon_comp:
                        msg = "Rang 5 — 3 bons + complémentaire"
                    elif nb == 3:
                        msg = "Rang 6 — 3 bons numéros"
                    elif nb == 2 and bon_comp:
                        msg = "Rang 7 — 2 bons + complémentaire"
                    elif nb == 2:
                        msg = "Rang 8 — 2 bons numéros"
                    else:
                        msg = "Rien du tout..."
                    resultat = (gagnants, comp, bons, bon_comp, msg)
 
            if event.type == pygame.MOUSEBUTTONDOWN:
                for rect, num in boutons:
                    if rect.collidepoint(event.pos):
                        if num in numeros:
                            numeros.remove(num)
                            resultat = None
                        elif len(numeros) < 6:
                            numeros.append(num)
                            resultat = None
                
                # Recoder une deuxième fois mais permet de  faire fonctionner le jeu
                if button_lancer.collidepoint(event.pos) and len(numeros) == 6:
                    resultat = None
                    pool = list(range(1, 50))
                    gagnants = random.sample(pool, 5)
                    pool_comp = [n for n in pool if n not in gagnants]
                    comp = random.choice(pool_comp)
                    bons = set(numeros[:5]) & set(gagnants)
                    bon_comp = numeros[5] == comp
                    nb = len(bons)
                    if nb == 5 and bon_comp:
                        msg = "JACKPOT !!!"
                    elif nb == 5:
                        msg = "Rang 2 — 5 bons numéros !"
                    elif nb == 4 and bon_comp:
                        msg = "Rang 3 — 4 bons + complémentaire !"
                    elif nb == 4:
                        msg = "Rang 4 — 4 bons numéros"
                    elif nb == 3 and bon_comp:
                        msg = "Rang 5 — 3 bons + complémentaire"
                    elif nb == 3:
                        msg = "Rang 6 — 3 bons numéros"
                    elif nb == 2 and bon_comp:
                        msg = "Rang 7 — 2 bons + complémentaire"
                    elif nb == 2:
                        msg = "Rang 8 — 2 bons numéros"
                    else:
                        msg = "Rien du tout..."
                    resultat = (gagnants, comp, bons, bon_comp, msg)
 
                if button_reset.collidepoint(event.pos):
                    numeros = []
                    complementaire = None
                    resultat = None
 
        fenetre.fill(DARK)
 
        titre = font_big.render("Loto", True, WHITE)
        fenetre.blit(titre, (W // 2 - titre.get_width() // 2, 15))

        # Affichage de la grille avec couleurs selon l'état de chaque numéro 
        for rect, num in boutons:
            est_principal = num in numeros[:5]
            est_comp = len(numeros) == 6 and num == numeros[5]
            gagne = resultat and num in resultat[2]
            gagne_comp = resultat and est_comp and resultat[3]
            couleur = GREEN if gagne or gagne_comp else HIGHLIGHT if est_principal else (150, 100, 0) if est_comp else GREY
            pygame.draw.rect(fenetre, couleur, rect, border_radius=6)
            txt = font.render(str(num), True, WHITE)
            fenetre.blit(txt, (rect.x + rect.w // 2 - txt.get_width() // 2,
                               rect.y + rect.h // 2 - txt.get_height() // 2))
 
        # Légende sélection
        nb_sel = len(numeros)
        if nb_sel < 5:
            hint_sel = f"Choisissez {5 - nb_sel} numéro(s) principal/aux"
        elif nb_sel == 5:
            hint_sel = "Choisissez maintenant votre complémentaire"
        else:
            principaux = numeros[:5]
            hint_sel = f"Vos numéros : {principaux}  +  complémentaire : {numeros[5]}"
        fenetre.blit(font_small.render(hint_sel, True, YELLOW), (50, 625))
        
        # Bouton "Lancer" grisé tant que la sélection n'est pas complète
        pret = len(numeros) == 6
        pygame.draw.rect(fenetre, BLUE if pret else (50, 50, 80), button_lancer, border_radius=8)
        fenetre.blit(font.render("Lancer le tirage", True, WHITE),
                     (button_lancer.x + 18, button_lancer.y + 14))
 
        pygame.draw.rect(fenetre, (100, 40, 40), button_reset, border_radius=8)
        fenetre.blit(font_small.render("Réinitialiser", True, WHITE),
                     (button_reset.x + 45, button_reset.y + 12))
 
        if resultat:
            gagnants, comp, bons, bon_comp, msg = resultat
            r1 = font_small.render(f"Tirage : {sorted(gagnants)}  +  complémentaire : {comp}", True, WHITE)
            fenetre.blit(r1, (50, 750))
            couleur_msg = GREEN if "Rang" in msg or "JACKPOT, vous gagnez 20 000 000" in msg else YELLOW if "2 bons" in msg else RED
            r2 = font_small.render(msg, True, couleur_msg)
            fenetre.blit(r2, (50, 775))
 
        hint = font_small.render("Espace pour lancer  |  Échap pour revenir", True, GREY)
        fenetre.blit(hint, (W // 2 - hint.get_width() // 2, H - 45))
 
        pygame.display.flip()
        clock.tick(60)