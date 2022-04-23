def multiplication(n1: int, n2: int):
    """
    Exemples:
    >>> multiplication(3,5)
    15
    >>> multiplication(-4,-8)
    32
    >>> multiplication(-2,6)
    -12
    >>> multiplication(-2,0)
    0
    """
    final = 0
    if(n2 < 0): boucle = range(n2, 0)
    else: boucle = range(n2)
    if(n1 < 0 and n2 < 0):
        n1 = int(str(n1)[1:])
    for _ in boucle:
        final += n1
    return final

def dichotomie(tab, x):
    """
        tab : tableau d’entiers trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
        
    Exemples:
    >>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28)
    True
    >>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27)
    False
    """

    debut = 0 
    fin = len(tab) - 1
    while debut <= fin:
        m = (fin + debut) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False

if __name__ == '__main__':
    from doctest import testmod
    testmod()