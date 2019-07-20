#name: ABDUL BASIT
#SECTION: BSCS5A
# REG NO: 146120


import numpy as np
import PIL
from PIL import Image

def cal_gradiant(im):
    numrows=im.shape[0]
    numcols=im.shape[1]
    new_img=np.zeros((numrows+2,numcols+2),dtype=np.uint8)
    for i in range(numrows):
        for j in range(numcols):
            if(i+1<(numrows-2)):
                   new_img[i][j]=abs(im[i+1][j]-im[i][j])
    gradd=Image.fromarray(new_img)
    gradd.show()
    gradd.save("gradd.jpg")
    return 0

img = Image.open('lena_color.jpg').convert('L')
im=np.asarray(img)
print(im)
cal_gradiant(im)
