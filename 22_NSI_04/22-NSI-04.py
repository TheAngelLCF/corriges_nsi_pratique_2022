def recherche(tab: list) -> list:
    final = []
    for rang in range(len(tab) - 1):
        if(tab[rang] + 1 == tab[rang + 1]):
            final.append((tab[rang], tab[rang + 1]))
    return final

def propager(M, i, j, val):
    if M[i][j] == val:
        return

    M[i][j] = val

    # l'élément en haut fait partie de la composante
    if ((i-1) >= 0 and M[i-1][j] == 1):
        propager(M, i-1, j, val)

    # l'élément en bas fait partie de la composante
    if ((i + 1) < len(M) and M[i+1][j] == 1):
        propager(M, i + 1, j, val)

    # l'élément à gauche fait partie de la composante
    if ((j - 1) >= 0 and M[i][j-1] == 1):
        propager(M, i, j - 1, val)

    # l'élément à droite fait partie de la composante
    if ((j + 1) < len(M) and M[i][j+1] == 1):
        propager(M, i, j + 1, val)
