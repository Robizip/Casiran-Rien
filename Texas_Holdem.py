# Créé par Benjamin Castel, le 29/09/2025 en Python 3.7
import random
argent = 10
def texassetup():
    hand1 = []
    hand2 = []
    table = []
    compteur = 0

    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
    couleurs = ['Trèfle', 'Carreau', 'Cœur', 'Pique']

    jeu = []

    for couleur in couleurs:
        for valeur in valeurs:
            jeu.append({"valeur": valeur, "couleur": couleur})

    for _ in range(2):
        a = random.randint(0, len(jeu)-1)
        hand1.append(jeu.pop(a))

        a = random.randint(0, len(jeu)-1)
        hand2.append(jeu.pop(a))

    return hand1, hand2, table, jeu

def valeur_num(v):
    ordre = {
        '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
        '8':8,'9':9,'10':10,'Valet':11,
        'Dame':12,'Roi':13,'As':14
    }
    return ordre[v]

def evaluer(main, table):
    cartes = main + table
    valeurs = sorted([valeur_num(c["valeur"]) for c in cartes])
    couleurs = [c["couleur"] for c in cartes]
    compte = {}
    for v in valeurs:
        compte[v] = compte.get(v, 0) + 1
    counts = sorted(compte.values(), reverse=True)
    flush = any(couleurs.count(c) >= 5 for c in set(couleurs))
    valeurs_uniques = sorted(set(valeurs))
    suite = False
    for i in range(len(valeurs_uniques)-4):
        if valeurs_uniques[i+4] - valeurs_uniques[i] == 4:
            suite = True
    if flush and suite:
        return 9
    if 4 in counts:
        return 8
    if 3 in counts and 2 in counts:
        return 7
    if flush:
        return 6
    if suite:
        return 5
    if 3 in counts:
        return 4
    if counts.count(2) >= 2:
        return 3
    if 2 in counts:
        return 2
    return 1

def texaslocal(argent1):
    if argent1 < 2:
        print("Mise minimale = 2€")
        return argent1
    hand1, hand2, table, jeu = texassetup()
    banque = 4
    argent1 -= 2
    print("Ta main :", hand1)
    for _ in range(3):
        table.append(jeu.pop(random.randint(0, len(jeu)-1)))
    print("Table :", table)
    choix = input("Continuer ? (oui/non) : ")
    if choix == "non":
        print("Tu te couches.")
        return argent1
    table.append(jeu.pop(random.randint(0, len(jeu)-1)))
    print("Table :", table)
    choix = input("Continuer ? (oui/non) : ")
    if choix == "non":
        print("Tu te couches.")
        return argent1
    table.append(jeu.pop(random.randint(0, len(jeu)-1)))
    print("Table finale :", table)
    print("Main bot :", hand2)
    score1 = evaluer(hand1, table)
    score2 = evaluer(hand2, table)
    print("Score joueur :", score1)
    print("Score bot :", score2)
    if score1 > score2:
        print("Tu gagnes !")
        argent1 += banque
    elif score1 < score2:
        print("Le bot gagne")
    else:
        print("Égalité")
        argent1 += banque // 2

    return argent1

while argent >= 2:
    argent = texaslocal(argent)
    print("Argent :", argent)

print("T'as plus d'argent")