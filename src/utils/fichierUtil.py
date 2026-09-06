from utils import csvUtil, xmlUtil


def choix_recuperation_donnees_fichier():
    """Fonction permettant à l'utilisateur de sélectionner le fichier depuis lequel les données sont récupérées

    Returns:
        list: Liste des objets Anime
    """
    choix_utilisateur = ""
    fichier = ""

    # Boucle de choix
    while choix_utilisateur != "1" and choix_utilisateur != "2":
        # Menu de sélection
        print("Depuis quel type de fichier souhaitez-vous récupérer les données ?\n")
        print("1. Fichier xml")
        print("2. Fichier csv")
        # Récupération du choix de l'utilisateur
        choix_utilisateur = input("Votre choix : ")

    # Cas où l'utilisateur veut récupérer depuis un fichier xml
    if choix_utilisateur == "1":
        fichier = input("Entrez le nom du fichier : ")
        fichier = fichier + ".xml"
        animes = xmlUtil.recupere_donnees_xml(fichier)
        return animes

    # Cas où l'utilisateur veut récupérer depuis un fichier csv
    if choix_utilisateur == "2":
        fichier = input("Entrez le nom du fichier : ")
        fichier = fichier + ".csv"
        animes = csvUtil.recupere_donnees_csv(fichier)
        return animes
