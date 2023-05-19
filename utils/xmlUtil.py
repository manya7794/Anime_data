import xml.etree.ElementTree as et


def recupere_donnees_xml(fichier_xml, liste_anime):
    """Cette fonction récupère les éléments spécifiés en argument dans le fichier XML

    Args:
        fichier_xml(String): Nom du fichier XML
        liste_anime(listeAnime):Liste allant contenir tous les animes et leurs attributs
    """
    # Récupération du nom du fichier
    tree = et.parse(fichier_xml)

    # Récupération de la racine
    root = tree.getroot()

    # Récupération de tous les noms dans une liste
    for titre in root.iter("series_title"):
        liste_anime.nom.append(titre.text)

    # Récupération de tous les identifiants dans une liste
    for identifiant in root.iter("series_animedb_id"):
        liste_anime.id.append(identifiant.text)

    # Récupération de toutes les notes dans une liste
    for note in root.iter("my_score"):
        liste_anime.score.append(note.text)

    # Récupération de tous les statuts de visionnage dans une liste
    for statut in root.iter("my_status"):
        liste_anime.etat.append(statut.text)
