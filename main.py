from dico import ajout_theme
from extractList import choix_recuperation_donnees, sauvegarde_liste
from scrapTheme import recupere_from_list
from tagGraph import nuage_de_mot_dico

nom = []
id = []
score = []
etat = []

# Récupération des listes
choix_recuperation_donnees(nom, id, score, etat)


# Création du dictonnaire de themes
themes = {}

# Initialisation des themes
recupere_from_list(themes, id)

# Affichage du nuage de mots
nuage_de_mot_dico(themes)

# Sauvegarde de la liste
sauvegarde_liste(nom, id, score, etat)
