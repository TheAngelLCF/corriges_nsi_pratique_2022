def verifie(tableau: list) -> bool:
    """
    Exemples :
    >>> verifie([0, 5, 8, 8, 9])
    True
    >>> verifie([8, 12, 4])
    False
    >>> verifie([-1, 4])
    True
    >>> verifie([5])
    True
    """
    assert isinstance(tableau, list) and tableau != [], 'Merci de spécifier un tableau (list) non vide !'
    minn = tableau[0]
    for rang in range(1, len(tableau)):
        if(minn <= tableau[rang]): minn = tableau[rang]
        else: return False
    return True
    

urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in list(resultat.keys()):
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale


if __name__ == '__main__':
    from doctest import testmod
    testmod()