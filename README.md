# Création d'un outil d'analyse des animes vus 

Le but de cet outil est de permettre aux utilisateurs du site MyAnimeList de pouvoir extraire leur liste de séries d'animation personnalisée depuis un fichier stocké sur leur PC ou directement depuis le site via leur nom d'utilisateur. Une fois la liste extraite, les utilisateurs peuvent choisir de visualiser différentes données représentant leur consommation d'animation dans des graphiques dédiés ou bien les télécharger sous forme de fichier csv.

## I.Installation
Download the project to your directory via a terminal by entering the following command:
```
git clone https://github.com/manya7794/Anime_data.git
```
Make sure you have Python 3.9 or higher installed on your computer and then run the following commands in a terminal opened in the folder containing the project:
```
python -m venv venv
.\venv\Scripts\activate
pip install -r .\requirements.txt
```

## II. Menu
### A. Importation des listes
Au début du programme, l'utilisateur se voit offrir le choix pour la récupération de ses données.
![image](https://user-images.githubusercontent.com/72400479/167317467-1063473f-99b8-43ee-a4b8-0eda5c98732f.png)


Dans le cas où il choisit de récupérer les données depuis un fichier, un second choix s'offre pour savoir si la récupération doit se faire depuis un fichier XML ou un fichier CSV.

![image](https://user-images.githubusercontent.com/72400479/167317770-52613bd0-36b8-4228-b1c6-550bba39b4a6.png)

Par la suite, l'adresse du fichier et son nom est demandé à l'utilisateur.

![image](https://user-images.githubusercontent.com/72400479/167317812-28ab90b3-2fa3-400d-b9b9-953e4b7109eb.png)

Dans le cas où l'utilisateur choisit de récupérer les données via l'API. Le programme demande d'entrer le nom de l'utilisateur dont les données proviennent.

![image](https://user-images.githubusercontent.com/72400479/167317740-bc3506ed-b412-4d26-9eaf-88ee068f6c0b.png)

### B.Sauvegarde de la liste
Le programme propose ensuite de sauvegarder la liste au format CSV pour pouvoir la réutiliser plus tard pour d'autres applications que l'utilisateur pourrait avoir avec celle-ci.

![image](https://user-images.githubusercontent.com/72400479/167317434-5dd3fd24-b4cd-4b37-8fe5-c8922e49b8a8.png)

### C. Récupération d'une sous-liste
Après avoir fini les traitements graphiques liés à la liste, le programme propose d'extraire les séries selon leur statuts pour pouvoir effectuer des traitements plus poussés sur des séries d'une même catégorie.

![image](https://user-images.githubusercontent.com/72400479/167317570-ccd2977b-6fcf-42c5-9a85-0c4b38201a04.png)

Si l'utilisateur choisit d'extraire une sous-liste, un nouveau choix s'offre à lui pour choisir le type de séries qu'il souhaite conserver dans la nouvelle liste.

![image](https://user-images.githubusercontent.com/72400479/167318124-74fcaa41-e4a6-44be-b987-2a1b5bbc8cab.png)


## III. Graphiques

### A. Nuages de mots
Une fois la liste importée, le programme propose de visualiser le nuage de mots.
![image](https://user-images.githubusercontent.com/72400479/167317719-093a01e2-b849-45dc-8c37-2300b7d2200b.png)

![image](https://user-images.githubusercontent.com/72400479/167318012-085a4273-7680-4990-bc5f-0c0dda0c4de8.png)


### B. Histogrames
Différents types d'histogrammes sont possibles pour permettre à l'utilisateur de comparer les données qu'il souhaite. 
#### 1. Notes 
![image](https://user-images.githubusercontent.com/72400479/167317661-6277e586-92dc-4a4b-b4f2-a1f0a7d79003.png)

![image](https://user-images.githubusercontent.com/72400479/167318046-f6f7e1de-b976-4ba5-a45a-87a9c9b64b1b.png)


#### 2. Statuts de visionnage
![image](https://user-images.githubusercontent.com/72400479/167317703-abcc7a70-eedf-492b-a0b9-f01b287044b6.png)

![image](https://user-images.githubusercontent.com/72400479/167318097-42083cfc-2eb9-4f97-94f4-c1dda7e433aa.png)


### C. Diagrammes Circulaires
#### 1. Notes
![image](https://user-images.githubusercontent.com/72400479/167317678-1fb54ee2-d720-4f0f-8c01-33587afd654d.png)

![image](https://user-images.githubusercontent.com/72400479/167318064-c39c4c99-34c7-4529-a2b1-e896925516d1.png)
