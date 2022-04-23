def maxi(tab: list) -> tuple:
    """
    >>> maxi([1,5,6,9,1,2,3,7,9,8])
    (9, 3)
    """
    rang = 0
    maxi = tab[0]
    for k in range(1, len(tab)):
        if(maxi < tab[k]):
            rang = k
            maxi = tab[k]
    return maxi, rang

def positif(T):
    """
    >>> positif([-1,0,5,-3,4,-6,10,9,-8 ])
    T =  [-1, 0, 5, -3, 4, -6, 10, 9, -8]
    [0, 5, 4, 10, 9]
    """
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ',T)
    return T2


if __name__ == '__main__':
    from doctest import testmod
    testmod()