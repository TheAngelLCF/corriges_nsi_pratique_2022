def moyenne(tab: list):
    """
    Exemples :
    >>> moyenne([1.0])
    1.0
    >>> moyenne([1.0, 2.0, 4.0])
    2.3333333333333335
    """
    assert tab != [], "Merci de spécifier un tableau non vide !"
    final = 0
    for elt in tab:
        assert isinstance(elt, float), str(float) + " n'est psa un float, uniquement des floattants doivent être dans le tableau !"
        final += elt
    return final / len(tab)

def dec_to_bin(a):
    """
    Exemples:
    >>> dec_to_bin(83)
    '1010011'
    >>> dec_to_bin(127)
    '1111111'
    """
    bin_a = str(a % 2)
    a = a//2
    while a != 0 :
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a

if __name__ == '__main__':
    from doctest import testmod
    testmod()