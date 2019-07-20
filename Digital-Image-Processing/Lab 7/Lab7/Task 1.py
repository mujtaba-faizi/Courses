from matplotlib import pyplot as plt
import numpy as np
import cv2
from PIL import Image

def show_hist(img):   #to show histograms
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()

img = cv2.imread('lab07.jpg',0)
cv2.imshow('image',img)
show_hist(img)
equ = cv2.equalizeHist(img)
cv2.imshow('image',equ)
show_hist(equ)
