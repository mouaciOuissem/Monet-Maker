## Introduction - Monet Maker
Ce projet a pour but de créer un agent pouvant peindre un tableau à partir d'une image. Il devra pouvoir dessiner un sketch du tableau, puis le remplir avec des couleurs, en donnant l'illusion d'être réalisé par un humain.

## Step 4 - Renoir et blanc

Lors de cette étape, nous passons pour la première fois à une tentative d'illusion d'activité humaine. Cette fois ci, l'objectif est de dessiner les contours selon une logique de proche en proche, comme si un vrai stylo était en train de tracer un trait devant nous.

## Utilisation :
Les valeurs requises en entrée par notre programme restent inchangées face à l'étape précédente :
```bash
python Step4.py -fi licorne.png -gb 3 -as [nombre_pixel_avant_refresh]
```

Si aucun tag n'est renseigné, le programme s'arrête en demandant de relancer avec le tag souhaité.
La valeur renseignée après le tag '-as' correspond au nombre de pixels à dessiner avant chaque update graphique. Plus elle est élevée, plus l'image se terminera rapidement, mais plus l'animation sera saccadée.

## Dépendances :
Les dépendances nécessaires sont celles déjà présentes depuis l'étape 1 et de scipy afin de créer un KDTree (strucuture de donnée permettant un calcul des distances entre chaque point) :
* `numpy==1.26.2`
* `opencv-python==4.8.1.78`
* `scipy==1.11.4`

Aucune librairie supplémentaire n'est utilisée, car turtle est présent dès l'installation de python.

## La sélection de l'ordre de dessin
Afin de détecter les pixels de proche en proche, nous produirons un KDTree à partir de l'image des contours. 
Cette structure contenue dans la librairie scipy. Nous créons un array contenant tous les pixels à dessiner et procédons à une boucle while tant que cet array n'est pas vide. Pour chaque tour de boucle, le KDTree nous permet de déterminer le point le plus proche de notre point actuel grâce à la méthode query. Une fois cela fait, on dessine le nouveau point, on supprime le point initial du reste à tracer et on repart sur un tour basé sur le nouveau point. Le premier point est sélectionné grâce à la fonction "get_starting_pixel" : un simple parcours de l'image qui récupère le premier point égal à 0 (donc noir) non isolé.

## Exécution :
Le script charge l'image spécifiée (lion ou licorne), applique le flou choisi par l'utilisateur, utilise la détection de contours de Canny puis utilise turtle pour dessiner ses contours comme sur une feuille blanche pour produire l'animation finale. Un tri par les pixels les plus proches en utilisant un KDTree permet de dessiner les contours de l'image dans le même ordre que le ferait un humain, et non plus de haut en bas.
Exemple qui nous parait optimal :
```bash
python Step4.py -fi licorne.png -gb 3 -as 10
```

## Conclusion :
Dans cette quatrième étape, nous avons récupéré le contour des étapes précédentes pour le redessiner en donnant l'illusion d'une action humaine. Cette étape constitue une avancée importante vers la création d'un agent capable de produire des peintures à partir d'images, c'est la première fois que nous essayons de cacher l'ordinateur derrière une action humaine.