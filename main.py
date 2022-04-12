from extractList import recupFichier
from scrapTheme import recupFromList
from tagGraph import cloudDico

nom = []
id = []
score = []
etat = []

# Récupération des listes
recupFichier(nom, id, score, etat)

# Création du dictonnaire de themes
themes = {}

# Initialisation des themes
recupFromList(themes, id)

cloudDico(themes)
