# Création d'un outil d'analyse des animes vus 

Le but de cet outil est de permettre aux utilisateurs du site MyAnimeList de pouvoir extraire leur liste de séries d'animation personnalisée depuis un fichier stocké sur leur PC ou directement depuis le site via leur nom d'utilisateur. Une fois la liste extraite, les utilisateurs peuvent choisir de visualiser différentes données représentant leur consommation d'animation dans des graphiques dédiés ou bien les télécharger sous forme de fichier csv.

## I. Menu
### A. Importation des listes
Au début du programme, l'utilisateur se voit offrir le choix pour la récupération de ses données.

Dans le cas où il choisit de récupérer les données depuis un fichier, un second choix s'offre pour savoir si la récupération doit se faire depuis un fichier XML ou un fichier CSV.

Dans le cas où l'utilisateur choisit de récupérer les données via l'API. Le programme demande d'entrer le nom de l'utilisateur dont les données proviennent.

### B.Sauvegarde de la liste
Le programme propose ensuite de sauvegarder la liste au format CSV pour pouvoir la réutiliser plus tard pour d'autres applications que l'utilisateur pourrait avoir avec celle-ci.
### C. Récupération d'une sous-liste
Après avoir fini les traitements graphiques liés à la liste, le programme propose d'extraire les séries selon leur statuts pour pouvoir effectuer des traitements plus poussés sur des séries d'une même catégorie.
## II. Graphiques

### A. Nuages de mots
Une fois la liste importée, le programme propose de visualiser le nuage de mots.
### B. Histogrames
Différents types d'histogrammes sont possibles pour permettre à l'utilisateur de comparer les données qu'il souhaite. 
#### 1. Notes 
#### 2. Statuts de visionnage
### C. Diagrammes Circulaires
#### 1. Notes