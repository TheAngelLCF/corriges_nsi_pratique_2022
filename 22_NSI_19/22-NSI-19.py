def multiplication(n1: int, n2: int) -> int:
    somme = 0
    if n1 == 0 or n2 == 0:
        return 0
    if n1 < 0:
        return -multiplication(-n1, n2)
    if n2 < 0:
        return -multiplication(n1, -n2)
    for i in range(n2):
        somme += n1
    return somme

def chercher(T,n,i,j):
    if i < 0 or j >= len(T) :
        print("Erreur")
        return None    
    if i > j :
        return None
    m = (i+j) // 2
    if T[m] < n :
        return chercher(T, n, m+1, j)
    elif T[m] > n :
        return chercher(T, n, i, m-1)
    else :
        return m
