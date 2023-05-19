import csv


def recupere_donnees_csv(fichier_csv, liste_anime):
    """Cette fonction récupère les éléments spécifiés en argument dans le fichier csv

    Args:
        fichier_csv(String): Nom du fichier csv
        liste_anime(listeAnime):Liste allant contenir tous les animes et leurs attributs
    """
    # Ouverture du fichier en lecture
    with open(fichier_csv) as fichier:
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
                liste_anime.nom.append(colonne[1])
                liste_anime.id.append(colonne[2])
                liste_anime.score.append(colonne[3])
                liste_anime.etat.append(colonne[4])
                # Passage à la ligne suivante
                ligne += 1
