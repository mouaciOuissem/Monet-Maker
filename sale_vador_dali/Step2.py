import cv2
import numpy as np
import sys

file_tag = "-fi"
gaussian_tag = "-gb"
box_blur_tag = "-bb"
median_blur_tag = "-mb"

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

def gaussian_blur(image, list_argv, gaussian_tag):
    # Perform the blur at the intensity of the value given after the gaussian tag
    blur_intensity_index = int(sys.argv[sys.argv.index(gaussian_tag) + 1])
    if blur_intensity_index < 0:
        print(f"intensité  de flou incorrecte (inférieure à 0) : {blur_intensity_index}")
        blur_intensity_index = 1
        print(f"intensité  de flou ramenée à {blur_intensity_index}")
    elif blur_intensity_index % 2 == 0:
        print(f"intensité  de flou incorrecte (impaire) : {blur_intensity_index}")
        blur_intensity_index += 1
        print(f"intensité  de flou ramenée à {blur_intensity_index}")
    return cv2.GaussianBlur(image, (blur_intensity_index, blur_intensity_index), 0) 

def box_blur(image, list_argv, box_blur_tag):
    # Perform the blur at the intensity of the value given after the box blur tag
    blur_intensity_index = int(sys.argv[sys.argv.index(box_blur_tag) + 1])
    if blur_intensity_index < 0:
        print(f"intensité  de flou incorrecte (inférieure à 0) : {blur_intensity_index}")
        blur_intensity_index = 1
        print(f"intensité  de flou ramenée à {blur_intensity_index}")
    return cv2.boxFilter(image, -1, (blur_intensity_index, blur_intensity_index))

def median_blur(image, list_argv, median_blur_tag):
    # Perform the blur at the intensity of the value given after the median blur tag
    blur_intensity_index = int(sys.argv[sys.argv.index(median_blur_tag) + 1])
    if blur_intensity_index < 0:
        print(f"intensité  de flou incorrecte (inférieure à 0) : {blur_intensity_index}")
        blur_intensity_index = 1
        print(f"intensité  de flou ramenée à {blur_intensity_index}")
    elif blur_intensity_index % 2 == 0:
        print(f"intensité  de flou incorrecte (impaire) : {blur_intensity_index}")
        blur_intensity_index += 1
        print(f"intensité  de flou ramenée à {blur_intensity_index}")
    return cv2.medianBlur(image, blur_intensity_index)


# Uploading the image
if (file_tag in str(sys.argv)):
    image_path = sys.argv[sys.argv.index(file_tag) + 1]
else :
    print("You didn't specify the image you want to work on. Please add the tag '-fi' followed by the image file name.")
    exit()
image = cv2.imread(image_path)

if (gaussian_tag in str(sys.argv)):
    image_blur = gaussian_blur(image, sys.argv, gaussian_tag)
    edges = canny_edge_detection(image_blur)
elif (box_blur_tag in str(sys.argv)):
    image_blur = box_blur(image, sys.argv, box_blur_tag)
    edges = canny_edge_detection(image_blur)
elif (median_blur_tag in str(sys.argv)):
    image_blur = median_blur(image, sys.argv, median_blur_tag)
    edges = canny_edge_detection(image_blur)
else :
    edges = canny_edge_detection(image)



final = inverse_binary_threshold(edges)

# Affichage des résultats
cv2.imshow("Original", image)
cv2.imshow("Canny Edges", final)
cv2.waitKey(0)
cv2.destroyAllWindows()
