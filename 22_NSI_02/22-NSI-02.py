def moyenne(tab: list) -> float:
    final = 0
    diviseur = 0
    for elt in tab:
        assert isinstance(elt, tuple) and len(elt) == 2
        assert isinstance(elt[0], int) and elt[0] >= 0 and elt[0] <= 20
        assert isinstance(elt[1], int) and elt[1] >= 0
        final += elt[0] * elt[1]
        diviseur += elt[1]
    return final / diviseur


def pascal(n):
    C= [[1]]
    for k in range(1,n + 1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C
