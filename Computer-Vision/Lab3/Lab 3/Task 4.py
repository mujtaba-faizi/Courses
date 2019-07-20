import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.png', 0)

gaus = cv2.GaussianBlur(img,(3,3),0)
blur = cv2.GaussianBlur(img,(5,5),0)
blur2 = cv2.GaussianBlur(img,(15,15),0)
edge1 = blur - blur2
edge2 = blur2 - blur

laplacian = cv2.Laplacian(gaus,cv2.CV_64F)  #laplacian of the gaussian of the image

sobelx = cv2.Sobel(gaus,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(gaus,cv2.CV_64F,0,1,ksize=5)  # y
sobel=sobelx+sobely # x and y combined

edges = cv2.Canny(img,100,200)  #canny edge detetection

plt.subplot(2,2,1),plt.imshow(edge1, cmap='gray'),plt.title('Edges (Blur1-Blur2)')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(sobel,cmap = 'gray')
plt.title('Sobel XY'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(edges,cmap = 'gray')
plt.title('Canny Edge Detetection'), plt.xticks([]), plt.yticks([])

plt.show()