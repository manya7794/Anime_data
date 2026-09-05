import json
import time
import requests

from models.anime import Anime
from config.settings import (
    api_key,
    NOMBRE_TENTATIVES_DEFAUT,
    DELAI_TENTATIVE_DEFAUT,
    MAL_API_URL,
    MAL_API_FIELDS,
)

STATUTS_ANIME = {
    "watching": "Watching",
    "completed": "Completed",
    "on_hold": "On-Hold",
    "dropped": "Dropped",
    "plan_to_watch": "Plan to Watch",
}


def _recupere_donnees_api(self, user_name):
    """Récupère les données des animes depuis l'API."""

    donnees = apiUtil.get_user_anime_list(user_name, self)

    return donnees


def _get_api_page(
    lien_api,
    headers,
    params=None,
    nombre_tentatives=NOMBRE_TENTATIVES_DEFAUT,
    delai_tentative=DELAI_TENTATIVE_DEFAUT,
):
    """Fonction permettant de récupérer une page de données depuis l'API MAL

    Args:
        lien_api (String): Lien de la page à récupérer.
        headers (dict): Headers utilisés pour la requête.
        params (dict, optional): Paramètres de la requête.
        nombre_tentatives (int, optional): Nombre maximal de tentatives.
        delai_tentative (int, optional): Délai entre deux tentatives.

    Returns:
        dict: Réponse de l'API au format JSON.
        None: Si la récupération échoue.
    """

    # Nombre de tentatives effectuées
    tentative = 0

    while tentative < nombre_tentatives:
        try:
            # Création de la requête vers l'API
            print(f"Récupération de la page : {lien_api}")
            reponse = requests.get(
                # Adresse de la demande
                lien_api,
                # Ajout des headers
                headers=headers,
                # Ajout des paramètres
                params=params,
                timeout=60,
            )

            # Vérification du statut de la réponse
            reponse.raise_for_status()

            # Convertit la réponse en fichier json
            return reponse.json()

        except (
            requests.exceptions.Timeout,
            requests.exceptions.ConnectionError,
        ) as erreur:
            tentative += 1
            print(
                f"Erreur réseau lors de la tentative "
                f"{tentative}/{nombre_tentatives} : {erreur}"
            )

            if tentative < nombre_tentatives:
                time.sleep(delai_tentative)

        except requests.exceptions.HTTPError as erreur:
            print(f"Erreur HTTP lors de la récupération : {erreur}")
            return None

    # Vérification si toutes les tentatives ont échoué
    print("Les tentatives de récupération ont toutes échoué.")
    return None


def get_user_anime_list(
    user_name,
    lien_api=None,
    nombre_tentatives=NOMBRE_TENTATIVES_DEFAUT,
    delai_tentative=DELAI_TENTATIVE_DEFAUT,
):
    """Fonction permettant à l'utilisateur de sélectionner les animes qu'il souhaite récupérer selon leur statut

    Args:
        liste_anime (listeAnime): Liste allant contenir tous les animes et leurs attributs
        lien_api (String, optional): Lien de l'API. Defaults to None.
        nombre_tentatives (int, optional): Nombre maximal de tentatives.
        delai_tentative (int, optional): Délai entre deux tentatives.
    """

    donnees_animes = []

    # Création du lien de l'api
    if lien_api is None:
        lien_api = MAL_API_URL.format(user_name=user_name)

    # Clé d'API
    headers = {
        "X-MAL-CLIENT-ID": api_key,
    }

    # Paramètres de sélection
    params = {"offset": 0, "fields": MAL_API_FIELDS}

    # Parcours des pages
    premiere_requete = True

    while lien_api is not None:
        reponse_json = _get_api_page(
            lien_api,
            headers,
            params if premiere_requete else None,
            nombre_tentatives,
            delai_tentative,
        )

        if reponse_json is None:
            return

        premiere_requete = False

        # Ajout des animes à la liste d'anime
        animes = recupere_donnees_api(reponse_json)
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

        animes.append(anime)

    return animes


def recupere_annee_sortie_api_mal(id_anime):
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
