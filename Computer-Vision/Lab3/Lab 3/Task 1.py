import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.png', 0)
blur = cv2.GaussianBlur(img,(5,5),0)
blur2 = cv2.GaussianBlur(img,(15,15),0)

edge1 = blur - blur2
edge2 = blur2 - blur

plt.subplot(2,2,1),plt.imshow(blur, cmap='gray'),plt.title('Blur1(5x5)')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(blur2, cmap='gray'),plt.title('Blur2 (15x15)')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(edge2, cmap='gray'),plt.title('Edges (Blur2-Blur1)')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(edge1, cmap='gray'),plt.title('Edges (Blur1-Blur2)')
plt.xticks([]), plt.yticks([])

plt.show()
