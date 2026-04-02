# Créé par Benjamin Castel, le 17/09/2025 en Python 3.7
import random
import time
argent = int(input("argent totale"))


def roulette(argent):
    startmoney = argent
    bet = []
    endbet = 0


    while endbet < 1:
        while True:
            time.sleep(1)
            print("choisissez un nombre (0 to 37) ou une couleur rouge ou noir)")
            time.sleep(1)
            print("parier sur un nombre vaut 35 pour 1 misé \nparier sur une couleur vaut 2 pour 1 misé")
            time.sleep(1)
            print(f"vous avez {argent}$")
            time.sleep(1)
            choix = input("Placez un parie (la catégorie): ").strip().lower()


            if choix.isdigit():
                numero = int(choix)
                if 0 <= numero <= 37:
                    bet.append(numero)
                    break
                else:
                    print("Le nombre doit être entre 0 et 37.")
            
            choix = choix.lower()
            if choix == "rouge" or choix == "noir":
                bet.append(choix)
                break

            else:
                print("Parie invalide. veillez entreer un nombre de 0-37 ou 'rouge'/'noir'.")

            print("Parie invalide, veillez réessayer")
        print(f"\n\nVous avez {argent}$")
        while True:
            try:
                time.sleep(1)
                bb = int(input("Combien voulez vous parier ? "))
                if bb <= argent and bb > 0:
                    argent -= bb
                    bet.append(bb)
                    break
                else:
                    print("La maison de fait pas crédit.")
                    time.sleep(1)
                    print("Revenez quand vous un petit peu plus... riche.")
            except ValueError:
                print("Veillez enter un nombre valide.")
        if argent == 0:
            endbet = 1
        if argent > 0:
            time.sleep(1)
            a = input("Voulez vous placer un autre parie ? oui/non")
            if a.lower() == "non":
                endbet = 1

    number = random.randint(0,37)

    if number == 0:
        color = "vert"
    elif number in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
        color = "rouge"
    else:
        color = "noir"
    print(f"{number} {color}")
    for z in range(0, len(bet), 2):  
        if bet[z] == number:
            time.sleep(1)
            print(f"Bravo, vous gagnez grâce à un nombre {bet[z]}\n"
            "votre argent parié ({bet[z+1]}), avec une côte de 35 pour 1, monte à {bet[z+1]*36}")
            argent += bet[z+1]*36
        elif str(bet[z]) == color: 
            time.sleep(1)
            print(f"Bravo vous gagnez grâce à une couleur {color}\n"
            "votre argent parié ({bet[z+1]}), avec une côte de 2 pour 1, monte à {bet[z+1]*2}")
            argent += bet[z+1]*2

    time.sleep(2)
    print(f"\n\n\nEn tout, votre argent est allé de {startmoney}€, à {argent}€.")
    return argent


print(roulette(10))