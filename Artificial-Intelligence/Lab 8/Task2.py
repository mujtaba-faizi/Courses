from PIL import Image
import numpy as np
from scipy.misc import imshow
from scipy.misc import toimage


def rgb_to_gray(img):
    img=np.array(im)
    grayImage = np.zeros(img.shape)
    R = np.array(img[:, :, 0])
    G = np.array(img[:, :, 1])
    B = np.array(img[:, :, 2])

    R = (R * .299)
    G = (G * .587)
    B = (B * .114)

    Avg = (R + G + B)
    grayImage = img

    for i in range(3):
        grayImage[:, :, i] = Avg

    return grayImage

im = Image.open('F:\Pics & Videos\NUST Events 2017\CS-5A\_DSC6837(1).jpg')
grayImage = rgb_to_gray(im)
toimage(grayImage).show()
