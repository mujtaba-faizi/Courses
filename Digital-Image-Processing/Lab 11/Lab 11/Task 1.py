import cv2
import numpy as np

img=cv2.imread("ThumbImpression.png",0)
img=255-img   #negative

size = np.size(img)
skel = np.zeros(img.shape, np.uint8)

ret, img = cv2.threshold(img, 127, 255, 0)
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
done = False

while (not done):    #skeletanization
    eroded = cv2.erode(img, element)
    temp = cv2.dilate(eroded, element)
    temp = cv2.subtract(img, temp)
    skel = cv2.bitwise_or(skel, temp)
    img = eroded.copy()

    zeros = size - cv2.countNonZero(img)
    if zeros == size:
        done = True

kernel = np.ones((1,1), np.uint8)

skel = cv2.dilate(skel, kernel, iterations=4)   #dilation
skel=255-skel   #negative
cv2.imwrite("skel.jpg", skel)



cv2.waitKey(0)
cv2.destroyAllWindows()