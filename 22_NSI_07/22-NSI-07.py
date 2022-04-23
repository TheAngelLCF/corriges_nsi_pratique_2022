def conv_bin(n: int) -> tuple:
    assert n >= 0, "Merci de spécifier une valeur entière positive !"
    final = []
    while n != 0:
        final.append(n % 2)
        n = n // 2
    final.reverse()
    return (final, len(final))


def tri_bulles(T):
    n = len(T)
    for i in range(n - 1,0,-1):
        for j in range(i):
            if T[j] > T[i]:
                temp = T[j]
                T[j] = T[i - 1]
                T[j+1] = temp
    return T
