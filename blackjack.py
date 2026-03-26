# Créé par Benjamin Castel, le 11/09/2025 en Python 3.7
import random

def blackjack(argent2):
    carte = [   #liste des cartes, uniquement leurs valeurs le reste est inutile
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10
        ]

    nb = random.randint(0,51) #tire une carte au hasard 
    cartejouer = carte[nb]
    carte.pop(nb) #retire la carte déjà tiré du jeu
    x = 1
    print(cartejouer)
    hit = cartejouer
    stay = 1
    lost = 0
    win = 0

    while True: #boucle du jeu entier
        choix = input("tirer or rester \n") #choix
        print(choix)
        if choix.lower() == "tirer":
            print("tirer")
            nb = random.randint(1,51-x) 
            cartejouer = carte[nb]
            print("dealer :")
            print(cartejouer)
            x += 1
            carte.pop(nb)
            hit += cartejouer
            print("vous :")
            print(hit)
            if hit > 20: #teste si la carte après le "tirer" reste sous les 21
                break
        elif choix == "rester":
            stay = 1
            print(f"vous restez à {hit}")
            nb = random.randint(1, 51-x) #sors une dernière carte
            cartejouer = carte[nb]
            print("dealer :")
            print(cartejouer)
            hit += cartejouer
            print("vous :")
            print(hit)
            if hit < 22: #teste si le "rester" compte ou non
                lost = 1
            elif hit > 21:
                win = 1
            break

    if hit < 21 and lost != 1 or win == 1:
        print(f"vous gagnez")
        print(f"votre argent passe de {argent2} à {argent2*2}")
        argent2 =  argent2*2
    elif hit > 21 or lost == 1:
        print("Dommage, vous perdez tout...")
        argent2 = 0
    elif hit == 21:
        print("Blackjack !")
        print(f"Jackpot! votre argent passe de {argent2} à {argent2*3}")
        argent2 = argent2*3
    return argent2

print(blackjack(10))




