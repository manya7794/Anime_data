import utils.dictionnaireUtil as dictionnaire
from utils import listUtil, themeUtil, graphUtil


class listeAnime:
    def __init__(self, themes=None):
        """Constructeur de la classe listeAnime

        Args:
            themes (dict, optional): Dictionnaire des thèmes des animes. Defaults to None.
        """
        self.animes = []

        if themes is not None:
            # Dictonnaire de themes
            self.themes = themes
        else:
            self.themes = {}
        # Dictionnaire de notes
        self.notes = {
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
        # Dictionnaire des statuts
        self.statuts = {}

        # Dictionnaire des annees de sorties
        self.annees_sortie = {}

    def set_themes(self):
        """Cette fonction initialise les thèmes de la liste"""
        # Initialisation des themes
        ids = [anime.id for anime in self.animes]

        self.themes = {}

        # Initialisation des themes
        themeUtil.recupere_themes_from_list(self.themes, ids)

    def print_themes(self):
        """Affiche la liste des thèmes des animes contenus dans la liste"""
        for key, values in self.themes.items():
            print(key, " : ", values)

    def set_notes(self):
        """Cette fonction initialise les notes de la liste"""
        # Récupération des scores des animes
        scores = [anime.score for anime in self.animes]

        self.notes = {
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

        dictionnaire.ajout_note(scores, self.notes)

    def set_statuts(self):
        """Cette fonction initialise les statuts de la liste"""
        # Récupération des statuts des animes
        statuts = [anime.etat for anime in self.animes]

        self.statuts = {}

        dictionnaire.ajout_statut(statuts, self.statuts)

    def set_annees_sortie(self):
        "Cette fonction initialise les années de sortie de la liste"
        ids = [anime.id for anime in self.animes]

        dictionnaire.ajout_annee_sortie(ids, self.annees_sortie)

    def _afficher_nuage_de_mot(self):
        """Initialise les thèmes et affiche le nuage de mots"""
        # Initialisation des themes
        self.set_themes()
        # Affichage du nuage de mots
        graphUtil.nuage_de_mot_dict(self.themes)

    def _afficher_histogramme_notes(self):
        """Affichage de l'histogramme des notes"""
        graphUtil.histogramme_notes(self.notes)

    def _afficher_diagramme_circulaire_notes(self):
        """Affichage du diagramme circulaire des notes"""
        graphUtil.diagramme_circulaire_notes(self.notes)

    def _afficher_histogramme_statuts(self):
        """Affichage de l'histogramme des statuts"""
        graphUtil.histogramme_statuts(self.statuts)

    def _afficher_graphique_annees_sortie(self):
        """Affichage du graphique des années de sortie des animes"""
        # Initialisation des années de sortie
        self.set_annees_sortie()
        # Affichage du graphique des années de sortie
        graphUtil.graphique_annees_sortie(self.annees_sortie)

    def recupere_animes_selon_statut(self, statut_cherche):
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

    def _confirmer_action(self, action, fonction, nom_affiche_liste=None):
        """Demande confirmation avant d'exécuter une action

        Args:
            action (String): Action à proposer à l'utilisateur
            fonction (function): Fonction à exécuter si l'utilisateur confirme
            nom_affiche_liste (String, optional): Nom à afficher pour la liste.
        """
        message = self._construire_message_menu(action, nom_affiche_liste)
        choix_utilisateur = self._demander_confirmation(message)

        if choix_utilisateur == "Y":
            fonction()

    def _construire_message_menu(self, action, nom_affiche_liste=None):
        """Construit le message affiché lors d'une action du menu

        Args:
            action (String): Action à proposer à l'utilisateur
            nom_affiche_liste (String, optional): Nom de la liste affichée.

        Returns:
            String: Message à afficher
        """
        if nom_affiche_liste is not None:
            return (
                "Voulez-vous visualiser "
                + action
                + " de la liste "
                + nom_affiche_liste
                + " ? (Y/N)\n"
            )

        return "Voulez-vous visualiser " + action + " de la liste complète ? (Y/N)\n"

    def _demander_confirmation(self, message):
        """Demande une confirmation à l'utilisateur

        Args:
            message (String): Message affiché à l'utilisateur

        Returns:
            String: Réponse de l'utilisateur (Y ou N)
        """
        choix_utilisateur = ""

        while choix_utilisateur not in ("Y", "N"):
            choix_utilisateur = input(message).upper()

        return choix_utilisateur

    def menu_liste_anime(self, nom_affiche_liste=None):
        """Menu permettant d'effectuer différentes actions sur une liste

        Args:
            nom_affiche_liste (String, optional): Nom à afficher pour la liste lors des choix (Ex: "animes vus",
            "animes en pause", etc...). Defaults to None.
        """

        # Récupération des notes dans le dictionnaire
        self.set_notes()

        # Récupération des statuts dans le dictionnaire
        self.set_statuts()

        # Nuage de mots
        self._confirmer_action(
            "le nuage de mots", self._afficher_nuage_de_mot, nom_affiche_liste
        )

        # Histogramme des notes
        self._confirmer_action(
            "l'histogramme des notes",
            self._afficher_histogramme_notes,
            nom_affiche_liste,
        )

        # Diagramme circulaire des notes
        self._confirmer_action(
            "le diagramme circulaire des notes",
            self._afficher_diagramme_circulaire_notes,
            nom_affiche_liste,
        )

        # Répartition des statuts
        self._confirmer_action(
            "la répartition des statuts",
            self._afficher_histogramme_statuts,
            nom_affiche_liste,
        )

        # Répartition des années de sortie
        self._confirmer_action(
            "la répartition des années de sortie",
            self._afficher_graphique_annees_sortie,
            nom_affiche_liste,
        )

    def sauvegarde(self):
        listUtil.sauvegarde_liste(self.animes)
