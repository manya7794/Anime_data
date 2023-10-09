import numpy as np

import utils.dictionnaireUtil as dictionnaire
from utils import listUtil, apiUtil, themeUtil, graphUtil


class ListeAnime:
    """Classe décrivant la liste d'anime d'un utilisateur"""

    def __init__(
        self,
        nom=None,
        anime_id=None,
        score=None,
        etat=None,
        themes=None,
        recupere_donnees_fichier=None,
        recupere_donnees_api=None,
    ):
        """Constructeur de la classe listeAnime

        Args:
            nom (List, optional): Liste des noms d'animes. Defaults to None.
            id (List, optional): Liste des identifiants d'animes. Defaults to None.
            score (List, optional): Liste des scores d'animes. Defaults to None.
            etat (List, optional): Liste des états de visionnage des animes. Defaults to None.
            themes (Dict, optional): Dictionnaire des thèmes des animes. Defaults to None.
            recupere_donnees_fichier (boolean, optional): Choisit ou non de récupérer les données depuis un fichier.
            Defaults to None.
            recupere_donnees_api (boolean, optional): Choisit ou non de récupérer les données depuis l'API.
            Defaults to None.
        """
        if nom is not None:
            self.nom = nom
        else:
            self.nom = []
        if anime_id is not None:
            self.anime_id = anime_id
        else:
            self.anime_id = []
        if score is not None:
            self.score = score
        else:
            self.score = []
        if etat is not None:
            self.etat = etat
        else:
            self.etat = []
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

        if recupere_donnees_fichier is not None and recupere_donnees_fichier is True:
            # Récupération des listes
            listUtil.choix_recuperation_donnees_fichier(self)
        if recupere_donnees_api is not None and recupere_donnees_api is True:
            # Récupération des listes
            apiUtil.choix_recuperation_donnees_api(self, params=True)
        if recupere_donnees_fichier is None and recupere_donnees_api is None:
            # Récupération du choix de l'utilisateur
            choix_utilisateur = ""

            while choix_utilisateur != "1" and choix_utilisateur != "2":
                print("Comment souhaitez-vous récupérer la liste des animes")
                print("1. Depuis un fichier (XML ou CSV)")
                print("2. Depuis l'API")
                choix_utilisateur = input()

            if choix_utilisateur == "1":
                listUtil.choix_recuperation_donnees_fichier(self)
            else:
                apiUtil.choix_recuperation_donnees_api(self, params=True)

    def set_themes(self):
        """Cette fonction initialise les thèmes de la liste"""
        # Initialisation des themes
        themeUtil.recupere_themes_from_list(self.themes, self.anime_id)

    def print_themes(self):
        """Affiche la liste des thèmes des animes contenus dans la liste"""
        for key, values in self.themes:
            print(key, " : ", values)

    def set_notes(self):
        """Cette fonction initialise les notes de la liste"""
        dictionnaire.ajout_note(self.score, self.notes)

    def set_statuts(self):
        """Cette fonction initialise les statuts de la liste"""
        dictionnaire.ajout_statut(self.etat, self.statuts)

    def set_annees_sortie(self):
        "Cette fonction initialise les années de sortie de la liste"
        dictionnaire.ajout_annee_sortie(self.anime_id, self.annees_sortie)

    def nuage_de_mot(self):
        """Affichage du nuage de mots"""
        graphUtil.nuage_de_mot_dict(self.themes)

    def histogramme_notes(self):
        """Affichage de l'histogramme des notes"""
        graphUtil.histogramme_notes(self.notes)

    def diagramme_circulaire_notes(self):
        """Affichage du diagramme circulaire des notes"""
        graphUtil.diagramme_circulaire_notes(self.notes)

    def histogramme_statuts(self):
        """Affichage de l'histogramme des statuts"""
        graphUtil.histogramme_statuts(self.statuts)

    def graphique_annees_sortie(self):
        """Affichage du graphique des années de sortie des animes"""
        graphUtil.graphique_annees_sortie(self.annees_sortie)

    def sauvegarde(self):
        """Fonction permettant de sauvegarder la liste dans un fichier"""
        listUtil.sauvegarde_liste(
            self.nom,
            self.anime_id,
            self.score,
            self.etat,
        )

    # A compléter
    def recupere_animes_selon_statut(self, statut_cherche):
        """Cette fonction permet de récupérer une liste d'anime possédant tous le même statut de visionnage

        Args:
            statut (String): Statut de visionnage des animes que l'on souhaite récupérer
            ("Completed", "Plan to Watch", "Watching", "On-Hold" or "Dropped")

        Returns:
            listeAnime: Nouvelle liste contenant tous les animes possédant le statut de visionnage recherché
        """
        nom_nouvelle_liste = []
        id_nouvelle_liste = []
        score_nouvelle_liste = []
        etat_nouvelle_liste = []

        # Liste des index des animes correspondants au statut recherché
        index_liste = []

        # Ajouter une fonction de retour d'erreur si le statut spécifié ne correspond à aucun des choix possibles

        # Parcours de la liste pour récupérer tous les animes correspondant au statut recherché
        index_liste = np.where(np.array(self.etat) == statut_cherche)
        index_liste = index_liste[0].tolist()

        # Ajout du nom de l'anime
        for index, element in enumerate(self.nom, start=0):
            if index in index_liste:
                nom_nouvelle_liste.append(element)

        # Ajout de l'id de l'anime
        for index, element in enumerate(self.anime_id, start=0):
            if index in index_liste:
                id_nouvelle_liste.append(element)

        # Ajout du score de l'anime
        for index, element in enumerate(self.score, start=0):
            if index in index_liste:
                score_nouvelle_liste.append(element)

        # Ajout de l'etat de l'anime
        for index, element in enumerate(self.etat, start=0):
            if index in index_liste:
                etat_nouvelle_liste.append(element)

        # Création de la nouvelle liste
        nouvelle_liste_anime = ListeAnime(
            nom=nom_nouvelle_liste,
            anime_id=id_nouvelle_liste,
            score=score_nouvelle_liste,
            etat=etat_nouvelle_liste,
            recupere_donnees_fichier=False,
            recupere_donnees_api=False,
        )
        return nouvelle_liste_anime

    # Diviser le menu en sous-menus plus lisibles
    def menu_liste_anime(self, nom_affiche_liste=None):
        """Menu permettant d'effectuer différentes actions sur une liste

        Args:
            nom_affiche_liste (String, optional): Nom à afficher pour la liste lors des choix (Ex: "animes vus",
            "animes en pause", etc...). Defaults to None.
        """
        # Initialisation du choix de l'utilisateur
        choix_utilisateur = ""

        # Récupération des notes dans le dictionnaire
        self.set_notes()

        # Récupération des notes dans le dictionnaire
        self.set_statuts()

        while choix_utilisateur != "Y" and choix_utilisateur != "N":
            # Récupération du choix de l'utilisateur
            if nom_affiche_liste is not None:
                choix_utilisateur = input(
                    "Voulez-vous visualiser le nuage de mot de la liste des "
                    + nom_affiche_liste
                    + " ? (Y/N)\n"
                )
            else:
                choix_utilisateur = input(
                    "Voulez-vous visualiser le nuage de mot de la liste complète ? (Y/N)\n"
                )

            # Cas où l'utilisateur choisit de sauvegarder
            if choix_utilisateur == "Y":
                # Initialisation des themes
                self.set_themes()
                # Affichage du nuage de mots
                self.nuage_de_mot()

        # Reset du choix de l'utilisateur
        choix_utilisateur = ""

        # Sauvegarde de la liste
        print("Sauvegarde de la liste complète")
        self.sauvegarde()

        while choix_utilisateur != "Y" and choix_utilisateur != "N":
            # Récupération du choix de l'utilisateur
            if nom_affiche_liste is not None:
                choix_utilisateur = input(
                    "Voulez-vous visualiser l'histogramme des notes de la liste des "
                    + nom_affiche_liste
                    + " ? (Y/N)\n"
                )
            else:
                choix_utilisateur = input(
                    "Voulez-vous visualiser l'histogramme des notes de la liste complète ? (Y/N)\n"
                )
            # Cas où l'utilisateur choisit de sauvegarder
            if choix_utilisateur == "Y":
                # Affichage de l'histogramme des notes
                self.histogramme_notes()

        # Reset du choix de l'utilisateur
        choix_utilisateur = ""
        while choix_utilisateur != "Y" and choix_utilisateur != "N":
            # Récupération du choix de l'utilisateur
            if nom_affiche_liste is not None:
                choix_utilisateur = input(
                    "Voulez-vous visualiser le diagramme circulaire des notes de la liste des "
                    + nom_affiche_liste
                    + " ? (Y/N)\n"
                )
            else:
                choix_utilisateur = input(
                    "Voulez-vous visualiser le diagramme circulaire des notes de la liste complète ? (Y/N)\n"
                )
            # Cas où l'utilisateur choisit de sauvegarder
            if choix_utilisateur == "Y":
                # Affichage de l'histogramme des notes
                self.diagramme_circulaire_notes()

        # Reset du choix de l'utilisateur
        choix_utilisateur = ""
        while choix_utilisateur != "Y" and choix_utilisateur != "N":
            # Récupération du choix de l'utilisateur
            if nom_affiche_liste is not None:
                choix_utilisateur = input(
                    "Voulez-vous visualiser la répartition des statuts de la liste des "
                    + nom_affiche_liste
                    + " ? (Y/N)\n"
                )
            else:
                choix_utilisateur = input(
                    "Voulez-vous visualiser la répartition des statuts de la liste complète ? (Y/N)\n"
                )
            # Cas où l'utilisateur choisit de sauvegarder
            if choix_utilisateur == "Y":
                # Affichage de l'histogramme des notes
                self.histogramme_statuts()

        # Choix pour la répartition des années de sortie
        """
        # Reset du choix de l'utilisateur
        choix_utilisateur = ""
        while choix_utilisateur != "Y" and choix_utilisateur != "N":
            # Récupération du choix de l'utilisateur
            if nom_affiche_liste is not None:
                choix_utilisateur = input(
                    "Voulez-vous visualiser la répartition des années de sortie de la liste des "
                    + nom_affiche_liste
                    + " ? (Y/N)\n"
                )
            else:
                choix_utilisateur = input(
                    "Voulez-vous visualiser la répartition des années de sortie de la liste complète ? (Y/N)\n"
                )
            # Cas où l'utilisateur choisit de sauvegarder
            if choix_utilisateur == "Y":

                # Affichage de l'histogramme des notes
                self.histogramme_statuts()
        """
