def nb_repetitions(elt, tab: list) -> int:
    """
    >>> nb_repetitions(5,[2,5,3,5,6,9,5])
    3
    >>> nb_repetitions('A',[ 'B', 'A', 'B', 'A', 'R'])
    2
    >>> nb_repetitions(12,[1, '! ',7,21,36,44])
    0
    """
    assert isinstance(tab, list), 'Merci de mettre un liste dans le paramètre tab'
    compteur = 0
    for element in tab:
        if(element == elt):
            compteur += 1
    return compteur
    
    

def binaire(a):
    """
    >>> binaire(0)
    '0'
    >>> binaire(77)
    '1001101'
    """
    bin_a = str(a % 2)
    a = a // 2
    while a != 0 :
        bin_a = str((a%2)) + bin_a
        a = a // 2
    return bin_a

if __name__ == '__main__':
    from doctest import testmod
    testmod()