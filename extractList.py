import pandas as pd
import numpy as np
import xml.etree.ElementTree as et

def recupFichier(nom, id, score, etat):
    # Récupération du nom du fichier
    tree = et.parse("animelist.xml")

    # Récupération de la racine
    root = tree.getroot()

    #Récupération de tous les noms dans une liste
    for titre in root.iter("series_title"):
        # print(identifiant.text)
        nom.append(titre.text)

    #Récupération de tous les identifiants dans une liste
    for identifiant in root.iter("series_animedb_id"):
        # print(identifiant.text)
        id.append(identifiant.text)

    #Récupération de toutess les notes dans une liste
    for note in root.iter("my_score"):
        score.append(note.text)

    #Récupération de tous les statuts de visionnage dans une liste
    for statut in root.iter("my_status"):
        etat.append(statut.text)
    
    return(nom, id, score, etat)


def createDataFrame(nom, id, score, etat):
    #Création d'une dataframe
    anime_df = pd.DataFrame(
        list(zip(
            nom, id, score, etat
        )),
        columns=["Nom","Identifiant", "Note", "Statut"]
    )

def saveCSV(dataframe):
    #Sauvegarde de la dataframe au format CSV
    dataframe.to_csv("animelist.csv")

