import csv

from models.anime import Anime


def recupere_donnees_csv(fichier_csv):
    """Cette fonction récupère les éléments spécifiés en argument dans le fichier csv

    Args:
        fichier_csv(String): Nom du fichier csv

    Returns:
        list: Liste des objets Anime
    """
    # Liste des animes
    animes = []

    # Ouverture du fichier en lecture
    with open(fichier_csv, encoding="utf-8") as fichier:
        csv_reader = csv.reader(fichier, delimiter=",")
        # Initialisation de la ligne
        ligne = 0
        # Initialisation de la lecture des colonnes
        for colonne in csv_reader:
            # Lecture de l'en-tête
            if ligne == 0:
                print(f"Les colonnes sont les suivantes{', '.join(colonne)}")
                # Passage à la ligne suivante
                ligne += 1
            # Lecture des lignes du document
            else:
                # Récupération des différentes données
                anime = Anime(
                    nom=colonne[1],
                    id=colonne[2],
                    score=colonne[3],
                    etat=colonne[4],
                )

                # Ajout de l'anime à la liste
                animes.append(anime)

                # Passage à la ligne suivante
                ligne += 1

    return animes
