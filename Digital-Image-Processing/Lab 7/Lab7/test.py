from matplotlib import pyplot as plt
import numpy as np
import cv2
def show_hist(img):   #to show histograms
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()
def equalize(img):
    return cv2.equalizeHist(img)

def tiling(tiles):
    arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    img2=np.array(arr * 255, dtype=np.uint8)
    show_hist(img2)
    print(arr)
    rows = arr.shape[0]  # width & height of the image i.e. no. of pixels
    cols = arr.shape[1]
    b=arr[0:2,0:2]
    im = np.array(b * 255, dtype=np.uint8)

    arr[0:2, 0:2] = np.asarray(equalize(im))
    show_hist(arr)
    return arr

c=tiling(4)
print (c)
