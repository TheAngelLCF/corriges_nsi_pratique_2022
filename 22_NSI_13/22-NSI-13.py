def rendu(somme_a_rendre: int):
    monnaie = [5, 2, 1]
    final = [0, 0, 0]
    rang = 0
    while somme_a_rendre != 0:
        if(somme_a_rendre - monnaie[rang] < 0):
            rang += 1
        else:
            somme_a_rendre -= monnaie[rang]
            final[rang] += 1
    return final

class Maillon :
    def __init__(self,v) :
        self.valeur = v
        self.suivant = None

class File :
    def __init__(self) :
        self.dernier_file = None

    def enfile(self,element) :
        nouveau_maillon = Maillon(element) 
        nouveau_maillon.suivant = self.dernier_file
        self.dernier_file = nouveau_maillon

    def est_vide(self) :
        return self.dernier_file == None

    def affiche(self) :
        maillon = self.dernier_file
        while maillon != None :
            print(maillon.valeur)
            maillon = maillon.suivant

    def defile(self) :
        if not self.est_vide() :
            if self.dernier_file.suivant == None :
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = self.dernier_file
            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = maillon.suivant.valeur
            maillon.suivant = None
            return resultat
        return None 

if __name__ == '__main__':
    F = File()
    print(F.est_vide())
    F.enfile(2)
    F.affiche()
    print(F.est_vide())
    F.enfile(5)
    F.enfile(7)
    F.affiche()
    print(F.defile())
    print(F.defile())
    print(F.defile())