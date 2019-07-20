import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('1.png',0)
img2 = cv2.imread('2.png',0)

edges1 = cv2.Canny(img1,10,20)
edges2 = cv2.Canny(img2,10,20)

code = cv2.bitwise_and(edges1, edges2)  #common edges between both images

plt.subplot(2,2,1),plt.imshow(edges1, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(edges2, cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(code, cmap = 'gray')
plt.title('Secret Code'), plt.xticks([]), plt.yticks([])

plt.show()
