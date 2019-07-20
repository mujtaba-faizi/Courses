import numpy as np
import cv2

def apply_filter(img,filter):
    filter_sum=0
    for x in range(0, filter.shape[0]):
        for y in range(0, filter.shape[1]):
            filter_sum = filter_sum + filter[x, y]
    arr=np.asarray(img)

    filter_row=filter.shape[0]
    filter_col=filter.shape[1]
    padding_size=filter_col/2                  #do zero padding acc. to the filer size to avoid out of bound errors
    arr=np.pad(arr, int(padding_size), mode='constant')  #applying zero padding
    rows = arr.shape[0]  # width & height of the image i.e. no. of pixels
    cols = arr.shape[1]
    c = 0
    d=0
    g=filter.shape[1]
    for a in range(0,(rows*cols)):
        if filter_col>cols:   #for last column pixel, move the window to the next row
             d+=1
             filter_row+=1
             c=0
             filter_col=g
        if filter_row>rows:   #after last row limit of window, exit
             break
        b=arr[int(d):int(filter_row), int(c):int(filter_col)]
        arr[int(d+padding_size),int(c+padding_size)]=np.median(b)   #replacing with the median pixel value
        c+=1    #for moving the window ahead one pixel at a time (same for rows also)
        filter_col+=1
    img = np.array(arr * 255, dtype=np.uint8)   #converting array to image
    return arr

img = cv2.imread('saltandpaper.tif',0)
a = np.array([[1,1,1], [1,1,1], [1,1,1]])
img=apply_filter(img,a)
cv2.imwrite('median_filter_applied.jpg', img)