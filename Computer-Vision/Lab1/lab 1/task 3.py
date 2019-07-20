from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread('4.PNG')
rows,cols,depth = img.shape
arr = np.asarray(img)
print(arr.shape)

TF = arr[int(0):int(20), int(0):int(20)]  #top left patch
cv2.imshow('Top left patch', TF)  #show the patch
cv2.imwrite('task3-1_TL.png',TF)
cv2.waitKey(0)
BR = arr[int(arr.shape[0]-20):int(arr.shape[0]), int(arr.shape[1]-20):int(arr.shape[1])]  #bottom right patch
cv2.imshow('Bottom right patch', BR)  #show the patch
cv2.imwrite('task3-1_BR.png',BR)
cv2.waitKey(0)
M = arr[int((arr.shape[0])/2):int(((arr.shape[0])/2)+20), int((arr.shape[1])/2):int(((arr.shape[1])/2)+20)]  #middle patch
cv2.imshow('Middle patch', M)  #show the patch
cv2.imwrite('task3-1_M.png',M)
cv2.waitKey(0)

arr[int(0):int(20), int(0):int(20)] = np.ones((20, 20, 3)) * [0, 0, 255]  #convert the top left patch to red
arr[int(arr.shape[0]-20):int(arr.shape[0]), int(arr.shape[1]-20):int(arr.shape[1])]= np.ones((20, 20, 3)) * [0, 255, 0]  #convert the top left patch to green
arr[int((arr.shape[0])/2):int(((arr.shape[0])/2)+20), int((arr.shape[1])/2):int(((arr.shape[1])/2)+20)]= np.ones((20, 20, 3)) * [0, 255, 255]  #convert the midle patch to yellow
cv2.imwrite('task3-2.png',img)

#Adding text to the patches
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(arr[int(0):int(20), int(0):int(20)],'TL',(0,12), font, 0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(arr[int(arr.shape[0]-20):int(arr.shape[0]), int(arr.shape[1]-20):int(arr.shape[1])],'BR',(0,12), font, 0.5,(0,0,0),2,cv2.LINE_AA)
cv2.putText(arr[int((arr.shape[0])/2):int(((arr.shape[0])/2)+20), int((arr.shape[1])/2):int(((arr.shape[1])/2)+20)],'M',(0,12), font, 0.5,(0,0,0),2,cv2.LINE_AA)
cv2.imwrite('task3-3.png',img)

#Adding the footer
cv2.rectangle(img, (1, 400), (990, 487), (0, 255, 0), 3)
cv2.circle(img,(850,450), 10, (0,255,0), -1)
cv2.putText(img,'Mujtaba Faizi',(865,455), font, 0.5,(0,255,0),2,cv2.LINE_AA)
cv2.imwrite('task3-4.png',img)

M = np.float32([[1,0,-(cols/2)+100],[0,1,0]])
img = cv2.warpAffine(img,M,(cols,rows))   #Translate the image such that the name is in the middle
cv2.imwrite('task3-5.png',img)

M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),180,1)
img = cv2.warpAffine(img,M,(cols,rows))   #Rotate the image by 180 degrees
cv2.imwrite('task3-6.png',img)

img = cv2.flip( img, 0 )  #Now flip the image upside down.
cv2.imwrite('task3-7.png',img)

img = arr[int(0):int(398), int(0):int(992)]   #image without the footer
cv2.imwrite('task3-8.png',img)

img = arr[int(0):int(100), int(0):int(992)]   #extracting the header
cv2.imwrite('task3-9.png',img)
