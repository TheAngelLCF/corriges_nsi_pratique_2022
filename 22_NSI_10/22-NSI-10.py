def occurence_lettres(phrase: str):
    dico = {}
    for elt in phrase:
        if(elt not in list(dico.keys())):
            dico[elt] = 1
        else:
            dico[elt] += 1
    return dico

# A faire plus tard

# def fusion(L1,L2):
#     n1 = len(L1)
#     n2 = len(L2)
#     L12 = [0]*(n1+n2)
#     i1 = 0
#     i2 = 0
#     i = 0
#     while i1 < n1 and i2 < n2 :
#         if L1[i1] < L2[i2]:
#             L12[i] = ...
#             i1 = ...
#         else:
#             L12[i] = L2[i2]
#             i2 = ...
#         i += 1
#     while i1 < n1:
#         L12[i] = ...
#         i1 = i1 + 1
#         i = ...
#     while i2 < n2:
#         L12[i] = ...
#         i2 = i2 + 1
#         i = ...
#     return L12
