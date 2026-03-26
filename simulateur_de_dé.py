import random #type: ignore

def sim_de():
    manche_joueurs = 0
    manche_ordi = 0
    
    while manche_joueurs < 3 and manche_ordi < 3:
        liste_joueurs = [] # on vide les listes au début de chaque manche
        liste_ordi = []
        
        verif_lancers = False # Système vérification
        while not verif_lancers: 
            lancers = input("Combien de dés souhaitez-vous lancer? ")
            try :
                int(lancers)
            except :
                print("Merci de mettre de vrai nombre.\n")
            else :
                lancers = int(lancers)
                if lancers <= 0 :
                    print("Merci de ne pas mettre de nombre négatif ou nul.\n")
                else :
                    verif_lancers = True


        
        verif_face = False # El famoso retour du système de vérification
        while not verif_face: 
            face = input("Combien de faces souhaitez-vous ? ")
            try :
                int(face)
            except :
                print("Merci de mettre de vrai nombre.\n")
            else :
                face = int(face)
                if face <= 0 :
                    print("Merci de ne pas mettre de nombre négatif ou nul.\n")
                else :
                    verif_face = True
        
        for i in range(lancers):
            dés = random.randint(1, face)
            ordi = random.randint(1, face)
            print(f"Valeur de ton dé : {dés} | Valeur du dé de l’ordi : {ordi}")
            liste_joueurs.append(dés)
            liste_ordi.append(ordi)
            
            # somme après la manche
            somme_joueurs = sum(liste_joueurs)
            somme_ordi = sum(liste_ordi)
            print(f"Somme personnelle : {somme_joueurs}")
            print(f"Somme ordi : {somme_ordi}")
        if somme_joueurs > somme_ordi:
            manche_joueurs += 1
            print(f"\nTu gagnes cette manche ! Score : Toi {manche_joueurs} - Ordi {manche_ordi}\n")
        elif somme_ordi > somme_joueurs:
            manche_ordi += 1
            print(f"\nL’ordi gagne cette manche ! Score : Toi {manche_joueurs} - Ordi {manche_ordi}\n")
        else:
            print("\nÉgalité ! Pas de point ajouté.\n")
    # fin du jeu
    if manche_joueurs == 3:
        print("\nBRAVO ! Tu as gagné la partie.")
    else:
        print("\nL'ordi a gagné la partie...")

sim_de()