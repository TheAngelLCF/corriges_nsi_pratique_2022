# Thuillier Valentin

def moyenne(tab):
    '''
        moyenne(list) -> float
        Entrée : un tableau non vide d'entiers
        Sortie : nombre de type float
        Correspondant à la moyenne des valeurs présentes dans le
        tableau
    '''
    assert len(tab) != [], 'Le tableau mit en paramètre est vide !'
    total = 0
    for elt in tab:
        assert isinstance(elt, int), 'L\élement "' + str(elt) + '" n\'est pas un entier !'
        total += elt
    return total / len(tab)    


def dichotomie(tab, x):
    """
        tab : tableau trie dans l'ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if not(len(tab)):
        return False,1

    # cas ou x n'est pas compris entre les valeurs extremes
    if (x < tab[0]) or (x > tab[-1]):
        return False,2
    
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = debut + ((fin - debut) // 2)
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return (False, 3)

# En 20 minutes

# Erreur sur le premier exercice ddans l'énoncé, impossible de renvoyer un int pourtant l'assert de l'énoncé fait == 1 et == 4