# Créé par Benjamin Castel, le 10/02/2026 en Python 3.7

def s():
    combin1 = []
    combin2 = []
    point1 = 0
    point2 = 0
    hand1 = [[4,1],[4,0]]
    hand2 = [[1,0],[2,0]]
    table = [[4,2],[4,3],[3,0]]
    table.append(hand1[0])
    table.append(hand1[1])
    dico = {}
    for z in range(len(table)):
        if table[z] not in dico:
            dico.append(table[z])
        else:
            dico[z]
