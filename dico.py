from operator import truediv
from extractList import recupere_annee_sortie_api
from progressbar import ProgressBar

pbar = ProgressBar()


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
    # Booléen vérifiant l'existence de theme_cherche
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


def ajout_note(notes, dico_notes):
    """Ajout de la note si celle-ci n'existe pas dans le dictionnaire

    Args:
        notes (list): Liste des notes à ajouter dans le dictionnaire
        dico (dict): Dictionnaire contenant les notes et leur fréquence
    """
    # Parcours de la liste des notes
    for note in notes:

        # Parcours du dictionnaire contenant toutes les notes
        for key in dico_notes.keys():
            if key == str(note):
                dico_notes[key] += 1


def ajout_statut(statuts, dico_statuts):
    """Ajout du theme si celui-ci n'existe pas dans le dictionnaire sinon augmente de 1 la fréquence

    Args:
        statuts (list): Liste des thèmes à ajouter dans le dictionnaire
        dico_statuts (dict): Dictionnaire contenant les thèmes et leurs fréquence
    """

    # Parcours de la liste des statuts
    for statut in statuts:

        if statut in dico_statuts:
            dico_statuts[statut] += 1
        else:
            dico_statuts[statut] = 1


def ajout_annee_sortie(liste_id, dico_annees):
    """Ajout de l'année de sortie si celle-ci n'existe pas dans le dictionnaire sinon augmente de 1 la fréquence

    Args:
        annees (list): Liste des années à ajouter dans le dictionnaire
        dico_annees (dict): Dictionnaire contenant les années et leurs fréquence
    """
    # Parcours de la liste des identifiants
    for identifiant in pbar(liste_id):
        annee = recupere_annee_sortie_api(identifiant)

        # Ajustement de la fréquence de l'année dans le  dictionnaire
        if annee in dico_annees:
            dico_annees[annee] += 1
        else:
            dico_annees[annee] = 1
