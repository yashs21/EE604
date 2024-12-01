import cv2
import numpy as np
import matplotlib.pyplot as plt

    


flag= cv2.imread("1.png")
print(flag[300, 300, 2])
img = flag[:, :, [2, 1, 0]] #
cv2.imshow("Indian Flag", img)
cv2.imwrite("indian_flag.jpg", img)  # Save the flag as an image
cv2.waitKey(0)
cv2.destroyAllWindows()
