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
        sum=np.sum(filter*b)
        avg=sum/filter_sum
        arr[int(d+padding_size),int(c+padding_size)]=avg   #replacing with the avg pixel value
        c+=1    #for moving the window ahead one pixel at a time (same for rows also)
        filter_col+=1
    return arr

a = np.array([[1,1,2,2,2,1,1], [1,2,2,4,2,2,1], [2,2,4,8,4,2,2], [2,4,8,16,8,4,2],[2,2,4,8,4,2,2],[1,2,2,4,2,2,1],[1,1,2,2,2,1,1]])
img = cv2.imread('unsharpmasking.tif',0)
arr1=np.asarray(img)
filter_col = a.shape[1]
padding_size = filter_col / 2  # do zero padding acc. to the filer size to keep the sizes equal with the filtered image
arr1 = np.pad(arr1, int(padding_size), mode='constant')  # applying zero padding

arr2=apply_filter(img,a)


cv2.imwrite('unsharp_masking_applied.jpg', np.add(np.absolute(np.subtract(arr1,arr2)),arr1))   #highpass = (original - lowpass) + original


