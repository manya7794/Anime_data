from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

from extractList import (
    create_dataframe_annees_sorties,
    create_dataframe_notes,
    create_dataframe_statut,
)


def nuage_de_mot(themes):
    """Affichage du wordcloud correspondant à la liste passée en argument

    Args:
        themes (list): Liste contenant les mots à insérer dans le wordcloud
    """
    # Conversion de la liste en string
    liste_themes = (" ").join(themes)

    # Création du wordcloud
    wordcloud = WordCloud(width=800, height=400).generate(liste_themes)

    # Affichage de l'image obtenue
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()


def nuage_de_mot_dico(dico_themes):
    """Affichage du nuage de mots depuis un dictionnaire

    Args:
        dico_themes (dict): Dictionnaire contenant les mots et leur fréquence
    """
    wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(dico_themes)
    plt.figure(figsize=(20, 10), facecolor="k")
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    # plt.margins(x=0, y=0)
    plt.show()


def histogramme_notes(dico_notes):
    """Affichage de l'histogramme des notes

    Args:
        dico_notes (dict): Dictionnaire contenant les notes et leur fréquence
    """
    # Création de la dataframe
    notes = create_dataframe_notes(dico_notes.keys(), dico_notes.values())
    # Création de l'histogramme
    histogramme = sns.barplot(x=notes.Notes, y=notes.Frequence, data=notes)
    # Affichage de l'histogramme
    plt.show()


def graphique_annees_sortie(dico_annees):
    """Affichage de l'histogramme du nombre d'animes présents dans la liste selon leur année de sortie

    Args:
        dico_annees (dict): Dictionnaire contenant les années et le nombre d'animes sortis durant chaque
    """
    annees = create_dataframe_annees_sorties(dico_annees.keys(), dico_annees.values())
    # Création du graphique
    graphique = sns.lineplot(x=annees.Annee, y=annees.Frequence, data=annees)
    # Affichage du graphique
    plt.show()


def histogramme_statuts(dico_statuts):
    """Affichage de l'histogramme du nombre d'anime présents dans la liste selon leur statut de visionnage

    Args:
        dico (dict): Dictionnaire contenant les différents statuts de visionnage et le nombre d'animes présents pour
        chaque statut
    """
    # Création de la dataframe
    statuts = create_dataframe_statut(dico_statuts.keys(), dico_statuts.values())
    # Création de l'histogramme
    histogramme = sns.barplot(x=statuts.Statut, y=statuts.Frequence, data=statuts)
    # Affichage de l'histogramme
    plt.show()


def diagramme_circulaire_notes(dico_notes):
    """Affichage du diagramme circulaire des notes

    Args:
        dico_notes (Dict): Dictionnaire contenant les notes et leur féquence
    """
    # Création de la dataframe
    notes = create_dataframe_notes(dico_notes.keys(), dico_notes.values())
    colors = sns.color_palette("pastel")[0:9]
    # Création du diagramme circulaire
    plt.pie(notes.Frequence, labels=notes.Notes, colors=colors, autopct="%.0f%%")
    plt.show()
