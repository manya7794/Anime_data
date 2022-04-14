from dico import ajout_note, ajout_theme
from extractList import choix_recuperation_donnees, sauvegarde_liste
from listeAnime import listeAnime
from scrapTheme import recupere_from_list
from tagGraph import histogramme_notes, nuage_de_mot_dico

liste_complete = listeAnime()

# Récupération des listes
choix_recuperation_donnees(liste_complete)

# Initialisation des themes
recupere_from_list(liste_complete.themes, liste_complete.id)

# Affichage du nuage de mots
nuage_de_mot_dico(liste_complete.themes)

# Sauvegarde de la liste
sauvegarde_liste(
    liste_complete.nom, liste_complete.id, liste_complete.score, liste_complete.etat
)


# Récupération des notes dans le dictionnaire
ajout_note(liste_complete.score, liste_complete.notes)

# Affichage de l'histogramme des notes
histogramme_notes(liste_complete.notes)
