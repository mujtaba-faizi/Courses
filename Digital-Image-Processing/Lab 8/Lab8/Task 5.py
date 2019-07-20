import cv2
import numpy as np

img = cv2.imread('two_cats.jpg',0)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)   #vertical edges by calculating gradient along x axis
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)   #horizontal edges by calculating gradient along y axis
arr1 = np.asarray(sobelx)
arr2 = np.asarray(sobely)
cv2.imwrite('Sharpening filter.jpg', np.add(arr1,arr2))

