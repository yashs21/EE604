import cv2
import numpy as np
import matplotlib.pyplot as plt

def solution(image_path):
    input_image = cv2.imread(image_path)
    grayscale_image =cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)

    edges = cv2.Canny(blurred_image, 50, 150, apertureSize=3)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)

    angles = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))
        angles.append(angle)
    avg_angle = np.mean(angles)
    if avg_angle<0:
        avg_angle=180+avg_angle+3.0
    borderValue=(255, 255, 255)
    image_center = tuple(np.array(input_image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, avg_angle, 1.0)
    result = cv2.warpAffine(input_image, rot_mat, input_image.shape[1::-1], flags=cv2.INTER_LINEAR, borderValue=borderValue)
    return result