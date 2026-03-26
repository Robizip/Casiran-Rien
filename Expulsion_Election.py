<<<<<<< HEAD:Expulsion d'Election.py
# Créé par Benjamin Castel, le 12/03/2026 en Python 3.7

import random

def bataillepolitique(argent):
    dead = []
    possiblemort = ["meurt en glissant sur une flaque", "meurt en prétant allégence", "a bus trop de boisson splashbot les meilleurs boissons dans ce coin de l'assemblé national", "se prend un coup du crâne à lylian", "s'est fait 3 couronnes", "quitte ce monde cruel", "se perd sur 4chan", "se fait harceler par Amin Saadi", "s'endort paisiblement", "se prend le coin de la table", "a trop pratiqué l'ABR", "se fait compresser en .zip", "commence sa carrière de modérateur discord", "s'est fait cancel", "a été retrouvé sur les fichiers Epstein", "meurt"]
    listecombattans = ["Zemmour", "Macron", "Melenchon", "Bardella", "MarineLepen", "JeanMarrieLepen", "NicolaSarkozy", "FrançoisHollande"]
    combattans = {"Zemmour":[], "Macron":[], "Melenchon":[], "Bardella":[], "MarineLepen":[], "JeanMarrieLepen":[], "NicolaSarkozy":[], "FrançoisHollande":[]}

    while True:
        print("choisisez votre combattant parmis cette liste:")
        choix = input(listecombattans)
        if choix.lower == "zemmour" or "macron" or "melenchon" or "bardella" or "marinelepen" or "jeanmarrielepen" or "nicolasarkozy" or "françoishollande":
            break
        else:
            print(f"{choix} ? Ce choix me semble incorect veillez essayer à nouveau, \n Pensez à faire attention à la liste des personnages disponible et à l'orthographe de ceux-ci.")

    print(f"Choix pris en compte, vous avez donc parié {argent} sur {choix}")

    for z in listecombattans :
        combattans[z].append(random.randint(10,20)) #vie
        combattans[z].append(random.randint(1,5)) #dégats
        combattans[z].append(random.randint(0,6)) #evasion
        combattans[z].append(0) #donné binaire pour vie/mort

    print("Êtes vous prêt ?")
    print("Que le combat commence ! Bonne chance à tout les gladiateurs, et que le meilleur gagne !")

    tours = 0
    print("Tours 0")
    while len(dead) < 8:
        if tours > 0:
            print(f"Tours {tours}")
        random.shuffle(listecombattans)
        for z in listecombattans:
            combattanspossible = listecombattans
            combattanspossible.remove(z)
            for zz in dead:
                combattanspossible.remove(zz)
            cible = random.choice(combattanspossible)
            if random.randint(0,10) <= combattans[cible][2]:
                print(f"{z} attaque {cible}, mais {cible} esquive !")
            else:
                combattans[cible][0] -= combattans[z][1]
                if combattans[cible][0] < 1:
                    dead.append(cible)
                    print(f"{z} attaque {cible}, et {cible} {random.choice(possiblemort)} !")
                else:
                    print(f"{z} attaque {cible}, {cible} prend {combattans[z][1]} dégats ! \nIl lui reste {combattans[cible][0]} points de vie..")
        tours += 1
        if dead == 7:
            break
    for amin in listecombattans:
        if amin not in dead:
            gagnant = amin
    print(f"Et le grand vainqueur est {gagnant}")
    
    if gagnant == choix:
        print("vous avez parié sur le cheval gagnant !")
        print(f"votre argent passe de {argent}€ à {argent * 8}€")
        print("Bravo, n'hésitez pas à rejouer ! \nCe serait dommage de casser une série.")
        return argent*8
    else:
        print("Dommage, vous perdez tout votre argent")
        print("Un deuxième round  pour le regagner ?")
        print("ou alors une petite pause au bar dans le coin là-bas.")
        return 0
    
argent = 10
print(bataillepolitique(argent))
=======
# Créé par Benjamin Castel, le 12/03/2026 en Python 3.7

import random

def bataillepolitique(argent):
    dead = []
    possiblemort = ["meurt en glissant sur une flaque", "meurt en prétant allégence", "a bus trop de boisson splashbot les meilleurs boissons dans ce coin de l'assemblé national", "se prend un coup du crâne à lylian", "s'est fait 3 couronnes", "quitte ce monde cruel", "se perd sur 4chan", "se fait harceler par Amin Saadi", "s'endort paisiblement", "se prend le coin de la table", "a trop pratiqué l'ABR", "se fait compresser en .zip", "commence sa carrière de modérateur discord", "s'est fait cancel", "a été retrouvé sur les fichiers Epstein", "meurt"]
    listecombattans = ["Zemmour", "Macron", "Melenchon", "Bardella", "MarineLepen", "JeanMarrieLepen", "NicolaSarkozy", "FrançoisHollande"]
    combattans = {"Zemmour":[], "Macron":[], "Melenchon":[], "Bardella":[], "MarineLepen":[], "JeanMarrieLepen":[], "NicolaSarkozy":[], "FrançoisHollande":[]}

    while True:
        pari = input("combien voulez vous parier ?")
        pari = int(pari)
        if argent - pari > -1:
            break
        else:
            print("Vous n'avez pas assez d'argent pour cela, désolée")
            return argent

    while True:
        print("choisisez votre combattant parmis cette liste:")
        choix = input(listecombattans)
        if choix.lower == "zemmour" or "macron" or "melenchon" or "bardella" or "marinelepen" or "jeanmarrielepen" or "nicolasarkozy" or "françoishollande":
            break
        else:
            print(f"{choix} ? Ce choix me semble incorect veillez essayer à nouveau, \n Pensez à faire attention à la liste des personnages disponible et à l'orthographe de ceux-ci.")

    print(f"Choix pris en compte, vous avez donc parié {pari} sur {choix}")

    for z in listecombattans :
        combattans[z].append(random.randint(10,20)) #vie
        combattans[z].append(random.randint(1,5)) #dégats
        combattans[z].append(random.randint(0,6)) #evasion
        combattans[z].append(0) #donné binaire pour vie/mort

    print("Êtes vous prêt ?")
    print("Que le combat commence ! Bonne chance à tout les gladiateurs, et que le meilleur gagne !")

    tours = 0
    print("Tours 0")
    while len(dead) < 8:
        if tours > 0:
            print(f"Tours {tours}")
        random.shuffle(listecombattans)
        for z in listecombattans:
            combattanspossible = listecombattans
            combattanspossible.remove(z)
            for zz in dead:
                combattanspossible.remove(zz)
            cible = random.choice(combattanspossible)
            if random.randint(0,10) =< combattans[cible][2]:
                print(f"{z} attaque {cible}, mais {cible} esquive !")
            else:
                combattans[cible][0] -= combattans[z][1]
                if combattans[cible][0] < 1:
                    print(f"{z} attaque {cible}, et {cible} {random.choice(possiblemort)} !")
                print(f"{z} attaque {cible}, {cible} prend {combattants[z][1] dégats ! \nIl reste {combattans[cible][0]} points de vie..")














>>>>>>> 15aa30881179c610921e814dd555ad0d1dfdcf5f:Expulsion_Election.py
