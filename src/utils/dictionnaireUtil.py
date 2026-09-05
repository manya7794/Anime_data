from utils.apiUtil import recupere_annee_sortie_api_mal
from progressbar import ProgressBar

pbar = ProgressBar()


def ajout_theme(dict_themes, theme_cherche):
    """Ajout du theme si celui n'existe pas dans le dictionnaire

    Args:
        dict_themes (dict): Dictionnaire contenant les thèmes et leur fréquence
        theme_cherche (String): Thème à ajouter dans le dictionnaire
    """
    if theme_cherche in dict_themes:
        # Augmentation de la fréquence d'apparition du theme
        dict_themes[theme_cherche] += 1
    else:
        # Création du theme
        dict_themes[theme_cherche] = 1


def ajout_note(notes, dict_notes):
    """Ajout de la note si celle-ci n'existe pas dans le dictionnaire

    Args:
        notes (list): Liste des notes à ajouter dans le dictionnaire
        dict_notes (dict): Dictionnaire contenant les notes et leur fréquence
    """
    # Parcours de la liste des notes
    for note in notes:
        if str(note) in dict_notes:
            dict_notes[str(note)] += 1


def ajout_statut(statuts, dict_statuts):
    """Ajout du theme si celui-ci n'existe pas dans le dictionnaire sinon augmente de 1 la fréquence

    Args:
        statuts (list): Liste des thèmes à ajouter dans le dictionnaire
        dict_statuts (dict): Dictionnaire contenant les thèmes et leurs fréquence
    """

    # Parcours de la liste des statuts
    for statut in statuts:
        if statut in dict_statuts:
            dict_statuts[statut] += 1
        else:
            dict_statuts[statut] = 1


def ajout_annee_sortie(liste_id, dict_annees):
    """Ajout de l'année de sortie si celle-ci n'existe pas dans le dictionnaire sinon augmente de 1 la fréquence

    Args:
        liste_id (list): Liste des id d'animes à vérifier
        dict_annees (dict): Dictionnaire contenant les années et leurs fréquence
    """
    # Parcours de la liste des identifiants
    for identifiant in pbar(liste_id):
        annee = recupere_annee_sortie_api_mal(identifiant)

        # Ajustement de la fréquence de l'année dans le  dictionnaire
        if annee in dict_annees:
            dict_annees[annee] += 1
        else:
            dict_annees[annee] = 1
