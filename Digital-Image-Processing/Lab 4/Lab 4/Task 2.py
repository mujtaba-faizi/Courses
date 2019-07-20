from PIL import Image
import numpy as np

def binarize_image(path,threshold):
    """Binarize an image."""
    img = Image.open(path)
    img = img.convert('L')  # convert image to greyscale
    img = img.point(lambda i: 0 if i < threshold else 255)  # if pixel intensity is less than threshold, change it to else 255
    return img

grayscale=binarize_image("Lab4-image.png",145)
arr = np.asarray(grayscale)

count=0
a=np.pad(arr, ((1,1),(1,1)), 'constant')   #zero padding to avoid out of bound error when checking for neighbours
rows = a.shape[0]    #width & height of the image i.e. no. of pixels
cols = a.shape[1]

for x in range(0, rows):
    for y in range(0, cols):
        if (a[x,y]==0):
            continue
        else:
            conn_labels = []
            if (a[x - 1, y]!=255) and (a[x - 1, y]!=0):    #neglecting the neighbours who dont have any labels (yet)
                conn_labels.append(a[x - 1, y])
            if (a[x + 1, y]!=255) and (a[x + 1, y]!=0):
                conn_labels.append(a[x + 1, y])
            if (a[x , y-1]!=255) and (a[x , y-1]!=0):
                conn_labels.append(a[x, y - 1])
            if (a[x , y+1]!=255) and (a[x , y+1]!=0):
                conn_labels.append(a[x, y + 1])

            if len(conn_labels)==0:
                    count=count+1    #incrementing label when no neighbour labels found
                    a[x,y]=count     #assigning the label
            else:
                min_label = min(conn_labels)     #assigning the minimum label
                a[x, y] = min_label

im=Image.fromarray(a)      #convert array to image
im.show()



