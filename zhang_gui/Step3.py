import cv2
import numpy as np
import sys
import turtle



file_tag = "-fi"
gaussian_tag = "-gb"
box_blur_tag = "-bb"
median_blur_tag = "-mb"
animation_speed_tag = "-as"

def canny_edge_detection(image, sigma=0.33):
    v = np.median(image)
    lower_thresh = int(max(0, (1.0 - sigma) * v))
    upper_thresh = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower_thresh, upper_thresh)
    return edged

def inverse_binary_threshold(image):
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

def draw_contours_turtle(image, animation_speed_tag):
    animation_speed_value = int(sys.argv[sys.argv.index(animation_speed_tag) + 1])
    turtle.Turtle(visible=False)
    turtle.hideturtle()
    turtle.tracer(0, 0) # No automatic update
    turtle.bgcolor("white")
    turtle.pencolor("black")
    turtle.pensize(2)
    turtle.penup()
    
    height, width = image.shape
    cpt = 0
    for y in range(height):
        for x in range(width):
            if image[y, x] == 0: # If the pixel should be black
                cpt += 1
                
                turtle.goto(x - width // 2, height // 2 - y)
                turtle.dot(2)

                # Update the window according to parameter
                if cpt == animation_speed_value:
                    turtle.update()
                    cpt = 0

    turtle.Screen().exitonclick()


# Uploading the image
if (file_tag in str(sys.argv)):
    image_path = sys.argv[sys.argv.index(file_tag) + 1]
else :
    print("You didn't specify the image you want to work on. Please add the tag '-fi' followed by the image file name.")
    exit()
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if (gaussian_tag in str(sys.argv)):
    image_blur = gaussian_blur(image, sys.argv, gaussian_tag)
    edges = canny_edge_detection(image_blur)
elif (box_blur_tag in str(sys.argv)):
    image_blur = box_blur(image, sys.argv, box_blur_tag)
    edges = canny_edge_detection(image_blur)
elif (median_blur_tag in str(sys.argv)):
    image_blur = median_blur(image, sys.argv, median_blur_tag)
    edges = canny_edge_detection(image_blur)
else:
    edges = canny_edge_detection(image)

final = inverse_binary_threshold(edges)

# Affichage des résultats avec Turtle
if (animation_speed_tag in str(sys.argv)):
    draw_contours_turtle(final, animation_speed_tag)
else:
    print("No animation speed was given. Please add the flag -as followed by the number of pixel to draw before each update. The more updates you ask, the slower it gets.")
    exit()
