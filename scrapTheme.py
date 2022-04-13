import requests
from bs4 import BeautifulSoup
from progressbar import ProgressBar

pbar = ProgressBar()

from dico import ajout_theme


def recupere_themes(dico, id):
    """Récupération des themes depuis la page web de l'anime

    Args:
        dico (dict): Dictionnaire contenant la liste des themes
        id (int): Identifiant de l'anime
    """

    # URL de la page à scrap
    URL = "https://myanimelist.net/anime/" + str(id)

    # Récupération du contenu de la page
    page = requests.get(URL)

    # Parsing de la page
    soup = BeautifulSoup(page.content, "html.parser")

    # Récupération de tous les genres de l'anime
    genre = soup.find_all(itemprop="genre")
    for theme in genre:
        ajout_theme(dico, theme.text.strip())


def recupere_from_list(dico, liste_identifiants):
    """Récupération des thèmes d'une liste d'animes

    Args:
        dico (dict): Dictionnaire contenant les thèmes et leur fréquence
        liste_identifiants (List): Liste d'identifiant des animes
    """
    for id in pbar(liste_identifiants):
        recupere_themes(dico, id)
