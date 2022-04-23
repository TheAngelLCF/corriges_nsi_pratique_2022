from random import randint

def tri_selection(tab: list) -> list:
    rang = 0
    final = tab.copy()
    while rang < len(tab):
        minn = rang
        for k in range(rang, len(final)):
            if(final[minn] > final[k]): minn = k
        final[minn], final[rang] = final[rang], final[minn]
        rang += 1
        
    return final
    
    
    
def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1

    while nb_mystere != nb_test and compteur < 10 :
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre etait ", nb_test)
        print("Nombre d'essais: ", compteur)
    else:
        print ("Perdu ! Le nombre etait ", nb_test)
