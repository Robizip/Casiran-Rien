import random #type: ignore

def sim_de():
    manche_joueurs = 0
    manche_ordi = 0
    
    while manche_joueurs < 3 and manche_ordi < 3:
        liste_joueurs = [] # on vide les listes au début de chaque manche
        liste_ordi = []
        lancers = int(input("Combien de dés souhaitez-vous lancer ? : "))
        face = int(input("Combien de faces souhaitez-vous ? : "))
        
        for i in range(lancers):
            dés = random.randint(1, face)
            ordi = random.randint(1, face)
            print(f"Ton dé : {dés} | Dé ordi : {ordi}")
            liste_joueurs.append(dés)
            liste_ordi.append(ordi)
            
            # somme après la manche
            somme_joueurs = sum(liste_joueurs)
            somme_ordi = sum(liste_ordi)
            print(f"Ta somme : {somme_joueurs}")
            print(f"Somme ordi : {somme_ordi}")
        if somme_joueurs > somme_ordi:
            manche_joueurs += 1
            print(f"Tu gagnes cette manche ! Score : Toi {manche_joueurs} - Ordi {manche_ordi}\n")
        elif somme_ordi > somme_joueurs:
            manche_ordi += 1
            print(f"L’ordi gagne cette manche ! Score : Toi {manche_joueurs} - Ordi {manche_ordi}\n")
        else:
            print("Égalité ! Pas de point ajouté.\n")
    # fin du jeu
    if manche_joueurs == 3:
        print("BRAVO ! Tu as gagné la partie.")
    else:
        print("L'ordi a gagné la partie...")

sim_de()