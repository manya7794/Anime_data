import json
import pandas as pd
import xml.etree.ElementTree as et
import csv
import requests
from config import api_key


def choix_recuperation_donnees_fichier(liste_anime):
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


def choix_recuperation_donnees_api(liste_anime, lien_api=None, params=None):
    """Fonction permettant à l'utilisateur de sélectionner les animes qu'il souhaite récupérer selon leur statut

    Args:
        liste_anime (listeAnime): Liste allant contenir tous les animes et leurs attributs
        lien_api (String, optional): Lien de l'API. Defaults to None.
        params (dict, optional): Paramètres de sélection. Defaults to None.
    """
    # Clé d'API
    headers = {
        "X-MAL-CLIENT-ID": api_key,
    }

    # Paramètres de sélection
    if params is not None and params is True:
        params = {"offset": "0", "fields": "list_status"}

    # Lien de l'API
    if lien_api is None:
        # Récupération du nom de l'utilisateur à rechercher
        user_name = input("Entrez le nom de l'utilisateur :")
        # Création du lien de l'api
        lien_api = f"https://api.myanimelist.net/v2/users/{user_name}/animelist"

    # Création de la requête vers l'API
    reponse = requests.get(
        # Adresse de la demande
        lien_api,
        # Ajout des headers
        headers=headers,
        # Ajout des paramètres
        params=params,
    )

    # Convertit la réponse en fichier json
    reponse_json = reponse.json()

    # Ajout des animes à la liste d'anime
    recupere_donnees_api(reponse_json, liste_anime)

    # Parcours des pages suivantes
    pagination = reponse_json["paging"]
    # Récupération du lien vers la liste suivante
    if "next" in pagination:
        # Recupération du lien nettoyé
        lien_page_suivante = pagination["next"]

        # Appel récursif de la fonction
        choix_recuperation_donnees_api(liste_anime, lien_api=lien_page_suivante)


def recupere_donnees_api(reponse_json, liste_anime):
    """Cette fonction récupère les éléments spécifiés pour chaque anime via l'API

    Args:
        reponse_json (String): Données au format JSON
        liste_anime (listeAnime): Liste allant contenir tous les animes et leurs attributs
    """
    reponse_json_dump = json.dumps(reponse_json)

    dict_data = json.loads(reponse_json_dump)

    for element in dict_data["data"]:

        # Ajout du titre à la liste d'anime
        liste_anime.nom.append(element["node"]["title"])

        # Ajout de l'identifiant à la liste d'anime
        liste_anime.id.append(element["node"]["id"])

        # Ajout du score à la liste d'anime
        liste_anime.score.append(element["list_status"]["score"])

        # Ajout de l'état de visionnage à la liste d'anime
        statut = element["list_status"]["status"]
        if statut == "watching":
            statut = "Watching"
        if statut == "completed":
            statut = "Completed"
        if statut == "on_hold":
            statut = "On-Hold"
        if statut == "dropped":
            statut = "Dropped"
        if statut == "plan_to_watch":
            statut = "Plan to Watch"
        liste_anime.etat.append(statut)


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


def affiche_liste_api(lien, headers, params=None):
    """_summary_

    Args:
        lien (String): Lien de l'API
        headers (Dict): Header à passer en argument pour la requête via l'API
        params (Dict, optional): Paramètres de sélection. Defaults to None.
    """

    # Création de la requête vers l'API
    reponse = requests.get(
        # Adresse de la demande
        lien,
        # Ajout des headers
        headers=headers,
        # Ajout des paramètres
        params=params,
    )
    print("\n")
    # Convertit la réponse en fichier json
    reponse_json = reponse.json()
    # Affiche le json de manière lisible
    print(json.dumps(reponse_json, indent=4, sort_keys=True))

    # Parcours des pages suivantes
    pagination = reponse_json["paging"]
    # Récupération du lien vers la liste suivante
    if "next" in pagination:
        # Recupération du lien nettoyé
        lien_page_suivante = pagination["next"]
        print(f"Lien nettoyé : {lien_page_suivante}")
        # Appel récursif de la fonction
        affiche_liste_api(lien_page_suivante, headers)
