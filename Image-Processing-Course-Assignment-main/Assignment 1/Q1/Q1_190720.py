import cv2
import numpy as np
import matplotlib.pyplot as plt

def solution(image_path):
    image= cv2.imread(image_path)
    blue_channel, green_channel, red_channel = cv2.split(image)
    height, width = red_channel.shape
    vertical=1
    right=1
    upper=1
    
    for x in range(50):
        for y in range(width):
            red = red_channel[x,y]
            green = green_channel[x,y]
            blue = blue_channel[x,y]
            
            if red==0 and blue==0 and green ==0:
                continue
            if red==255 and blue==255 and green==255:
                vertical=0
    
    if vertical==1:
        for x in range(50):
            for y in range(width):
                red = red_channel[x,y]
                green = green_channel[x,y]
                blue = blue_channel[x,y]
                
                if red==0 and blue==0 and green==0:
                    continue
                if red==0 and blue==0 and green>0:
                    upper=0
                    
    else:
        for x in range(height):
            for y in range(50):
                red = red_channel[y,x]
                green = green_channel[y,x]
                blue = blue_channel[y,x]
                  
                if red==0 and blue==0 and green ==0:
                    continue
                if red==0 and blue==0 and green>0:
                    right=0
    
    flag = np.ones((600, 600, 3), dtype=np.uint8) * 255

    saffron = (255, 153, 51)
    green = (0, 128, 0)
    white = (255, 255, 255)
    blue = (0, 0, 255)

    stripe_height = 600 // 3

    flag[:stripe_height] = saffron
    flag[stripe_height:2 * stripe_height] = white
    flag[2 * stripe_height:] = green

    center_x, center_y = 300, 300
    circle_radius = 100
    circle_width = 2
    spoke_width = 1

    cv2.circle(flag, (center_x, center_y), 99, blue, 2)

    for i in range(24):
        for j in range(1,circle_radius-2):
            angle = np.deg2rad(i * 15)  
            x1 = int(center_x + (j - circle_width // 2) * np.cos(angle))
            y1 = int(center_y + (j - circle_width // 2) * np.sin(angle))
            x2 = int(center_x + (j + circle_width // 2) * np.cos(angle))
            y2 = int(center_y + (j + circle_width // 2) * np.sin(angle))
            cv2.line(flag, (x1, y1), (x2, y2), blue, spoke_width)
    
    if vertical==1 and upper==1:
        return flag
    elif vertical==1 and upper==0:
        flag_cw_180 = cv2.rotate(flag, cv2.ROTATE_180)
        return flag_cw_180
    elif vertical==0 and right==1:
        flag_ccw_90 = cv2.rotate(flag, cv2.ROTATE_90_COUNTERCLOCKWISE)
        return flag_ccw_90
    elif vertical==0 and right==0:
        flag_cw_90 = cv2.rotate(flag, cv2.ROTATE_90_CLOCKWISE)
        return flag_cw_90