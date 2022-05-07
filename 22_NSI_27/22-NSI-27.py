def taille(arbre: dict, lettre: str) -> int: # Version sans: On pourra distinguer les 4 cas où les deux « fils » du nœud sont '', le fils gauche seulement est '', le fils droit seulement est '', aucun des deux fils n’est ''. 
    if(lettre == ""): return 0
    if(arbre[lettre] == ["", ""]):
        return 1
    else:
        gauche = arbre[lettre][0]
        droite = arbre[lettre][1]
        return 1 + taille(arbre, gauche) + taille(arbre, droite)
    
def taille_2(arbre: dict, lettre: str) -> int: # Version avec
    if(arbre[lettre] == ["", ""]): return 1
    elif(arbre[lettre][0] == "" and arbre[lettre][1] != ""): return 1 + taille(arbre, arbre[lettre][1])
    elif(arbre[lettre][1] == "" and arbre[lettre][0] != ""): return 1 + taille(arbre, arbre[lettre][0])
    else: return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])

def tri_iteratif(tab):
    for k in range( len(tab) - 1 , 0, -1):
        imax = 0
        for i in range(0 , k ):
            if tab[i] > tab[imax] :
                imax = i
        if tab[imax] > tab[k] :
            tab[k] , tab[imax] = tab[imax] , tab[k]
    return tab

if __name__ == "__main__":
    a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'],'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}
