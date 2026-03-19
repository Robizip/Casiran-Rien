import random #type: ignore

def chifoumi():
    pierre = "pierre"
    ciseaux = "ciseaux"
    feuille = "feuille"
    jeu = [pierre, feuille, ciseaux]
    victoire_joueur = 0
    victoire_ordi = 0
    while victoire_joueur < 3 and victoire_ordi < 3 :
        choix = input("Choisis ton signe \n" \
                  "pierre \n" \
                  "feuille \n" 
                  "ciseaux \n")
        ordi = random.choice(jeu)
        print(f"L'ordinateur a choisi : {ordi}")
        if choix == ordi:
            print("Egalité")
        elif (choix == "pierre" and ordi == "ciseaux") \
            or (choix == "ciseaux" and ordi == "feuille") \
            or (choix == "feuille" and ordi == "pierre"):
            victoire_joueur += 1
            print(f"Tu as gagné un point, tu as {victoire_joueur} points, continue mon négro de Bagdad ! ")
        else:
            victoire_ordi += 1
            print(f"Tu as perdu, l'ordinateur a {victoire_ordi} points, resaisis-toi ! ")
        if victoire_joueur == 3:
            print("T'as gagné, c'est bien. ")
        else:
            print("Tia perdu, tié nul, HAAAAAAAAAAAAAHHHHHHHAAAAAAAAA !!! ")

chifoumi()