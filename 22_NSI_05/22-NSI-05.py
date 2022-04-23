def RechercheMinMax(tab: list) -> dict:
    if(tab == []): return {'min': None, 'max': None}
    dico = {'min': tab[0],
            'max': tab[0]}
    
    for elt in tab:
        if(dico['min'] > elt): dico['min'] = elt
        elif(dico['max'] < elt): dico['max'] = elt

class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10, 
       Valet, Dame, Roi"""
    def getNom(self):
        """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    def getCouleur(self):
        
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    """Remplit le paquet de cartes"""
    def remplir(self):
        for k in range(1, 5):
            for i in range(1, 14):
                self.contenu.append(Carte(k, i))
        
    def getCarteAt(self, pos):
        """Renvoie la Carte qui se trouve à la position donnée"""
        return self.contenu[pos]