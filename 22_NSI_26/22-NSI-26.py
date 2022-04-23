def RechercheMin(tab: list) -> int:
    """
    >>> RechercheMin([5])
    0
    >>> RechercheMin([2, 4, 1])
    2
    >>> RechercheMin([5, 3, 2, 2, 4])
    2
    """
    trier = tab.copy()
    trier.sort()
    assert tab != [] and (tab != trier or len(tab) == 1), "Merci de spécifier une liste d'entier non vide non trié !"
    minn = 0
    for k in range(len(tab)):
        if(tab[minn] > tab[k]): minn = k
    return minn
    


def separe(tab):
    """
    >>> separe([1, 0, 1, 0, 1, 0, 1, 0])
    [0, 0, 0, 0, 1, 1, 1, 1]
    >>> separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0])
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    """
    i = 0
    j = len(tab) - 1
    while i < j :
        if tab[i] == 0 :
            i = i + 1
        else :
            tab[i], tab[j] = tab[j], tab[i]
            j = j - 1
    return tab

if __name__ == '__main__':
    from doctest import testmod
    testmod()