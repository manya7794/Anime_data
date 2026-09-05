from config.settings import user_name
from listeAnime import listeAnime
from utils import apiUtil, listUtil


def main():

    # Création de la liste
    liste_anime = listeAnime()
    animes = []

    # Récupération du choix de l'utilisateur
    choix_utilisateur = ""

    while choix_utilisateur != "1" and choix_utilisateur != "2":
        print("Comment souhaitez-vous récupérer la liste des animes")
        print("1. Depuis un fichier (XML ou CSV)")
        print("2. Depuis l'API")
        choix_utilisateur = input("Votre choix : ")

        # Récupération depuis un fichier
        if choix_utilisateur == "1":
            animes = listUtil.choix_recuperation_donnees_fichier()

        # Récupération depuis l'API
        if choix_utilisateur == "2":
            animes = apiUtil.get_user_anime_list(user_name)

    # Ajout des animes à la liste
    if animes is not None:
        liste_anime.animes.extend(animes)

    liste_personnalisee = listUtil.extraire_nouvelle_liste_personnalisee(liste_anime)

    if liste_personnalisee is not None:
        liste_personnalisee.menu_liste_anime()
    else:
        liste_anime.menu_liste_anime()

    print("\nFin du programme")


if __name__ == "__main__":
    main()
