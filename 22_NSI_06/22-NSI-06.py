def maxi(tab: list) -> tuple:
    assert isinstance(tab, list), 'Merci de mettre en paramètre une liste !'
    assert tab != [], 'Merci de mettre une liste non vide !'
    maxi = tab[0]
    rang = 0
    for k in range(len(tab)):
        assert isinstance(tab[k], int), 'L\'élement "' + str(tab[k]) + '" n\'est pas un nombre entier !'
        if(maxi < tab[k]):
            maxi = tab[k]
            rang = k
    return (maxi, rang)
    



def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n and trouve == False :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j += 1
        if j == g:
            trouve = True
        i += 1
    return trouve
