import random #type: ignore

def loto():
    numero_joueur = []
    for i in range(5):
        choix = int(input(f"Choisissez votre numéro {i+1} entre 1 et 49 : "))
        numero_joueur.append(choix)
    choix_complementaire = int(input("Choisissez votre numéro complémentaire entre 1 et 10 : "))
    numero_joueur.append(choix_complementaire)
    numero_gagnant = random.sample(range(1, 50), 5)  # 5 numéros uniques entre 1 et 49
    loto_complementaire = random.randint(1, 10)
    numero_gagnant.append(loto_complementaire)
    print("\nVos numéros :", numero_joueur[:-1], " + complémentaire :", numero_joueur[-1])
    print("Numéros gagnants :", numero_gagnant[:-1], " + complémentaire :", numero_gagnant[-1])
    bons_numeros = set(numero_joueur[:-1]) & set(numero_gagnant[:-1])
    if bons_numeros == 0:
        print("Vous avez 0 bons numéros ")
    else:
        print(f"\nVous avez trouvé {len(bons_numeros)} bons numéros :", bons_numeros)
    if numero_joueur[-1] == numero_gagnant[-1]:
        print("Vous avez aussi trouvé le numéro complémentaire !")

loto()
