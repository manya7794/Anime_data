import pandas as pd
import xml.etree.ElementTree as et
import csv


def choix_recuperation_donnees(nom, id, score, etat):
    """Fonction permettant à l'utilisateur de sélectionner le fichier depuis lequel les données sont récupérées

    Args:
        nom (list): Liste des noms des animes
        id (list): Liste des id des animes
        score (list): Liste des scores des animes
        etat (list): Liste des états de visionnages des animes
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
        recupere_donnees_xml(fichier, nom, id, score, etat)

    # Cas où l'utilisateur veut récupérer depuis un fichier csv
    if choix_utilisateur == "2":
        fichier = input("Entrez le nom du fichier : ")
        fichier = fichier + ".csv"
        recupere_donnees_csv(fichier, nom, id, score, etat)


def recupere_donnees_xml(fichier_xml, nom, id, score, etat):
    """Cette fonction récupère les éléments spécifiés en argument dans le fichier XML

    Args:
        fichier_xml(String): Nom du fichier XML
        nom (list): Liste des noms des animes
        id (list): Liste des id des animes
        score (list): Liste des scores des animes
        etat (list): Liste des états de visionnages des animes
    """
    # Récupération du nom du fichier
    tree = et.parse(fichier_xml)

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


def recupere_donnees_csv(fichier_csv, nom, id, score, etat):
    """Cette fonction récupère les éléments spécifiés en argument dans le fichier XML

    Args:
        fichier_csv(String): Nom du fichier csv
        nom (list): Liste des noms des animes
        id (list): Liste des id des animes
        score (list): Liste des scores des animes
        etat (list): Liste des états de visionnages des animes
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
                nom.append(colonne[1])
                id.append(colonne[2])
                score.append(colonne[3])
                etat.append(colonne[4])
                # Passage à la ligne suivante
                ligne += 1

        return (nom, id, score, etat)


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
            create_data_frame(nom, id, score, etat)


def create_data_frame(nom, id, score, etat):
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
    sauvegarde_csv(anime_dataframe)


def sauvegarde_csv(dataframe):
    """Cette fonction génère un fichier CSV à partir du dataframe

    Args:
        dataframe (DataFrame): DataFrame simplifié des animes récupérés depuis le XML
    """
    # Sauvegarde du dataframe au format CSV
    nom_csv = input("Entrez le nom du fichier .CSV à sauvegarder : ")
    nom_csv = nom_csv + ".csv"
    dataframe.to_csv(nom_csv)
