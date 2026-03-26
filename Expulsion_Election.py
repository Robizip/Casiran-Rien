import random
import time

def bataillepolitique(argent):
    dead = [] #établissement des variables
    possiblemort = ["meurt en glissant sur une flaque", "meurt en prétant allégence", "a bus trop de boisson splashbot les meilleurs boissons dans ce coin de l'assemblé national", "se prend un coup du crâne à lylian", "s'est fait 3 couronnes", "quitte ce monde cruel", "se perd sur 4chan", "se fait harceler par Amin Saadi", "s'endort paisiblement", "se prend le coin de la table", "a trop pratiqué l'ABR", "se fait compresser en .zip", "commence sa carrière de modérateur discord", "s'est fait cancel", "a été retrouvé sur les fichiers Epstein", "meurt"]
    listecombattans = ["Zemmour", "Macron", "Melenchon", "Bardella", "MarineLepen", "JeanMarrieLepen", "NicolaSarkozy", "FrançoisHollande"]
    combattans = {"Zemmour":[], "Macron":[], "Melenchon":[], "Bardella":[], "MarineLepen":[], "JeanMarrieLepen":[], "NicolaSarkozy":[], "FrançoisHollande":[]}

    while True: #choix du personnage
        print("choisisez votre combattant parmis cette liste:")
        choix = input(str(listecombattans))
        if choix.lower() in [c.lower() for c in listecombattans]:
            break
        else:
            print(f"{choix} ? Ce choix me semble incorect veillez essayer à nouveau, \n Pensez à faire attention à la liste des personnages disponible et à l'orthographe de ceux-ci.")

    print(f"Choix pris en compte, vous avez donc parié {argent} sur {choix}")

    for z in listecombattans : #établissement aléatoire des stats
        combattans[z].append(random.randint(10,20)) #vie
        combattans[z].append(random.randint(1,5)) #dégats
        combattans[z].append(random.randint(0,6)) #evasion = pourcentage de chance d'esquiver
        combattans[z].append(0) #donné binaire pour vie/mort

    print("Êtes vous prêt ?")
    print("Que le combat commence ! Bonne chance à tout les gladiateurs, et que le meilleur gagne !")
    time.sleep(3)
    tours = 0
    print("Tours 0")
    while len(dead) < 8: #boucle durant tout le combat 
        if tours > 0:
            print(f"Tours {tours}") #annonce du tour
        random.shuffle(listecombattans)
        for z in listecombattans: #chaque combattans fait son action
            if z not in dead:
                combattanspossible = listecombattans.copy() 
                combattanspossible.remove(z)
                for zz in dead: #rend impossible que l'ia attaque un personnage déjà mort
                    if zz in combattanspossible: 
                        combattanspossible.remove(zz)
                if not combattanspossible:  
                    continue
                cible = random.choice(combattanspossible)#le personnage cible un autre
                if random.randint(0,10) <= combattans[cible][2]: #teste si la cible arrive à esquive celon sa state d'evasion
                    print(f"{z} attaque {cible}, mais {cible} esquive !")
                else:
                    combattans[cible][0] -= combattans[z][1]
                    if combattans[cible][0] < 1:
                        if cible not in dead:  
                            dead.append(cible) #le combattant est mis comme mort
                        print(f"{z} attaque {cible}, et {cible} {random.choice(possiblemort)} !") #message de mort aléatoire
                    else:
                        print(f"{z} attaque {cible}, {cible} prend {combattans[z][1]} dégats ! \nIl lui reste {combattans[cible][0]} points de vie..")
                        time.sleep(2) #attente pour rendre le jeu moins rapide
        tours += 1
        time.sleep(1)
        if len(dead) == 7:  
            break
    for amin in listecombattans: #recherche du personnage encore en vie
        if amin not in dead:
            gagnant = amin
    if gagnant == None: #teste en cas où le code ne marche pas 
        gagnant = "Erreur votre argent vous a été rendu"
        return argent
    time.sleep(1)
    print(f"Et le grand vainqueur est {gagnant}")
    time.sleep(1)
    if gagnant == choix:
        print("\n\nvous avez parié sur le cheval gagnant !")
        print(f"votre argent passe de {argent}€ à {argent * 8}€")
        print("\nBravo, n'hésitez pas à rejouer ! \nCe serait dommage de casser une série.")
        return argent*8
    else:
        print("\n\nDommage, vous perdez tout votre argent")
        print("Un deuxième round pour le regagner ?")
        print("\nou alors une petite pause au bar dans le coin là-bas.")
        return 0
    
argent = 10
print(bataillepolitique(argent))