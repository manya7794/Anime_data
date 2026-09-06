from config.settings import user_name
from listeAnime import listeAnime
from menu import Menu
from utils import apiUtil, fichierUtil


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
            animes = fichierUtil.choix_recuperation_donnees_fichier()

        # Récupération depuis l'API
        if choix_utilisateur == "2":
            animes = apiUtil.get_user_anime_list(user_name)

    # Ajout des animes à la liste
    if animes is None:
        print("\nImpossible de récupérer les données des animes.")
        print("Le programme va se terminer.")
        return

    liste_anime.animes.extend(animes)

    menu = Menu(liste_anime)

    liste_personnalisee = menu.extraire_nouvelle_liste_personnalisee()

    if liste_personnalisee is not None:
        menu = Menu(liste_personnalisee)
        menu.afficher_menu()
    else:
        menu = Menu(liste_anime)
        menu.afficher_menu()

    print("\nFin du programme")


if __name__ == "__main__":
    main()
