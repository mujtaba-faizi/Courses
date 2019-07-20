import numpy as np

a = np.array([[255, 255, 0, 255, 255, 255, 0, 255], [255, 255, 0, 255, 0, 255, 0, 255], [255,255,255,255,0,0,0,255],[0,0,0,0,0,0,0,255],
     [255,255,255,255,0,255,0,255],[0,0,0,255,0,255,0,255],[255,255,255,255,0,0,0,255],[255,255,255,255,0,255,255,255]])
print a

count=0
a=np.pad(a, ((1,1),(1,1)), 'constant')   #zero padding to avoid out of bound error when checking for neighbours
rows = a.shape[0]    #width & height of the image i.e. no. of pixels
cols = a.shape[1]

print "\nAfter applying zero padding"
print a

for x in range(0, rows):
    for y in range(0, cols):
        if (a[x,y]==0):       #neglecting the black boundaries
            continue
        else:
            conn_labels = []
            if (a[x - 1, y]!=255) and (a[x - 1, y]!=0):     #neglecting the neighbours who dont have any labels (yet)
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
                min_label = min(conn_labels)    #assigning the minimum label
                a[x, y] = min_label

print "\nAfter applying algorithm"
print a




