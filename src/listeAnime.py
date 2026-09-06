from utils import statistiquesUtil


class listeAnime:
    def __init__(self):
        """Constructeur de la classe listeAnime"""

        self.animes = []

    def get_notes(self):
        """Récupère les fréquences des notes de la liste.

        Returns:
            dict: Dictionnaire contenant les notes et leur fréquence
        """
        return statistiquesUtil.calcule_notes(self.animes)

    def get_statuts(self):
        """Récupère les fréquences des statuts de la liste.

        Returns:
            dict: Dictionnaire contenant les statuts et leur fréquence
        """
        return statistiquesUtil.calcule_statuts(self.animes)

    def get_themes(self):
        """Récupère les fréquences des thèmes de la liste.

        Returns:
            dict: Dictionnaire contenant les thèmes et leur fréquence
        """
        return statistiquesUtil.calcule_themes(self.animes)

    def get_annees_sortie(self):
        """Récupère les fréquences des années de sortie des animes.

        Returns:
            dict: Dictionnaire contenant les années et leur fréquence
        """
        return statistiquesUtil.calcule_annees_sortie(self.animes)

    def get_animes_par_statut(self, statut_cherche):
        """Cette fonction permet de récupérer une liste d'anime possédant tous le même statut de visionnage

        Args:
            statut (String): Statut de visionnage des animes que l'on souhaite récupérer
            ("Completed", "Plan to Watch", "Watching", "On-Hold" or "Dropped")

        Returns:
            listeAnime: Nouvelle liste contenant tous les animes possédant le statut de visionnage recherché
        """

        # Liste des animes correspondant au statut recherché
        animes_correspondants = [
            anime for anime in self.animes if anime.etat == statut_cherche
        ]

        # Création de la nouvelle liste
        nouvelle_liste_anime = listeAnime()

        # Ajout des animes correspondants
        nouvelle_liste_anime.animes.extend(animes_correspondants)

        return nouvelle_liste_anime
