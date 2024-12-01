import cv2
import numpy as np

def bilateral_filter(image, diameter, sigma_color, sigma_space):
    height, width, channels = image.shape
    filtered_image = np.zeros_like(image, dtype=np.float64)
    y_range, x_range = np.mgrid[0:height, 0:width]

    for y in range(height):
        for x in range(width):
            y_min, y_max = max(y - diameter // 2, 0), min(y + diameter // 2 + 1, height)
            x_min, x_max = max(x - diameter // 2, 0), min(x + diameter // 2 + 1, width)
            
            local_window = image[y_min:y_max, x_min:x_max]
            spatial_weights = np.exp(-((y - y_range[y_min:y_max, x_min:x_max])**2 + 
                                       (x - x_range[y_min:y_max, x_min:x_max])**2) / (2 * sigma_space**2))
            
            intensity_weights = np.exp(-np.linalg.norm(local_window - image[y, x], axis=2)**2 / (2 * sigma_color**2))
            weights = (spatial_weights * intensity_weights).reshape(-1, 1)
            normalized_weights = weights / np.sum(weights)
            filtered_pixel = np.sum(local_window.reshape(-1, channels) * normalized_weights, axis=0)
            filtered_image[y, x] = filtered_pixel
            
    return filtered_image.astype(np.uint8)

def solution(image_path_a, image_path_b):
    flash_img = cv2.imread(image_path_a)
    no_flash_img = cv2.imread(image_path_b)

    filtered_flash_img = bilateral_filter(flash_img, diameter=9, sigma_color=75, sigma_space=75)
    filtered_no_flash_img = bilateral_filter(no_flash_img, diameter=9, sigma_color=75, sigma_space=75)

    prolight_img = 0.5 * filtered_flash_img + 0.5 * filtered_no_flash_img
    return prolight_img