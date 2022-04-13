def iteration_frequence_theme(dico, theme_cherche):
    """Augmente la fréquence d'apparition du thême cherché passé en argument

    Args:
        dico (dict): Dictionnaire contenant les thèmes et leur fréquence
        theme_cherche (String): Clé du theme recherché
    """
    for key in dico.keys():
        if key == theme_cherche:
            dico[key] += 1


def ajout_theme(dico, theme_cherche):
    """Ajout du theme si celui n'existe pas dans le dictionnaire

    Args:
        dico (dict): Dictionnaire contenant les thèmes et leur fréquence
        theme_cherche (String): Thême à ajouter dans le dictionnaire
    """
    # Booléen vérifiant l'existence de l'theme_cherche
    existe = False

    for theme in dico:
        if theme == theme_cherche:
            # Cas où le thème est présent dans le dictionnaire
            existe = True
            # Augmentation de la fréquence d'apparition du theme
            iteration_frequence_theme(dico, theme_cherche)
            break
    # Cas où le thème n'est pas présent dans le dictionnaire
    if existe is False:
        # Création du theme
        dico[theme_cherche] = 1
