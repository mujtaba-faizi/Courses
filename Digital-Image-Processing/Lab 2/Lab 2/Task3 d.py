from PIL import Image
import numpy as np

def rgb2gray(rgb):
    print (rgb)
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

im = Image.open('09f9131b9619e7d720a66f9e018b6078.jpg')
array=np.asarray(im)
b=rgb2gray(array)
im=Image.fromarray(b)
im.show()

