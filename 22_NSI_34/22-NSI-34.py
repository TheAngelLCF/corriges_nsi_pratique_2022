# Thuillier Valentin

def occurence_max(chaine: str) -> str:
    assert isinstance(chaine, str), 'Merci de mettre un paramètre un string !'
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o,','p','q','r','s','t','u','v','w','x','y','z']
    occurence = [0] * 26
    for elt in chaine:
        if(elt in alphabet):
             occurence[alphabet.index(elt)] += 1
    
    rang = 0
    maxi = 0
    
    for k in range(len(occurence)):
        if(occurence[k] > maxi):
            rang = k
            maxi = occurence[k]
            
    return alphabet[rang]


# Exercice 1 en 6 minutes

def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le negatif de l'image sous la forme 
       d'une liste de listes'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] 
# on cree une image de 0 aux memes dimensions que le parametre image 
    for i in range(len(image)):
        for j in range(len(image[0])):
            L[i][j] = 255 - image[i][j]
    return L

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme 
       d'une liste de listes contenant des 0 si la valeur 
       du pixel est strictement inferieure au seuil 
       et 1 sinon'''
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] # on cree une image de 0 aux memes dimensions que le parametre image 
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] < seuil :
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L

# Exercice 2 en 7 minutes

# Erreur sur le sujet,
# binaire(img,120), la valeur retourner indiquer à un problème, elle retourne l'inverse de ce qu'elle devrait retourner !
# Je pense qu'il ont inquiet en paramètre que img = negatif(img)