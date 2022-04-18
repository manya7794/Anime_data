from extractList import extraire_nouvelle_liste_personnalisee
from listeAnime import listeAnime

liste_complete = listeAnime(recupere_donnees_fichier=True)

liste_complete.menu_liste_anime()

liste_personnalisee = extraire_nouvelle_liste_personnalisee(liste_complete)

# Cas où l'utilisateur a initialisé la liste
if liste_personnalisee is not None:
    liste_personnalisee.menu_liste_anime()

print("Fin du programme")
