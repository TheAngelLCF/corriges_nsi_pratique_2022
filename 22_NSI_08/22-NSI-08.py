def recherche(elt: int, tab: list) -> int:
    """
    Exemples:
    >>> recherche(1, [2, 3, 4])
    -1
    >>> recherche(1, [10, 12, 1, 56])
    2
    >>> recherche(50, [1, 50, 1])
    1
    >>> recherche(15, [8, 9, 10, 15])
    3
    """
    for rang in range(len(tab)):
        if(tab[rang] == elt): return rang
    return -1

def insere(a, tab):
    """
    Exemples:
    >>> insere(3,[1,2,4,5])
    [1, 2, 3, 4, 5]
    >>> insere(10,[1,2,7,12,14,25])
    [1, 2, 7, 10, 12, 14, 25]
    >>> insere(1,[2,3,4])
    [1, 2, 3, 4]
    """
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(l) - 2
    while a < l[i] and i >= 0: 
      l[i+1] = l[i]
      l[i] = a
      i = i - 1
    return l

if __name__ == '__main__':
    from doctest import testmod
    testmod()