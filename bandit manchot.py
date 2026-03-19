import random #type: ignore
def machine_sous():
    symboles = ["🍒", "🍋", "🍊", "🍇", "🍉", "🍀", "🔔", "💎", "⭐", "7️⃣"]
    tirage = [random.choice(symboles) for _ in range(3)]
    print(" | ".join(tirage))
    
    if tirage.count("7️⃣") == 3:
        print("Jackpot, tu as gagné !!!")
    elif tirage[0] == tirage[1] == tirage[2]:
        print(f"Bravo, 3 {tirage[0]} identiques !!")
    elif tirage[0] == tirage[1] or tirage[1] == tirage[2] or tirage[0] == tirage[2]:
        print("Deux symboles identiques, pas mauvais")
    else:
        print("Perdu, réessaie !")

machine_sous()