def recherche(tab: list, n: int):
    """
    Exemples:
    >>> recherche([2, 3, 4, 5, 6], 5)
    3
    >>> recherche([2, 3, 4, 6, 7], 5)
    -1
    """
    debut = 0
    fin = len(tab)
    while debut < fin:
        mediane = (fin + debut) // 2
        if(tab[mediane] == n):
            return mediane
        elif(tab[mediane] > n):
            fin = mediane - 1
        else:
            debut = mediane
    return -1

ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    """
    Exemples :
    >>> cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !',4)
    'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
    >>> cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !',-5)
    'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
    """
    resultat = ''
    for lettre in message :
        if lettre in ALPHABET :
            indice = ( position_alphabet(lettre) + decalage )%26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + lettre
    return resultat

if __name__ == '__main__':
    from doctest import testmod
    testmod()