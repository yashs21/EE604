import cv2
import numpy as np

def is_sun_present(image_path, sun_threshold=0.01):
    image = cv2.imread(image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred_image = cv2.GaussianBlur(gray_image, (15, 15), 0)

    edges = cv2.Canny(blurred_image, 30, 100)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    min_contour_area = 100
    max_contour_area = 5000
    min_circularity = 0.8

    filtered_contours = [
        contour for contour in contours
        if min_contour_area < cv2.contourArea(contour) < max_contour_area
        and cv2.matchShapes(contour, cv2.approxPolyDP(contour, 0.03 * cv2.arcLength(contour, True), True), 2, 0.0) < min_circularity
    ]
    if filtered_contours:        
        return True

    return False

def solution(image_path):
    image= cv2.imread(image_path)
    result=is_sun_present(image_path)
    if result:
        height, width, back = image.shape
        black_image = np.zeros((height, width), dtype=np.uint8)
        return black_image
    else:  
      hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


      lower_threshold = np.array([0, 120, 70])  
      upper_threshold = np.array([20, 255, 255]) 

    
      lava_mask = cv2.inRange(hsv_image, lower_threshold, upper_threshold)

    
      kernel = np.ones((5, 5), np.uint8)
      lava_mask = cv2.morphologyEx(lava_mask, cv2.MORPH_CLOSE, kernel)
      lava_mask = cv2.morphologyEx(lava_mask, cv2.MORPH_OPEN, kernel)

   
      contours, _ = cv2.findContours(lava_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
      min_contour_area = 500  

   
      lava_detected_mask = np.zeros_like(image)

    
      for contour in contours:
          if cv2.contourArea(contour) > min_contour_area:
              cv2.drawContours(lava_detected_mask, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)
    
      return lava_detected_mask

