from pyparsing import Word
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from extractList import *

def cloud(objet):
    """Affichage du wordcloud correspondant à la liste passée en argument

    Args:
        objet (List): Liste contenant les mots à insérer dans le wordcloud
    """
    #Conversion de la liste en string
    listeObjet=(" ").join(objet)
    
    #Création du wordcloud
    wordcloud = WordCloud(width=480, height=480, margin=0).generate(listeObjet)

    #Affichage de l'image obtenue
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()



nom=[]
id=[]
score=[]
etat=[]
recupFichier(nom, id, score, etat)

cloud(nom)



