import cv2
import numpy as np
from sklearn.cluster import KMeans
import sys

file_tag = "-fi"
colorize_tag = "-cl"

def apply_color(image, k=5):
    pixels = image.reshape((-1, 3))
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)
    centers = kmeans.cluster_centers_.astype(int)
    labels = kmeans.labels_
    segmented_image = centers[labels].reshape(image.shape)
    return segmented_image

if file_tag in sys.argv:
    image_path = sys.argv[sys.argv.index(file_tag) + 1]
else:
    print("You didn't specify the image you want to work on. Please add the tag '-fi' followed by the image file name.")
    exit()

image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

if colorize_tag in sys.argv:
    k_value = int(sys.argv[sys.argv.index(colorize_tag) + 1])
    colorized_image = apply_color(image_rgb, k_value)
else:
    colorized_image = apply_color(image_rgb)

# Convertir l'image colorisée en type de données np.uint8
colorized_image_uint8 = colorized_image.astype(np.uint8)

# Afficher l'image convertie
cv2.imshow("Original Image", cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR))
cv2.imshow("Colorized Image", cv2.cvtColor(colorized_image_uint8, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()
