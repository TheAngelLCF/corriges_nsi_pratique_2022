def mini(releve: list, date: list):
    """
    >>> t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
    >>> annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
    >>> mini(t_moy, annees)
    (12.5, 2016)
    """
    assert len(releve) == len(date), "Releve et date incompatible !"
    minn = 0
    for k in range(len(releve)):
        if(releve[k] < releve[minn]): minn = k
    return releve[minn], date[minn]

def inverse_chaine(chaine):
    result = ''
    for caractere in chaine:
       result = caractere + result 
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return inverse == chaine
    
def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)

if __name__ == '__main__':
    from doctest import testmod
    testmod()