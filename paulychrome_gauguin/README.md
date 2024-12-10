## Etape5 : paulychrome_gauguin
## Objectif
L'objectif de cette étape est d'appliquer des couleurs à l'image générée par notre agent de dessin. Nous utiliserons des techniques de machine learning, en particulier la classification ou le clustering, pour déterminer une palette de couleurs et attribuer ces couleurs à chaque pixel de l'image.

## Dépendances
Assurez-vous d'avoir les bibliothèques Python nécessaires installées en utilisant le fichier requirements.txt. Vous pouvez les installer en exécutant la commande suivante :

```bash

pip install -r requirements.txt
```
Les dépendances principales pour cette étape incluent :

OpenCV (cv2)
NumPy (numpy)
scikit-learn (sklearn)

## Utilisation
Pour exécuter le script, utilisez la commande suivante dans votre terminal ou invite de commande :

```bash
python step5.py -fi chemin/vers/votre/image.jpg -cl nombre_de_clusters
```

-fi : spécifiez le chemin de l'image que vous souhaitez coloriser.
-cl : (optionnel) déterminez le nombre de clusters (couleurs) à utiliser.

## Exécution
```bash
python step5.py -fi licorne.png -cl 8
```
Cela colorisera l'image "licorne.png" avec une palette de 8 couleurs.

## Conclusion
Dans cette étape du projet "Baulychrome Gauguin", nous avons réussi à apporter une touche de couleur à nos créations artistiques générées par l'agent de dessin. En utilisant des techniques de machine learning, nous avons exploré deux approches principales : la classification et le clustering.