import requests
from bs4 import BeautifulSoup
from progressbar import ProgressBar

MAL_ANIME_URL = "https://myanimelist.net/anime/{}"

pbar = ProgressBar()


def recupere_themes(identifiant):
    """Récupère les thèmes depuis la page web d'un anime.

    Args:
        identifiant (int): Identifiant de l'anime

    Returns:
        list: Liste des thèmes de l'anime
    """

    # URL de la page à scrap
    url = MAL_ANIME_URL.format(identifiant)

    # Récupération du contenu de la page
    page = requests.get(url, timeout=10)
    page.raise_for_status()

    # Parsing de la page
    soup = BeautifulSoup(page.content, "html.parser")

    # Récupération de tous les genres de l'anime
    genres = soup.find_all(itemprop="genre")

    # Création de la liste des thèmes
    themes = [genre.text.strip() for genre in genres]

    return themes


def recupere_themes_from_list(liste_identifiants):
    """Récupère les thèmes d'une liste d'animes et calcule leur fréquence.

    Args:
        liste_identifiants (list): Liste des identifiants des animes

    Returns:
        dict: Dictionnaire contenant les thèmes et leur fréquence
    """

    # Dictionnaire contenant les thèmes et leur fréquence
    themes = {}

    for identifiant in pbar(liste_identifiants):

        # Récupération des thèmes de l'anime
        themes_anime = recupere_themes(identifiant)

        # Ajout des thèmes au dictionnaire
        for theme in themes_anime:
            if theme in themes:
                themes[theme] += 1
            else:
                themes[theme] = 1

    return themes
