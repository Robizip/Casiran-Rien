# Créé par Benjamin Castel, le 17/09/2025 en Python 3.7
import random
argent = int(input("total money"))


def roulette(argent):
    startmoney = argent
    bet = []
    endbet = 0


    while endbet < 1:
        while True:
            print("Choose a number (0 to 37) or a color (red or black)")
            print("betting on a single number has a pay of 35:1 \nbetting on a color is a 1:1")
            print(f"You have {argent}$")
            choix = input("Place a bet (the category): ").strip().lower()


            if choix == "red" or choix == "black":
                bet.append(choix)
                break


            if choix.isdigit():
                numero = int(choix)
                if 0 <= numero <= 37:
                    bet.append(numero)
                    break
                else:
                    print("Number must be between 0 and 37.")
            else:
                print("Invalid input. Please enter a number between 0-37 or 'red'/'black'.")

            print("wrong input, try again")
        print(f"You have {argent}$")
        while True:
            try:
                bb = int(input("How much do you want to bet on that? "))
                if bb <= argent and bb > 0:
                    argent -= bb
                    bet.append(bb)
                    break
                else:
                    print("You can't bet more than you have or a non-positive amount.")
                    print("The house doesn't make credit.")
            except ValueError:
                print("Please enter a valid number.")
        if argent == 0:
            endbet = 1
        if argent > 0:
            a = input("Do you want to place another bet ? yes/no")
            if a == "no":
                endbet = 1

    number = random.randint(0,37)

    if number == 0:
        color = "green"
    elif number in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
        color = "red"
    else:
        color = "black"
    print(color)
    for z in range(0, len(bet), 2):  # <- correction ici
        if bet[z] == number:
            print(f"Congrats, you win with a number bet with the number {bet[z]}\n"
            "your bet money ({bet[z+1]}), with a 35:1 rule, goes up to {bet[z+1]*36}")
            argent += bet[z+1]*36
        elif str(bet[z]) == color:  # inutile de caster deux fois
            print(f"Congrats, you win with a color bet with the color {color}\n"
            "your bet money ({bet[z+1]}), with a 1:1 rule, goes up to {bet[z+1]*2}")
            argent += bet[z+1]*2


    print(f"Your money went from: {startmoney}, to {argent}.")
    return argent



end = 0
play = roulette(argent)
if play > 0:
    while end < 1:
        d = input("do you want to play again ? yes/no")
        if d == "yes":
            print("good luck")

            while True:
                dd = int(input("how much of your money do you wana re bet ?"))
                if dd > argent:
                    print("The house doesn't make credits")
                elif dd > 0:
                    argent = dd
                    play -= argent
                    play += roulette(argent)
        elif d == "no":
            end = 1
        else:
            print("incorrect input, please try again")
else:
    print("Im sorry you can't continu without any money to bet")
