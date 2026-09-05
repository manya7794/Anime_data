import xml.etree.ElementTree as et

from models.anime import Anime


def recupere_donnees_xml(fichier_xml):
    """Cette fonction récupère les éléments spécifiés en argument dans le fichier XML

    Args:
        fichier_xml(String): Nom du fichier XML

    Returns:
        list: Liste des objets Anime
    """
    # Récupération du nom du fichier
    tree = et.parse(fichier_xml)

    # Récupération de la racine
    root = tree.getroot()

    # Liste des animes
    animes = []

    # Récupération des données de chaque anime
    for anime_xml in root.findall("anime"):
        # Récupération du nom
        titre = anime_xml.find("series_title")

        # Récupération de l'identifiant
        identifiant = anime_xml.find("series_animedb_id")

        # Récupération de la note
        note = anime_xml.find("my_score")

        # Récupération du statut de visionnage
        statut = anime_xml.find("my_status")

        # Création de l'anime
        anime = Anime(
            nom=titre.text,
            id=identifiant.text,
            score=note.text,
            etat=statut.text,
        )

        # Ajout de l'anime à la liste
        animes.append(anime)

    return animes
