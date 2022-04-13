from wordcloud import WordCloud
import matplotlib.pyplot as plt


dico = {}


def nuage_de_mot(objet):
    """Affichage du wordcloud correspondant à la liste passée en argument

    Args:
        objet (list): Liste contenant les mots à insérer dans le wordcloud
    """
    # Conversion de la liste en string
    listeObjet = (" ").join(objet)

    # Création du wordcloud
    wordcloud = WordCloud(width=800, height=400).generate(listeObjet)

    # Affichage de l'image obtenue
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()


def nuage_de_mot_dico(dico):
    """Affichage du nuage de mots depuis un dictionnaire

    Args:
        dico (dict): Dictionnaire contenant les mots et leur fréquence
    """
    wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(dico)
    plt.figure(figsize=(20, 10), facecolor="k")
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    # plt.margins(x=0, y=0)
    plt.show()
