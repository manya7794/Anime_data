dico={}

def iterFrequence(dico, objet):
    """Augmente la fréquence d'apparition de l'objet passé en argument

    Args:
        dico (dict): Dictionnaire contenant les thèmes et leur fréquence
        objet (String): Clé de l'objet 
    """
    for key in dico.keys():
        if key==objet:
            dico[key]+=1

def ajoutTheme(dico,objet):
    """Ajout du theme si celui n'existe pas dans le dictionnaire

    Args:
        dico (dict): Dictionnaire contenant les thèmes et leur fréquence
        objet (String): Theme à ajouter dans le dictionnaire
    """
    #Booléen vérifiant l'existence de l'objet
    existe=False

    for key in dico:
        if key==objet:
            #Cas où le thème est présent dans le dictionnaire
            existe=True
            #Augmentation de la fréquence d'apparition du theme
            iterFrequence(dico, objet)
            break
    #Cas où le thème n'est pas présent dans le dictionnaire
    if existe==False:
        #Création du theme
        dico[objet]=1
