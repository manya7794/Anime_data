from utils import graphUtil


class Menu:
    def __init__(self, liste_anime):
        self.liste_anime = liste_anime

    def _afficher_nuage_de_mot(self):
        """Initialise les thèmes et affiche le nuage de mots"""
        # Initialisation des themes
        themes = self.liste_anime.get_themes()
        # Affichage du nuage de mots
        graphUtil.nuage_de_mot_dict(themes)

    def _afficher_histogramme_notes(self):
        """Affichage de l'histogramme des notes"""
        notes = self.liste_anime.get_notes()
        graphUtil.histogramme_notes(notes)

    def _afficher_diagramme_circulaire_notes(self):
        """Affichage du diagramme circulaire des notes"""
        notes = self.liste_anime.get_notes()
        graphUtil.diagramme_circulaire_notes(notes)

    def _afficher_histogramme_statuts(self):
        """Affichage de l'histogramme des statuts"""
        statuts = self.liste_anime.get_statuts()
        graphUtil.histogramme_statuts(statuts)

    def _afficher_graphique_annees_sortie(self):
        """Affichage du graphique des années de sortie des animes"""
        # Initialisation des années de sortie
        annees_sortie = self.liste_anime.get_annees_sortie()
        # Affichage du graphique des années de sortie
        graphUtil.graphique_annees_sortie(annees_sortie)

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

    def afficher_menu(self, nom_affiche_liste=None):
        """Menu permettant d'effectuer différentes actions sur une liste

        Args:
            nom_affiche_liste (String, optional): Nom à afficher pour la liste lors des choix (Ex: "animes vus",
            "animes en pause", etc...). Defaults to None.
        """

        # Nuage de mots
        self._confirmer_action(
            "le nuage de mots",
            self._afficher_nuage_de_mot,
            nom_affiche_liste,
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

    def extraire_nouvelle_liste_personnalisee(self):
        """Cette fonction extrait une nouvelle liste d'animes dont l'état correspond au choix de l'utilisateur

        Returns:
            listeAnime: Nouvelle liste d'animes dont les états correspondent au choix de l'utilisateur
        """
        # Initialisation du choix de l'utilisateur
        choix_utilisateur = ""

        while choix_utilisateur != "Y" and choix_utilisateur != "N":
            # Récupération du choix de l'utilisateur
            choix_utilisateur = input(
                "Voulez-vous charger des animes dans une autre liste ? (Y/N)\n"
            ).upper()

            # Cas où l'utilisateur choisit de créer une nouvelle liste
            if choix_utilisateur == "Y":
                choix_utilisateur = ""

                while choix_utilisateur not in ("1", "2", "3", "4", "5"):
                    # Choix du type d'animes à sélectionner dans la liste
                    print("Quel type d'animes voulez-vous sélectionner ?")
                    print("1 : Animes en cours de visionnage")
                    print("2 : Animes finis")
                    print("3 : Animes en pause")
                    print("4 : Animes abandonnés")
                    print("5 : Animes à regarder plus tard")
                    choix_utilisateur = input()

                statuts = {
                    "1": "Watching",
                    "2": "Completed",
                    "3": "On-Hold",
                    "4": "Dropped",
                    "5": "Plan to Watch",
                }

                return self.liste_anime.get_animes_par_statut(
                    statuts[choix_utilisateur]
                )

            # Cas où l'utilisateur choisit de ne pas créer de nouvelle liste
            if choix_utilisateur == "N":
                return None
