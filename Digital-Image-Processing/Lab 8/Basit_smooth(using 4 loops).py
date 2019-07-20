import numpy as np
from PIL import Image, ImageOps, ImageStat


img=Image.open('smoothing.tif')

img=img.convert('L')
img.show()
kernel=(np.ones((7,7),np.float32)/49)


di=kernel.shape[0]-3


imgp=ImageOps.expand(img, border=di, fill=0)


imarr = np.array(imgp)

#print(imarr)

for i in range(1,img.size[0]):
    for j in range(1,img.size[1]):
        added=0.0
        for a in range(kernel.shape[0]):
            for b in range(kernel.shape[1]):
                added=added+(kernel[a][b]*imarr[i-di+a][j-di+b])
        #print(added)
        imarr[i][j]=added
        
#print(imarr)
h=Image.fromarray(imarr)
h.save('mon.jpg')
