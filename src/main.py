from listeAnime import listeAnime
from utils import listUtil


def main():
    user_name = input("Entrez le nom de l'utilisateur : ")
    liste_complete = listeAnime(user_name=user_name)
    liste_complete.menu_liste_anime()

    liste_personnalisee = listUtil.extraire_nouvelle_liste_personnalisee(liste_complete)

    if liste_personnalisee is not None:
        liste_personnalisee.menu_liste_anime()

    print("\nFin du programme")


if __name__ == "__main__":
    main()
