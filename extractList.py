import pandas as pd
import numpy as np
import xml.etree.ElementTree as et

# Récupération du nom du fichier
tree = et.parse("animelist.xml")

# Récupération de la racine
root = tree.getroot()

#Identifiant de la série
#print(root[1][0].text)

#Titre de la série
#print(root[1][1].text)

#Score donné à la série
#print(root[1][9].text)

#Etat de visionnage de la série
#print(root[1][12].text)

id = []
score = []
etat = []

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
