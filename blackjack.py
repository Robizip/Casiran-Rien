# Créé par Benjamin Castel, le 11/09/2025 en Python 3.7
import random

def blackjack(argent2):
    carte = [
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10
        ]

    nb = random.randint(0,51)
    cartejouer = carte[nb]
    carte.pop(nb)
    x = 1
    print(cartejouer)
    hit = cartejouer
    stay = 1
    lost = 0
    win = 0
    while True:
        choix = input("hit or stay")
        print(choix)
        if choix == "hit":
            print("hit")
            nb = random.randint(1,51-x)
            cartejouer = carte[nb]
            print("dealer :")
            print(cartejouer)
            x += 1
            carte.pop(nb)
            hit += cartejouer
            print("you :")
            print(hit)
            if hit > 20:
                break
        elif choix == "stay":
            stay = 1
            print(f"you stay at {hit}")
            nb = random.randint(1, 51-x)
            cartejouer = carte[nb]
            print("dealer :")
            print(cartejouer)
            hit += cartejouer
            print("you :")
            print(hit)
            if hit < 22:
                lost = 1
            elif hit > 21:
                win = 1
            break

    if hit < 21 and lost != 1 or win == 1:
        print(f"you win")
        print(f"your money goes from {argent2} to {argent2*2}")
        argent2 =  argent2*2
    elif hit > 21 or lost == 1:
        print("too bad you lose your money")
        argent2 = 0
    elif hit == 21:
        print("Blackjack !")
        print(f"Jackpot! your money goes from {argent2} to {argent2*3}")
        argent2 = argent2*3
    return argent2

def menu():
    end = 0
    mise = 0
    argent = int(input("your total money"))
    while end != 1:
        while True:
            mise = int(input("what's  your bet ?"))
            if mise > argent:
                print("too poor")
            else:
                break
        argent = argent - mise
        print(f"bet placed for {mise}$")
        argent = argent + blackjack(mise)
        if argent < 1:
            end = 1
        if end != 1:
            a = input("Do you want do continu ? yes/no")
            if a == "no":
                end = 1
    return argent
print(f"You end your game with {menu()}$ in your pockets")




