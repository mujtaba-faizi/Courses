import cv2
from skimage.util import random_noise
from matplotlib import pyplot

image = cv2.imread('lena.jpg',0)

img = random_noise(image, mode='gaussian', seed=None, clip=True)
pyplot.imshow(img, cmap='gray')
pyplot.imsave("Task1_Gaussian.jpg", img, cmap='gray')

img = random_noise(image, mode='s&p', seed=None, amount=0.15,salt_vs_pepper=0.25)
pyplot.imshow(img)
pyplot.imsave("Task1_Salt&pepper.jpg", img, cmap='gray')

img = random_noise(image, mode='speckle', seed=None, mean=0.1,var=0.02)
pyplot.imshow(img, cmap='gray')
pyplot.imsave("Task1_Speckle.jpg", img, cmap='gray')




