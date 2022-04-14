from dico import ajout_note, ajout_theme
from extractList import (
    choix_recuperation_donnees,
    create_dataframe_notes,
    sauvegarde_liste,
)
from scrapTheme import recupere_from_list
from tagGraph import histogramme_notes, nuage_de_mot_dico

nom = []
id = []
score = []
etat = []

# Récupération des listes
choix_recuperation_donnees(nom, id, score, etat)

# Création du dictonnaire de themes
themes = {}
# Création du dictionnaire de notes
notes = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 0,
}

# Initialisation des themes
recupere_from_list(themes, id)

# Affichage du nuage de mots
nuage_de_mot_dico(themes)

# Sauvegarde de la liste
sauvegarde_liste(nom, id, score, etat)

# Récupération des notes dans le dictionnaire
ajout_note(score, notes)

# Affichage de l'histogramme des notes
histogramme_notes(notes)
