import json

import requests
from config import api_key


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
        # Récupération du lien nettoyé
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


def recupere_annee_sortie_api_mal(id_anime):
    """Fonction récupérant la date de sortie des animes de la liste depuis l'API

    Args:
        id_anime (List): Liste contenant les identifiants de tous les animes

    Returns:
        List: Liste contenant la date de sortie de tous les animes
    """
    # Clé d'API
    headers = {
        "X-MAL-CLIENT-ID": api_key,
    }
    reponse = requests.get(
        f"https://api.myanimelist.net/v2/anime/{id_anime}?fields=start_season,status",
        headers=headers,
    )
    # Conversion de la réponse au format json
    reponse_json = reponse.json()
    # Dump de la réponse
    reponse_json_dump = json.dumps(reponse_json)
    # Enregistrement du dump dans un dictionnaire
    dict_data = json.loads(reponse_json_dump)
    # Renvoi de l'année de sortie
    if dict_data["status"] != "not_yet_aired":
        # print(dict_data["start_season"]["year"])
        return dict_data["start_season"]["year"]
