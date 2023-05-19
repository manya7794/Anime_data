from utils import csvUtil, xmlUtil

import json
import pandas as pd
import requests


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
        xmlUtil.recupere_donnees_xml(fichier, liste_anime)

    # Cas où l'utilisateur veut récupérer depuis un fichier csv
    if choix_utilisateur == "2":
        fichier = input("Entrez le nom du fichier : ")
        fichier = fichier + ".csv"
        csvUtil.recupere_donnees_csv(fichier, liste_anime)


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

    Returns:
        anime_dataframe: Dataframe contenant les animes et leurs caractéristiques
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
    """Cette fonction génère un dataframe à partir des années de sortie de chaque anime

    Args:
        annees (List): Liste des années de sortie des animes
        annees_frequence (List): Liste des fréquences de chaque année

    Returns:
        dataframe: Dataframe contenant les années et leur fréquence
    """
    annees_sortie_dataframe = pd.DataFrame(
        {"Annee": annees, "Frequence": annees_frequence}
    )
    return annees_sortie_dataframe


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
        # Récupération du lien nettoyé
        lien_page_suivante = pagination["next"]
        print(f"Lien nettoyé : {lien_page_suivante}")
        # Appel récursif de la fonction
        affiche_liste_api(lien_page_suivante, headers)
