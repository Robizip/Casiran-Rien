import random #type: ignore
def machine_sous():
    symboles = ["🍒", "🍋", "🍊", "🍇", "🍉", "🍀", "🔔", "💎", "⭐", "7"]
    tirage = [random.choice(symboles) for _ in range(3)]
    print(" | ".join(tirage))

    tirage = list(set(tirage)) # Retire tous les éléments en double du tirage
    if len(tirage) == 1 : # Vérification 3 symboles identiques
        if tirage[0] == "7" : # Vérification si jackpot
            print("Jackpot, tu as gagné !!!")
        else :
            print(f"Bravo, 3 {tirage[0]} identiques !!")
    elif len(tirage) == 2 : # Vérification 2 symboles identiques
        print("Deux symboles identiques, pas mauvais")
    else :
        print("Perdu, réessaie !")
        
machine_sous()