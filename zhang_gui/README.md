## Introduction - Monet Maker
Ce projet a pour but de créer un agent pouvant peindre un tableau à partir d'une image. Il devra pouvoir dessiner un sketch du tableau, puis le remplir avec des couleurs, en donnant l'illusion d'être réalisé par un humain.

## Step 3 - Zhang Gui
Cette étape est la suite directe de l'étape 2. Maintenant que les contours de notre image sont bien déterminés, notre agent va devoir les redessiner par lui-même.

## Utilisation :
Notre programme prend en paramètre une valeur indiquée par l'utilisateur pour décider d'appliquer ou non un flou, ainsi que l'intensité du flou. Trois types de flous sont disponibles, comme vu dans l'étape 2. Pour la suite de ces étapes, nous utiliserons un flou gaussien d'intensité 3. Dorénavant, le programme demande également en paramètre la vitesse d'animation (-as pour animation speed) :
```bash
python Step3.py -fi licorne.png -gb 3 -as [pixel_avant_refresh]
```

Si aucun tag n'est renseigné, le programme s'arrête en demandant de relancer avec le tag souhaité.
La valeur renseignée après le tag correspond au nombre de pixels à dessiner avant chaque update graphique. Plus elle est élevée, plus l'image se terminera rapidement, mais plus l'animation sera saccadée.

## Dépendances :
Les seules dépendances nécessaires sont celles déjà présentes depuis l'étape 1 :
* `numpy==1.26.2`
* `opencv-python==4.8.1.78`  

Aucune librairie supplémentaire n'est utilisée, car turtle est présent dès l'installation de python.

## L'animation by turtle
Pour débuter cette étape, nous partons de l'array numpy de la fin de l'étape deux. Cette array liste tous les pixels de l'image, plaçant un 255 pour un pixel blanc et un 0 pour un pixel noir. Le stylo est donc levé, et à chaque 0 trouvé dans le tableau un point est placé grâce à turtle.dot(). Un paramètre de 2 pour l'épaisseur à été choisie comme étant corecte, mais elle serait également facilement paramétrable.  
Le turtle.goto() ne prend pas directement x et y, mais s'adapte au fait que le 0,0 est en haut à gauche pour l'array ou au centre pour turtle.  
Enfin, un compteur sur la boucle qui parcourt l'array permet de savoir combien de pixel a été dessiné, et d'actualiser l'image quand le nombre de pixel requis est atteint.    


## Exécution :
Le script charge l'image spécifiée (lion ou licorne), applique le flou choisi par l'utilisateur, utilise la détection de contours de Canny puis utilise turtle pour dessiner ces contours comme sur une feuille blanche pour produire l'animation finale.
Exemple qui nous parait optimal :
```bash
python Step3.py -fi licorne.png -gb 3 -as 100
```

## Conclusion :
Dans cette troisième étape, nous avons commencé à produire un premier croquis basé sur l'analyse des étapes précédentes. Cette étape constitue une avancée importante vers la création d'un agent capable de produire des peintures à partir d'images, c'est la première brique du dessin final.