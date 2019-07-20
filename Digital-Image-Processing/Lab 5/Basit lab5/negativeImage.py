#import cv2 as cv
import numpy as np
import PIL
from PIL import Image


def rgbToNegative(im):
    numrows=im1.shape[0]
    numcols=im1.shape[1]
    new_img=np.zeros((numrows,numcols,3),dtype=np.uint8)
    
    for i in range(numrows):
        for j in range(numcols):
            new_img[i][j][0]=255-im1[i][j][0]
            new_img[i][j][1]=255-im1[i][j][1]
            new_img[i][j][2]=255-im1[i][j][2]
    return new_img

def grayToNegative(im1):
    
    numrows=im1.shape[0]
    numcols=im1.shape[1]
    new_img=np.zeros((numrows,numcols),dtype=np.uint8)
    
    for i in range(numrows):
        for j in range(numcols):
            new_img[i][j]=255-im1[i][j]
    return new_img

def toBinary(im_2):
    numrows=im_2.shape[0]
    numcols=im_2.shape[1]
    new_img1=np.zeros((numrows,numcols),dtype=np.uint8)
    for i in range(numrows):
        for j in range(numcols):
            if(im_2[i][j]>=130):
                new_img1[i][j]=0
            else:
                new_img1[i][j]=255
    return new_img1


#open the image
#img = cv.imread('lena_color.jpg',0)
img = Image.open('lena_color.jpg')
#binary_negative=np.invert(im1)
option=input("1.RGB inversion\n2.grayscale\n3.binary")


if(option==1):
    
    im1=np.asarray(img)
    rgb_negative=rgbToNegative(im1)
    rgb=Image.fromarray(rgb_negative)
    rgb.show()
    rgb.save("rgb.jpg")
elif(option==2):
    img=img.convert('L')
    im1=np.asarray(img)
    gray_negative=grayToNegative(im1)
    gray=Image.fromarray(gray_negative)
    gray.show()
    gray.save("graya.png")
else:
    im1=img.convert('L')
    im2=np.asarray(im1)
    bn=toBinary(im2)
    bnp=Image.fromarray(bn)
    bnp.show()
    bnp.save("Binary.jpg")
