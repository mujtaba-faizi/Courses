import numpy as np
import cv2

img = cv2.imread('Task2.png',0)
kernel = np.ones((5,5), np.uint8)
ret,thresh_img = cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)
img_erosion = cv2.erode(thresh_img, kernel, iterations=1)
img_dilation = cv2.dilate(thresh_img, kernel, iterations=1)
cv2.imshow("dd",img_dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()