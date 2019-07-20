from PIL import Image
import numpy as np

img = Image.open("Mujtaba.png")
img = img.convert('L') # convert image to greyscale
arr=np.asarray(img)
height = len(arr)  # width & height of the image i.e. no. of pixels
width = len(arr[0])
pix = np.zeros((height, width), dtype=np.uint8)     # new array of zeros

for x in range(0, height):
    for y in range(0, width):
        if y==width-1:   # when reaching the last pixel column
            pix[x][y]=arr[x,y]
            continue
        else:
            pix[x, y] = abs(arr[x,y] - arr[x, y+1])  # subtracting pixel intensity with right neighbour pixel intensity
im = Image.fromarray(pix)    # converting array to image
im.show()