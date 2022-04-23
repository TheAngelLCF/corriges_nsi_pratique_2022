def correspond(mot: str, mot_a_trous: str) -> bool:
    final = ''
    if(len(mot) != len(mot_a_trous)): return False
    for rang in range(len(mot)):
        if(mot_a_trous[rang] == '*'): final += mot[rang]
        else: final += mot_a_trous[rang]
    return mot == final

def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant 
    à un plan d'envoi de messages entre `N` personnes A, B, C, 
    D, E, F ...(avec N <= 26).
    Renvoie True si le plan d'envoi de messages est cyclique
    et False sinon. 
    '''
    personne = 'A'
    N = len(plan)                          
    for i in range(N - 1):
        if plan[personne] == 'A':
            return False
        else:
            personne = plan[personne]
    return True