## Introduction - Monet Maker
Ce projet a pour but de créer un agent pouvant peindre un tableau à partir d'une image. Il devra pouvoir dessiner un sketch du tableau, puis le remplir avec des couleurs, en donnant l'illusion d'être réalisé par un humain.

## Step 2 - Sale Vador Dali

Cette étape vise à améliorer l'isolation des contours de l'image en effectuant un pré-traitement qui consiste à appliquer un flou sur certaines parties de l'image. Cette approche permet de résoudre le problème des images trop détaillées, où le rendu des contours est trop chargé.

## Utilisation :
Notre programme prend en paramètre une valeur indiquée par l'utilisateur pour décider d'appliquer ou non un flou, ainsi que l'intensité du flou. Trois types de flous sont disponibles :
1. Flou Gaussien (-gb):
```bash
python Step2.py -fi licorne.png -gb [intensité]
```
2.Flou Encadré (-bb):
```bash
python Step2.py -fi licorne.png -bb [intensité]
```

3.Flou Médian (-mb):
```bash
python Step2.py -fi licorne.png -mb [intensité]
```
Si aucun tag n'est renseigné, aucun flou n'est appliqué, et Step2 est donc le même que Step1.  
Comme dans la Step1, l'image utilisée doit être passée en argument (-licorne ou -lion).

## Dépendances :
Les seules dépendances nécessaires sont celles déjà présentes depuis l'étape 1 :
* `numpy==1.26.2`
* `opencv-python==4.8.1.78`
Aucune librairie supplémentaire n'est utilisée, car les flous sont déjà implémentés dans OpenCV.

## Implémentation des Flous :
Trois types de flous ont été implémentés :
1. Flou Gaussien:
* Implémenté avec `cv2.GaussianBlur`.
* L'utilisateur doit spécifier l'intensité du flou après le tag `-gb`. Cette intensité se doit d'être impaire et supérieure à 0. Si elle est inférieure à 0, elle sera ramenée à 1, et si elle est paire, elle sera augmentée de 1.

2. Flou Encadré:
* Implémenté avec `cv2.boxFilter`.
* L'utilisateur doit spécifier l'intensité du flou après le tag `-bb`. Cette intensité se doit d'être supérieure à 0. Si elle est inférieure à 0, elle sera ramenée à 1.

3. Flou Médian:
Implémenté avec `cv2.medianBlur`.
L'utilisateur doit spécifier l'intensité du flou après le tag `-mb`. Cette intensité se doit d'être impaire et supérieure à 0. Si elle est inférieure à 0, elle sera ramenée à 1, et si elle est paire, elle sera augmentée de 1.

## Priorité des Flous :
Si plusieurs tags sont présents, le flou gaussien a la priorité, suivi du flou encadré, et enfin du flou médian.

Après quelques tests, il semble que le flou encadré ait une intensité de base plus forte. Un flou gaussien d'intensité 5 équivaudrait à un flou encadré d'intensité 3, et à un flou médian d'intensité 5 également.

## Exécution :
Le script charge l'image spécifiée (lion ou licorne), applique le flou choisi par l'utilisateur, puis utilise la détection de contours de Canny pour produire un résultat final.
```bash
python Step2.py -fi licorne.png -gb 5
```
L'image originale et les contours détectés par Canny sont affichés pour évaluation.

## Conclusion :
Dans cette deuxième étape, nous avons renforcé le pré-traitement de l'image en introduisant des techniques de floutage pour gérer les détails excessifs. Les flous gaussien, encadré et médian sont disponibles, offrant à l'utilisateur une flexibilité dans le choix du pré-traitement. Notre approche met l'accent sur la simplicité en utilisant efficacement les fonctionnalités d'OpenCV, tout en maintenant des dépendances minimales. L'ordre de priorité des flous a été défini pour gérer les cas où plusieurs tags sont présents. Cette étape constitue une avancée importante vers la création d'un agent capable de produire des peintures à partir d'images, avec un processus de pré-traitement plus robuste.