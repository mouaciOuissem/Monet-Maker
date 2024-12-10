## Introduction - Monet Maker
Ce projet a pour but de créer un agent pouvant peindre un tableau à partir d'une image. Il devra pouvoir dessiner un sketch du tableau, puis le remplir avec des couleurs, en donnant l'illusion d'être réalisé par un humain.

## Step 1 - Big Fernand Leger
Cette étape a pour but d'analyser l'image pour en isoler les contours.

## Utilisation :
  
Pour lancer le programme, il faut placer son image au même endroit que le fichier python. Puis, se placer à l'emplacement du fichier et executer le script en passant en argument l'image à utiliser grâce au tag -fi :  
```bash
python .\Step1.py -fi [file_name]
```     
```bash
python .\Step1.py -fi lion.jpg 
```    
```bash
python .\Step1.py -fi licorne.png
```     
## Dépendances :
Pour cette étape, deux librairies sont requises : 
* `numpy==1.26.2`
* `opencv-python==4.8.1.78`  

Numpy servira à calculer une médiane des pixels de l'image afin de pratiquer la méthode de Otsu, quand opencv servira à pratique des opérations sur l'image, notamment nos deux algorithmes phares.  

## Architecture :
Deux fonctions sont créées, une pour chacun des algorithmes : le canny edge detection et le inverse binary thresholding.    

## Exécution :
Le programme commence par charger l'image souhaitée grâce à la librairie opencv, puis va directement appeler les deux fonctions réalisées en série. Selon les arguments donnés, l'image du lion ou celle de la licorne sera utilisée.  
La fonction canny edge detection de opencv a besoin de threshold pour comprendre ce qu'elle doit considérer comme étant des contours ou non. Ces thresholds sont ici calculés automatiquement grâce à la méthode Otsu, basée sur une médiane donnée par la librairie numpy. Cette méthode suppose que l'image ne contient que deux plans (le premier plan et l'arrière-plan) puis calcule le seuil optimal qui réparti chaque pixel dans chacun des plans. Ce seuil marque donc la limite entre l'avant et l'arrière, et donc les contours des objets.    
La fonction inverse binary thresholding est plus simple, elle se contente d'appeler une fonction de opencv qui va inverser les couleurs, pour passer de fond noir/contour blanc à fond blanc/contour noir.
opencv est alors utilisée une dernière fois pour afficher l'image initiale et l'image finale.

## Conclusion :
Dans cette première étape, nous chargeons l'image souhaitée, déterminons un seuil différenciant l'arrière plan du premier plan et l'utilisons au sein de l'algorithme de canny edge detection afin de tracer les contours de notre image. Finalement, afin d'obtenir une image en fond blanc et contours noirs, nous appliquons la fonction inverse binary thresholding.  
C'est la première étape vers un agent capable de produire des peintures à partir d'images : en définir les contours.