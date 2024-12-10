import numpy as np
import cv2
import turtle
from scipy.spatial import cKDTree
import sys

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

def gaussian_blur(image, gaussian_tag):
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

def box_blur(image, box_blur_tag):
    # Perform the blur at the intensity of the value given after the box blur tag
    blur_intensity_index = int(sys.argv[sys.argv.index(box_blur_tag) + 1])
    if blur_intensity_index < 0:
        print(f"intensité  de flou incorrecte (inférieure à 0) : {blur_intensity_index}")
        blur_intensity_index = 1
        print(f"intensité  de flou ramenée à {blur_intensity_index}")
    return cv2.boxFilter(image, -1, (blur_intensity_index, blur_intensity_index))

def median_blur(image, median_blur_tag):
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

def get_starting_pixel(image, width, height):
    for i in range(height):
        for j in range(width):
            if image[i, j] == 0:
                if(has_neighbour(image, height, width, i, j)):
                    return (j, i)
            
    return None

def has_neighbour(image, height, width, i, j):
    if i > 0 and image[i - 1, j] == 0: 
        return True
    elif i < height - 1 and image[i + 1, j] == 0:
        return True
    elif j > 0 and image[i, j - 1] == 0: 
        return True
    elif j < width - 1 and image[i, j + 1] == 0:
        return True
    return False

def draw_image_mine(image, animation_speed_tag):
    animation_speed_value = int(sys.argv[sys.argv.index(animation_speed_tag) + 1])
    turtle.Turtle(visible=False)
    turtle.hideturtle()
    turtle.tracer(0, 0) # No automatic update
    turtle.bgcolor("white")
    turtle.pencolor("black")
    turtle.penup()

    ret, bw_img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    width = int(image.shape[1])
    height = int(image.shape[0])

    turtle.screensize(width, height)

    starting_pixel = get_starting_pixel(bw_img, width, height)
    if starting_pixel is None:
        print("No starting pixel found.")
        return

    remaining_pixels = np.column_stack(np.where(bw_img == 0))
    remaining_pixels_tree = cKDTree(remaining_pixels)

    current_pixel = starting_pixel
    turtle.goto(current_pixel[1] - height // 2, width // 2 - current_pixel[0])

    cpt = 0
    while remaining_pixels.size > 0:
        _, index = remaining_pixels_tree.query(current_pixel)
        nearest_pixel = remaining_pixels_tree.data[index]

        if np.linalg.norm(current_pixel - nearest_pixel) <= 4 and final[int(nearest_pixel[0]), int(nearest_pixel[1])] == 0:
            turtle.goto(nearest_pixel[1] - height // 2, width // 2 - nearest_pixel[0])
            remaining_pixels_tree = cKDTree(np.delete(remaining_pixels_tree.data, index, axis=0))
            remaining_pixels = np.delete(remaining_pixels, index, axis=0)
            current_pixel = nearest_pixel
            turtle.pendown()
            if cpt % animation_speed_value == 0:
                turtle.update()
                cpt = 0
        else:
            turtle.penup()
            turtle.goto(nearest_pixel[1] - height // 2, width // 2 - nearest_pixel[0])
            current_pixel = nearest_pixel
        cpt += 1
    turtle.done()

if (file_tag in str(sys.argv)):
    image_path = sys.argv[sys.argv.index(file_tag) + 1]
else :
    print("You didn't specify the image you want to work on. Please add the tag '-fi' followed by the image file name.")
    exit()
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if (gaussian_tag in str(sys.argv)):
    image_blur = gaussian_blur(image, gaussian_tag)
    edges = canny_edge_detection(image_blur)
elif (box_blur_tag in str(sys.argv)):
    image_blur = box_blur(image, box_blur_tag)
    edges = canny_edge_detection(image_blur)
elif (median_blur_tag in str(sys.argv)):
    image_blur = median_blur(image, median_blur_tag)
    edges = canny_edge_detection(image_blur)
else:
    edges = canny_edge_detection(image)

final = inverse_binary_threshold(edges)

if (animation_speed_tag in str(sys.argv)):
    draw_image_mine(final, animation_speed_tag)
else:
   print("No animation speed was given. Please add the flag -as followed by the number of pixel to draw before each update. The more updates you ask, the slower it gets.")
   exit()
