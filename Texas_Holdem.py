# Créé par Benjamin Castel, le 29/09/2025 en Python 3.7
argent = 10
global argent

import random
def texassetup():
    hand1 = []
    hand2 = []
    table = []
    endbet = 0
    compteur = 0
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
    couleurs = ['Trèfle', 'Carreau', 'Cœur', 'Pique']
    jeu = []
    bet1 = 1
    bet2 = 2
    for couleur in couleurs:
        for valeur in valeurs:
            carte = {
                "valeur": valeur,
                "couleur": couleur
            }
            jeu.append(carte)

    a = random.randint(0,51)
    hand1.append(jeu[a])
    jeu.pop(a)
    compteur += 1
    a = random.randint(0,51-compteur)
    hand1.append(jeu[a])
    jeu.pop(a)
    compteur += 1
    a = random.randint(0,51-compteur)
    hand2.append(jeu[a])
    jeu.pop(a)
    compteur += 1
    a = random.randint(0,51-compteur)
    hand2.append(jeu[a])
    jeu.pop(a)
    compteur += 1

    return hand1, hand2, jeu, compteur


def texaslocal(argent1):
    #setup 2
    if argent1< 2:
        print("2 est la mise minimal")
        while True:
            b = input("voulez-vous l'ajouter ?")
            if b == "oui":
                z = input("mise supplmentaire du joueur")
                z = int(z)
                if z > argent:
                    print("vous n'avez pas assez d'argent")
                else:
                    return texaslocal(argent1 + z)
            else:
                return argent1
    a = texassetup()
    end = 0
    likemeter = 0
    banque = 0
    hand1 = a[0]
    hand2 = a[1]
    jeu = a[2]
    compteur = a[3]
    name "= ["MoneyMan", "Realplayer05", "JeanLassale", "EFN", "LeRN", "LFI", "Sarkozie", "Fraude_Fiscale_Lover89", "Mathis", "Amin", "Elon_Musk", "LeDineRigolo", "Xx_antoninDu96_xX", "Jean_Phillipe1920", "Kevin2012", "Luc", "Harley_harold", "Xavier_Noj", "PasLePatronDuCasino", "ForSure", "Chatgpt", "deep_seek", "Maza", "Bachar_Al_Assad", "Leasbienne", "LesCookies_deLaCafet", "Micheal_Afton", "JojoSucre", "Cortex91DesPiramides", "MinouLeChat", "Edupython", "VisualCode", "Spyder", "Pyrorca", "Johan", "LeSeranoSalé", "Asterion", "TomEtJerrie", "Basile_LeTueur_DeBulgareXx", "http_SansLeS", "MangaNimes", "SplashBot", "Hacker02", "IlanLeLaquel", "Karlie Chirk", "XavierNiel", "Terracid", "StreamerKick", "DavidLafargePokemon", "Malte", "GiletLaPerfectionAuMasculin", "Israel", "Amin_dupontDeLigoness", "MichelDuma", "Trivess","SandwichAuCrepit", "DonalTrump", "TK78", "ICE", "LaMeufDeSardoche", "ASMRtortue", "ReadShadowLeagend", "NodVPN", "Loui16", "SprinkleCookie_Arracheur2Monstres", "CreaJeu", "L_ordinateurDeCharle", "RougeSonic", "RandiStairs", "Pronote", "NickBate", "ChrisChan", "FeldupEnTMAX", "NetaMiaou", "Parole2Chat", "FuriousJumper", "JackLang", "LeLoupDe_Wallstreet", "JeanJesusDupuit", "Pididi", "Juda", "JL", "JaqueBoulon", "VerduLucas", "Tezos", "Alvin", "Theodore", "Simon", "NouveauLepen", "JeanLassale2027", "NeymarJr", "BricoDepot", "Fan2Detournement_Fiscal", "Ponzi", "DonDivin", "Bernard_Tapie", "Cnews", "HugoDes_Criptes", "Pirouette_cacahouete", "Vol370MalesiaAirline", "Mario&Luigi", "BobLenon", "Einpstein", "laPulga", "elBicho", "ElTigro", "Crouteurdu02", "Benzi", "PasTresNormanActivity", "Gerard2parts2gateau", "6769", "Timoté67", "tungtungtungsahur6767", "MDBTF", "Gardevoir", "Steve_Balaimont", "Emilien", "Christian_Quesada", "MultiplaGooner", "Minus8", "FalusMalus", "Overdlow", "Dexter", "WalterWhite", "JessiePinkman", "Julgane", "Chevocheur2Halouf", "RizMAyo", "TorahRienduTout", "", "LeCraneA_Lilian", "SmallVille", "Lorenzo76", "Kojima", "LeGabon", "CR7"]
    bot = name[random.randint(0,len(name)-1)]
    #le bot calcule si sa main est bien
    for z in hand2:
        if hand2[z][0] == "As":
            likemeter += 2
        elif hand2[z][0] == "Dame" or "Roi" or "Valet":
            likemeter += 1
    if hand2[0][0] == hand2[1][0]:
        likemetter += 4
    if hand2[0][1] == hand2[1][1]:
        likemetter += 1

    #continu player
    banque += 4
    argent1 -= 2
    endturn = 0
    up = 0
    intour = 0
    aa = 0
    while end < 4:
        while endturn == 0:

            while True:
                za = 1
                print("c'est votre tour !")
                print(f"votre main est: {hand1}, et vous avez: {argent1}€")
                if intour > 0:
                    a = input("Voulez-vous vous coucher ?")
                    if a.lower() == "oui":
                        print(f"Le gagnant de la somme de {banque} est {bot}")
                        return argent1
                if up < argent1:
                    a = input("voulez-vous augmenter votre mise ?")
                    if a.lower() == "oui":
                        aa = input("de combien d'euro ?")
                        if int(aa) < argent1:
                            print("Vous n'avez pas les fonds")
                            za = 0
                        else:
                            banque += int(a)
                            argent1 -= int(a)
                            break
                    else:
                        banque += up
                        argent1 -= up
                        break

                elif za == 1:
                    banque += argent1
                    argent1 = O
                    break




            print(f"au tour de {bot}")
            banque += int(a)
            if likemeter > 2 + intour and argent1 > 0:
                z = random.randint(0,1)
                if z == 1:
                    up = banque / 4
                    if up > argent1:
                        banque += argent1
                    else:
                        banque += up
                else:
                    banque += int(aa)
                    endturn = 1
            else:
                banque += int(aa)
                endturn = 1

            aa = 0
            intour += 1


        end += 1
        #fin tour carte + calcul likemeter
        a = random.randint(0,51-compteur)
        compteur += 1
        table.append(jeu[a])
        jeu.pop(a)
        print(f"les cartes actuellement sur la table sont {table}")

        #calcul du bot
        if hand2[0][0] == table[end][0]:
            likemeter += 4
        if hand2[1][0] == table[end][0]:
            likemeter += 4
        if end == 1: #calcul couleur 1
            if hand2[0][1] and hand2[1][1] == table[0][1]:
                likemeter += 1
        if end == 2: #couleur 2
            if hand2[0][1] and hand2[1][1] == table[0][1] and table[1][1]:
                likemeter += 4
        if end == 3: #couleur 3
            if hand2[0][1] and hand2[1][1] == table[0][1] and table[1][1]:
                if table[1][1] == table[2][1]:
                    likemeter += 5
                else:
                    likemeter -= 5

    #fin du jeu / calcul des points et decision du gagnant
    combin1 = []
    combin2 = []
    point1 = 0
    point2 = 0

    if hand1[0][0] and hand1[1][0] == table[0][0]:
        point1 += 1
    if hand1[0][0] and hand1[1][0] == table[1][0]:
        point1 += 1
    if hand1[0][0] and hand1[1][0] == table[2][0]:
        point1 += 1
    if point1 == 2:
        combin1.append(7)

    if hand2[0][0] and hand2[1][0] == table[0][0]:
        point2 += 1
    if hand2[0][0] and hand2[1][0] == table[1][0]:
        point2 += 1
    if hand2[0][0] and hand2[1][0] == table[2][0]:
        point2 += 1
    if point2 == 2:
        combin2.append(7)

    if combin1 == combin2:


















print(texaslocal(1))




