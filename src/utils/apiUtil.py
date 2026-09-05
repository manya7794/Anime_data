from config.settings import (
    api_key,
    MAL_API_FIELDS,
    MAL_API_URL,
    NOMBRE_TENTATIVES_DEFAUT,
    DELAI_TENTATIVE_DEFAUT,
)

from models.anime import Anime

import requests
import time

STATUTS_ANIME = {
    "watching": "Watching",
    "completed": "Completed",
    "on_hold": "On-Hold",
    "dropped": "Dropped",
    "plan_to_watch": "Plan to Watch",
}


def get_user_anime_list(
    user_name,
    lien_api=None,
    nombre_tentatives=NOMBRE_TENTATIVES_DEFAUT,
    delai_tentative=DELAI_TENTATIVE_DEFAUT,
):
    """Fonction permettant de récupérer la liste des animes d'un utilisateur via l'API MAL

    Args:
        user_name (String): Nom d'utilisateur MAL
        lien_api (String, optional): Lien de l'API. Defaults to None.
        nombre_tentatives (int, optional): Nombre maximal de tentatives.
        delai_tentative (int, optional): Délai entre deux tentatives.

    Returns:
        list: Liste des objets Anime
        None: Si la récupération échoue.
    """

    # Création du lien de l'api
    if lien_api is None:
        lien_api = MAL_API_URL.format(user_name=user_name)

    # Clé d'API
    headers = {
        "X-MAL-CLIENT-ID": api_key,
    }

    # Paramètres de sélection
    params = {
        "offset": 0,
        "fields": MAL_API_FIELDS,
    }

    # Données des animes
    donnees_animes = []

    # Parcours des pages
    premiere_requete = True

    while lien_api is not None:
        try:
            # Création de la requête vers l'API
            print(f"Récupération de la page : {lien_api}")
            reponse = requests.get(
                # Adresse de la demande
                lien_api,
                # Ajout des headers
                headers=headers,
                # Ajout des paramètres
                params=params if premiere_requete else None,
                timeout=60,
            )

            # Vérification du statut de la réponse
            reponse.raise_for_status()

            # Convertit la réponse en fichier json
            reponse_json = reponse.json()

        except (
            requests.exceptions.Timeout,
            requests.exceptions.ConnectionError,
        ) as erreur:
            print(f"Erreur réseau : {erreur}")
            return None

        except requests.exceptions.HTTPError as erreur:
            print(f"Erreur HTTP lors de la récupération : {erreur}")
            return None

        premiere_requete = False

        # Récupération des données de la page
        animes = recupere_donnees_api(reponse_json)

        # Ajout des données à la liste
        donnees_animes.extend(animes)

        # Parcours des pages suivantes
        pagination = reponse_json["paging"]

        # Vérification de la page suivante
        lien_page_suivante = pagination.get("next")

        if lien_page_suivante == lien_api:
            print("La page suivante est identique à la page actuelle.")
            break

        # Récupération du lien vers la liste suivante
        lien_api = lien_page_suivante

    return donnees_animes


def recupere_donnees_api(reponse_json):
    """Cette fonction récupère les éléments spécifiés pour chaque anime via l'API

    Args:
        reponse_json (dict): Données au format JSON

    Returns:
        list: Liste des objets Anime
    """
    animes = []

    for element in reponse_json["data"]:
        # Ajout de l'état de visionnage à la liste d'anime
        statut = element["list_status"]["status"]
        statut = STATUTS_ANIME.get(statut, statut)

        anime = Anime(
            nom=element["node"]["title"],
            id=element["node"]["id"],
            score=element["list_status"]["score"],
            etat=statut,
        )

        # Ajout de l'anime à la liste
        animes.append(anime)

    return animes


def recupere_annee_sortie_api_mal(id_anime):
    # Clé d'API
    headers = {
        "X-MAL-CLIENT-ID": api_key,
    }

    # Création de la requête vers l'API
    reponse = requests.get(
        f"https://api.myanimelist.net/v2/anime/{id_anime}?fields=start_season,status",
        headers=headers,
    )

    # Vérification du statut de la réponse
    reponse.raise_for_status()

    # Conversion de la réponse au format json
    reponse_json = reponse.json()

    # Renvoi de l'année de sortie
    if reponse_json["status"] != "not_yet_aired":
        # print(reponse_json["start_season"]["year"])
        return reponse_json["start_season"]["year"]
