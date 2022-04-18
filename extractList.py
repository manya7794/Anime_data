import pandas as pd
import xml.etree.ElementTree as et
import csv


def choix_recuperation_donnees(liste_anime):
    """Fonction permettant à l'utilisateur de sélectionner le fichier depuis lequel les données sont récupérées

    Args:
        liste_anime(listeAnime):Liste allant contenir tous les animes et leurs attributs
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
        recupere_donnees_xml(fichier, liste_anime)

    # Cas où l'utilisateur veut récupérer depuis un fichier csv
    if choix_utilisateur == "2":
        fichier = input("Entrez le nom du fichier : ")
        fichier = fichier + ".csv"
        recupere_donnees_csv(fichier, liste_anime)


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
        # print(identifiant.text)
        liste_anime.nom.append(titre.text)

    # Récupération de tous les identifiants dans une liste
    for identifiant in root.iter("series_animedb_id"):
        # print(identifiant.text)
        liste_anime.id.append(identifiant.text)

    # Récupération de toutess les notes dans une liste
    for note in root.iter("my_score"):
        liste_anime.score.append(note.text)

    # Récupération de tous les statuts de visionnage dans une liste
    for statut in root.iter("my_status"):
        liste_anime.etat.append(statut.text)


def recupere_donnees_csv(fichier_csv, liste_anime):
    """Cette fonction récupère les éléments spécifiés en argument dans le fichier XML

    Args:
        fichier_csv(String): Nom du fichier csv
        liste_anime(listeAnime):Liste allant contenir tous les animes et leurs attributs
    """
    # Ouverture du fichier en lecture
    with open(fichier_csv) as fichier:
        csv_reader = csv.reader(fichier, delimiter=",")
        # Initialisation de la ligne
        ligne = 0
        # Initiliasition de la lecture des colonnes
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


def sauvegarde_liste(nom, id, score, etat):
    """Cette fonction permet d'initialiser la demande de sauvegarde de la liste

    Args:
        nom (list): Liste des noms des animes
        id (list): Liste des id des animes
        score (list): Liste des scores des animes
        etat (list): Liste des états de visionnages des animes
    """
    choix_sauvegarde = ""
    # Boucle de choix
    while choix_sauvegarde != "Y" and choix_sauvegarde != "N":
        # Récupération du choix de l'utilisateur
        choix_sauvegarde = input("Voulez-vous sauvegarder au format CSV ? (Y/N) \n")
        # Cas où l'utilisateur choisit de sauvegarder
        if choix_sauvegarde == "Y":
            anime_dataframe = create_dataframe_liste(nom, id, score, etat)
            sauvegarde_csv(anime_dataframe)


def create_dataframe_liste(nom, id, score, etat):
    """Cette fonction génère un dataframe à partir des listes passées en argument

    Args:
        nom (list): Liste des noms des animes
        id (list): Liste des id des animes
        score (list): Liste des scores des animes
        etat (list): Liste des états de visionnages des animes
    """
    # Création d'une dataframe
    anime_dataframe = pd.DataFrame(
        list(zip(nom, id, score, etat)),
        columns=["Nom", "Identifiant", "Note", "Statut"],
    )
    # Sauvegarde de la dataframe au format CSV
    return anime_dataframe


def create_dataframe_notes(score_id, score_frequence):
    """Cette fonction génère un dataframe à partir des score attribuées à chaque anime

    Args:
        score (list): Liste des scores des animes
    """
    notes_dataframe = pd.DataFrame({"Notes": score_id, "Frequence": score_frequence})
    return notes_dataframe


def sauvegarde_csv(dataframe):
    """Cette fonction génère un fichier CSV à partir du dataframe

    Args:
        dataframe (DataFrame): DataFrame simplifié des animes récupérés depuis le XML
    """
    # Sauvegarde du dataframe au format CSV
    nom_csv = input("Entrez le nom du fichier .CSV à sauvegarder : ")
    nom_csv = nom_csv + ".csv"
    dataframe.to_csv(nom_csv)


def extraire_nouvelle_liste_personnalisee(liste_anime):
    """Cette fonction extrait une nouvelle liste d'animes dont l'état correspond au choix de l'utilisateur

    Args:
        liste_anime (listeAnime): Liste d'animes depuis laquelle l'utilisateur souhaite extraire ceux possédant
        tous le même état

    Returns:
        listeAnime: Nouvelle liste d'animes dont les états correspondent au choix de l'utilisateur
    """
    # Initialisation du choix de l'utilisateur
    choix_utilisateur = ""
    while choix_utilisateur != "Y" and choix_utilisateur != "N":
        # Récupération du choix de l'utilisateur
        choix_utilisateur = input(
            "Voulez-vous charger des animes dans une autre liste ? (Y/N)\n"
        )
        # Cas où l'utilisateur choisit de créer une nouvelle liste
        if choix_utilisateur == "Y":
            while (
                choix_utilisateur != "1"
                and choix_utilisateur != "2"
                and choix_utilisateur != "3"
                and choix_utilisateur != "4"
                and choix_utilisateur != "5"
            ):
                # Choix du type d'animes à sélectionner dans la liste
                print("Quel type d'animes voulez-vous sélectionner ?")
                print("1 : Animes en cours de visionnage")
                print("2 : Animes finis")
                print("3 : Animes en pause")
                print("4 : Animes abandonnés")
                print("5 : Animes à regarder plus tard")
                choix_utilisateur = input()

            # Animes en cours de visionnage
            if choix_utilisateur == "1":
                liste_animes = liste_anime.recupere_animes_selon_statut("Watching")
            # Animes finis
            if choix_utilisateur == "2":
                liste_animes = liste_anime.recupere_animes_selon_statut("Completed")
            # Animes en pause
            if choix_utilisateur == "3":
                liste_animes = liste_anime.recupere_animes_selon_statut("On-Hold")
            # Animes abandonnés
            if choix_utilisateur == "4":
                liste_animes = liste_anime.recupere_animes_selon_statut("Dropped")
            # Animes à regarder plus tard
            if choix_utilisateur == "5":
                liste_animes = liste_anime.recupere_animes_selon_statut("Plan to Watch")

            # Renvoi de la nouvelle liste personnalisée
            return liste_animes

        # Cas où l'utilisateur choisit de ne pas créer de nouvelle liste
        if choix_utilisateur == "N":
            return None
