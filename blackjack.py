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
        choix = input("tire or reste \n") #choix
        print(choix)
        if choix.lower() == "tire":
            print("vous tirez")
            nb = random.randint(1,51-x) 
            cartejouer = carte[nb]
            print("\ncroupier :")
            print(cartejouer)
            x += 1
            carte.pop(nb)
            hit += cartejouer
            print("\nvous :")
            print(hit)
            print("\n")
            if hit > 20: #teste si la carte après le "tirer" compte ou non
                break
        elif choix == "reste":
            stay = 1
            print(f"vous restez à {hit}")
            nb = random.randint(1, 51-x) #sors une dernière carte
            cartejouer = carte[nb]
            print("croupier :")
            print(cartejouer)
            hit += cartejouer
            print("vous :")
            print(hit)
            if hit < 22: #teste si le "rester" compte ou non
                lost = 1
            elif hit > 21:
                win = 1
            break

    if hit < 21 and lost != 1 or win == 1: #teste si le joueur a gagner en testant : que le total fasse moins que 21
        print(f"vous gagnez")              #et qu'il n'ai pas perdu, ou alors qu'il ai gagné en étant "rester" ou "stay"
        print(f"votre argent passe de {argent2} à {argent2*2}")
        argent2 =  argent2*2
    elif hit > 21 or lost == 1: # si le total dépasse 21 ou que le joueur a perdu il perd tout
        print("Dommage, vous perdez tout...")
        argent2 = 0
    elif hit == 21:  #teste si le joueur a gagné (grace aux autres testes) si le total est égale à exactement 21 pour le jackpot 
        print("Blackjack !")
        print(f"Jackpot! votre argent passe de {argent2} à {argent2*3}")
        argent2 = argent2*3
    return argent2 #renvoie l'argent gagné ou perdu à la fin du jeu

print(blackjack(10))




