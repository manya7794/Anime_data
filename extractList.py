import pandas as pd
import xml.etree.ElementTree as et


def recupFichier(nom, id, score, etat):
    """Cette fonction récupère les éléments spécifiés en argument dans le fichier

    Args:
        nom (list): Liste des noms des animes
        id (list): Liste des id des animes
        score (list): Liste des scores des animes
        etat (list): Liste des états de visionnages des animes
    """

    # Récupération du nom du fichier
    tree = et.parse("animelist.xml")

    # Récupération de la racine
    root = tree.getroot()

    # Récupération de tous les noms dans une liste
    for titre in root.iter("series_title"):
        # print(identifiant.text)
        nom.append(titre.text)

    # Récupération de tous les identifiants dans une liste
    for identifiant in root.iter("series_animedb_id"):
        # print(identifiant.text)
        id.append(identifiant.text)

    # Récupération de toutess les notes dans une liste
    for note in root.iter("my_score"):
        score.append(note.text)

    # Récupération de tous les statuts de visionnage dans une liste
    for statut in root.iter("my_status"):
        etat.append(statut.text)

    return (nom, id, score, etat)


def createDataFrame(nom, id, score, etat):
    """Cette fonction génère un dataframe à partir des listes passées en argument

    Args:
        nom (list): Liste des noms des animes
        id (list): Liste des id des animes
        score (list): Liste des scores des animes
        etat (list): Liste des états de visionnages des animes
    """
    # Création d'une dataframe
    anime_df = pd.DataFrame(
        list(zip(nom, id, score, etat)),
        columns=["Numero", "Nom", "Identifiant", "Note", "Statut"],
    )


def saveCSV(dataframe):
    """Cette fonction génère un fichier CSV à partir du dataframe

    Args:
        dataframe (DataFrame): DataFrame simplifié des animes récupérés depuis le XML
    """
    # Sauvegarde du dataframe au format CSV
    dataframe.to_csv("animelist.csv")
