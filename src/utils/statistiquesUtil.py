import pandas as pd
from utils import themeUtil
from utils.apiUtil import recupere_annee_sortie_api_mal


def calcule_notes(animes):
    """Calcule la fréquence des notes d'une liste d'animes.

    Args:
        animes (list): Liste des animes

    Returns:
        dict: Dictionnaire contenant les notes et leur fréquence
    """
    dict_notes = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
    }

    # Récupération des scores des animes
    scores = [anime.score for anime in animes]

    # Parcours de la liste des notes
    for score in scores:
        if str(score) in dict_notes:
            dict_notes[str(score)] += 1

    return dict_notes


def calcule_statuts(animes):
    """Calcule la fréquence des statuts d'une liste d'animes.

    Args:
        animes (list): Liste des animes

    Returns:
        dict: Dictionnaire contenant les statuts et leur fréquence
    """
    dict_statuts = {}

    # Récupération des statuts des animes
    statuts = [anime.etat for anime in animes]

    # Parcours de la liste des statuts
    for statut in statuts:
        if statut in dict_statuts:
            dict_statuts[statut] += 1
        else:
            dict_statuts[statut] = 1

    return dict_statuts


def calcule_themes(animes):
    """Calcule la fréquence des thèmes d'une liste d'animes.
    Args:
        animes (list): Liste des animes

    Returns:
        dict: Dictionnaire contenant les thèmes et leur fréquence
    """
    # Récupération des identifiants des animes
    ids = [anime.id for anime in animes]

    return themeUtil.recupere_themes_from_list(ids)


def calcule_annees_sortie(animes):
    """Calcule la fréquence des années de sortie d'une liste d'animes.

    Args:
        animes (list): Liste des animes

    Returns:
        dict: Dictionnaire contenant les années et leur fréquence
    """
    dict_annees = {}

    # Récupération des identifiants des animes
    ids = [anime.id for anime in animes]

    # Parcours de la liste des identifiants
    for identifiant in ids:
        annee = recupere_annee_sortie_api_mal(identifiant)

        # Ajustement de la fréquence de l'année dans le dictionnaire
        if annee in dict_annees:
            dict_annees[annee] += 1
        else:
            dict_annees[annee] = 1

    return dict_annees


def create_dataframe_notes(score_id, score_frequence):
    """Cette fonction génère un dataframe à partir des score attribuées à chaque anime

    Args:
        score_id (list): Liste des scores des animes
        score_frequence (list): Liste des fréquences de chaque score

    Returns:
        notes_dataframe: Dataframe contenant les notes et leur fréquence
    """
    notes_dataframe = pd.DataFrame({"Notes": score_id, "Frequence": score_frequence})
    return notes_dataframe


def create_dataframe_statut(statuts, statuts_frequence):
    """Cette fonction génère un dataframe à partir des statuts de visionnage de chaque anime

    Args:
        statuts (List): Liste des statuts des animes
        statuts_frequence (List): Liste des fréquences de chaque statut

     Returns:
        dataframe: Dataframe contenant les statuts et leur fréquence
    """
    statut_dataframe = pd.DataFrame({"Statut": statuts, "Frequence": statuts_frequence})
    return statut_dataframe


def create_dataframe_annees_sorties(annees, annees_frequence):
    """Cette fonction génère un dataframe à partir des années de sortie des animes

    Args:
        annees (List): Liste des années et leur fréquence

    Returns:
        dataframe: Dataframe contenant les années et leur fréquence
    """
    annees_sortie_dataframe = pd.DataFrame(
        {"Annee": annees, "Frequence": annees_frequence}
    )
    return annees_sortie_dataframe
