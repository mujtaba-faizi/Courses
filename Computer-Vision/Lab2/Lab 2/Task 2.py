import cv2
import numpy as np

def median(img, ksize=3, title='Median Filter Result', show=1):
    # Median filter function provided by OpenCV. ksize is the kernel size.
    img = cv2.medianBlur(img, ksize)
    return img

def mean(image):
    # apply the 3x3 mean filter on the image
    kernel = np.ones((3,3),np.float32)/9
    processed_image = cv2.filter2D(image,-1,kernel)
    return processed_image

img1 = cv2.imread('Task1_Gaussian.jpg',0) # Only for grayscale image
img2 = cv2.imread('Task1_Salt&pepper.jpg',0) # Only for grayscale image
img3 = cv2.imread('Task1_Speckle.jpg',0) # Only for grayscale image

img=median(img1)
cv2.imshow('Median filter', img)
cv2.waitKey(0)
cv2.imwrite('Task2_Gaussian_Median-Filter.png',img)

img=mean(img1)
cv2.imshow('Mean filter', img)
cv2.waitKey(0)
cv2.imwrite('Task2_Gaussian_Mean-Filter.png',img)

img=median(img2)
cv2.imshow('Median filter', img)
cv2.waitKey(0)
cv2.imwrite('Task2_Salt&pepper_Median-Filter.png',img)

img=mean(img2)
cv2.imshow('Mean filter', img)
cv2.waitKey(0)
cv2.imwrite('Task2_Salt&pepper_Mean-Filter.png',img)

img=median(img3)
cv2.imshow('Median filter', img)
cv2.waitKey(0)
cv2.imwrite('Task2_Speckle_Median-Filter.png',img)

img=mean(img3)
cv2.imshow('Mean filter', img)
cv2.waitKey(0)
cv2.imwrite('Task2_Speckle_Mean-Filter.png',img)

