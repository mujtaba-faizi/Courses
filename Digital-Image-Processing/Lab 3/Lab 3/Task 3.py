from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("XY-cutss.png")
gray = img.convert('L')  # greyscale

arr = np.asarray(gray).copy()
width = (gray.size)[0]    #width & height of the image i.e. no. of pixels
height = (gray.size)[1]

#calculate sums along X
sumsAlongX = []
for row in arr:
	curVal = 0
	for val in row:
		curVal += val
	sumsAlongX.append(curVal)

#calculate sums along Y
sumsAlongY = arr[0]
for i in range(1,height):
	for j in range(0,width):
		newValue = int(sumsAlongY[j]) + int(arr[i][j])
		sumsAlongY[j] = newValue

print ("X: ",sumsAlongX)
print ("Y: ",sumsAlongY)

plt.figure(1)   #white space density graph is produced, with peaks for vertical or horizontal whitespace lines
plt.plot(sumsAlongX)
plt.show()
plt.figure(2)
plt.plot(sumsAlongY)
plt.show()


