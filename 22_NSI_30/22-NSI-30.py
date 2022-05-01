def fusion(tab1: list, tab2: list) -> list:
    final = []
    while tab1 != [] and tab2 != []:
        if(tab1[0] < tab2[0]): final.append(tab1.pop(0))
        else: final.append(tab2.pop(0))
    if(tab1 != []):
        for elt in tab1:
            final.append(elt)
    if(tab2 != []):
        for elt in tab2:
            final.append(elt)
    return final
        
def rom_to_dec (nombre):

    """ Renvoie l’écriture décimale du nombre donné en chiffres romains """

    dico = {"I":1, "V":5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if len(nombre) == 1:
        return dico[nombre]

    else:
        ### on supprime le premier caractère de la chaîne contenue dans la variable nombre
         ### et cette nouvelle chaîne est enregistrée dans la variable nombre_droite
        nombre_droite = nombre[1:]
    
        
        if dico[nombre[0]] >= dico[nombre[1]]:
            return dico[nombre[0]] + rom_to_dec(nombre_droite)
        else:
            return rom_to_dec(nombre_droite) - dico[nombre[0]]

assert rom_to_dec("CXLII") == 142
