def recherche(a, t):
    assert isinstance(a, int) or isinstance(a, float), 'La variable a doit être soit un int ou un float'
    assert isinstance(t, list), 'La variable t doit être une liste'
    
    final = 0
    for elt in t:
        if(elt == a): final += 1
    return final

# Exercice 1 en deux minutes


def rendu_monnaie_centimes(s_due, s_versee):
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = []
    a_rendre = s_versee - s_due
    i = len(pieces) - 1
    while a_rendre > s_versee :
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre = a_rendre - pieces[i]
        else :
            i = i - 1
    return rendu
