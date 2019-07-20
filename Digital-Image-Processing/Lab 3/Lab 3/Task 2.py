import cv2
from matplotlib import pyplot as plt

def show_hist(path):
    img = cv2.imread(path, 0)
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()

show_hist("B1.png")
show_hist("B2.jpg")
show_hist("B3.jpg")