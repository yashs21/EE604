import cv2
import numpy as np

def is_sun_present(image_path, sun_threshold=0.01):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (15, 15), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred_image, 30, 100)

    # Find contours in the edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on area and circularity
    min_contour_area = 100
    max_contour_area = 5000
    min_circularity = 0.8

    filtered_contours = [
        contour for contour in contours
        if min_contour_area < cv2.contourArea(contour) < max_contour_area
        and cv2.matchShapes(contour, cv2.approxPolyDP(contour, 0.03 * cv2.arcLength(contour, True), True), 2, 0.0) < min_circularity
    ]

    # If filtered contours are detected, consider the sun present
    if filtered_contours:        
        return True

    return False

# Example usage:
image_path = 'lava25.jpg'
result = is_sun_present(image_path)

if result:
    print("Sun is present in the image.")
else:
    print("Sun is not present in the image.")
