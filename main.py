import json
import requests
from extractList import (
    extraire_nouvelle_liste_personnalisee,
    affiche_liste_api,
    recupere_annee_sortie_api,
)
from listeAnime import listeAnime
from config import api_key, user_name

# Clé d'API
headers = {
    "X-MAL-CLIENT-ID": api_key,
}
# Paramètres de sélection
params = {"offset": "0", "fields": "list_status"}
# Lien de l'API
lien_api = f"https://api.myanimelist.net/v2/users/{user_name}/animelist"

liste_complete = listeAnime()
"""
liste_complete.set_annees_sortie()

print(liste_complete.annees_sortie)
"""


liste_complete.menu_liste_anime()

liste_personnalisee = extraire_nouvelle_liste_personnalisee(liste_complete)


# Cas où l'utilisateur a initialisé la liste
if liste_personnalisee is not None:
    liste_personnalisee.menu_liste_anime()


print("\nFin du programme")
