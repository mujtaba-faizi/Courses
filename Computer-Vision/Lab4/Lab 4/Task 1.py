import cv2
import numpy as np
from matplotlib import pyplot as plt

#we convert to grayscale to increase the processing speed
img = cv2.imread('lena.png' ,0)
gray = np.float32(img)

dst = cv2.cornerHarris(gray,2,3,0.04)

#For every pixel p , the function cornerEigenValsAndVecs considers a blockSize * blockSize neighborhood S(p) .
#It calculates the covariation matrix of derivatives over the neighborhood
#increasing the blocksize parameter gives wider corners.
# dst = cv2.cornerHarris(gray,10,3,0.04)

#Decreasing the kernal size for sobel detector parameter gives poor results, and the best results are obtained for 3*3
# dst = cv2.cornerHarris(gray,2,1,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[255]

cv2.imshow('dst',img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

