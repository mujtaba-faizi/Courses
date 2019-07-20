import webcolors
import cv2
import numpy as np


img = cv2.imread('objects.png')
gray = cv2.imread('objects.png',0)
ret3, segmented = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
kernel = np.ones((5,5), np.uint8)
img_erosion = cv2.erode(segmented, kernel, iterations=1)
img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)
cv2.imshow('Segmentation',img_dilation)
ret, labels = cv2.connectedComponents(img_dilation)

# Map component labels to hue val
label_hue = np.uint8(179*labels/np.max(labels))
blank_ch = 255*np.ones_like(label_hue)
labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
cv2.imshow('labeled.png', labeled_img)

# cvt to BGR for display
labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

# set bg label to black
labeled_img[label_hue==0] = 0
cv2.imshow('labeled.png', labeled_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
