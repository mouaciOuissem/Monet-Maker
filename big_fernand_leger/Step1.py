import cv2
import numpy as np
import sys

file_tag = "-fi"

def canny_edge_detection(image, sigma=0.33):
    # Calculating the median of the image, and applying it with the Otsu method
    # to find the best thresholds for the canny edge detection.
    v = np.median(image)
    lower_thresh = int(max(0, (1.0 - sigma) * v))
    upper_thresh = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower_thresh, upper_thresh)
    
    return edged

def inverse_binary_threshold(image):
    # Inverting black and white
    return cv2.bitwise_not(image)

# Uploading the image
if (file_tag in str(sys.argv)):
    image_path = sys.argv[sys.argv.index(file_tag) + 1]
else :
    print("You didn't specify the image you want to work on. Please add the tag '-fi' followed by the image file name.")
    exit()

image = cv2.imread(image_path)

edges = canny_edge_detection(image)
final = inverse_binary_threshold(edges)

# Affichage des résultats
cv2.imshow("Original", image)
cv2.imshow("Canny Edges", final)
cv2.waitKey(0)
cv2.destroyAllWindows()