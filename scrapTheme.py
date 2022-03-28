import requests
from bs4 import BeautifulSoup

from dico import *

def RecupThemes(dico, id):
    """Récupération des themes depuis la page web de l'anime

    Args:
        dico (dict): Dictionnaire contenant la liste des themes
        id (int): Identifiant de l'anime
    """

    #URL de la page à scrap
    URL = "https://myanimelist.net/anime/"+str(id)

    #Récupération du contenu de la page
    page = requests.get(URL)

    #Parsing de la page
    soup = BeautifulSoup(page.content, "html.parser")

    #Récupération de tous les genres de l'anime
    genre=soup.find_all(itemprop="genre")
    for theme in genre:
        ajoutTheme(dico, theme.text.strip())