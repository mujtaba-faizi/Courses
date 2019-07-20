import cv2
img = cv2.imread('lena.png')
# Create SURF object
surf = cv2.xfeatures2d.SURF_create(5000)

# Here I decreased Hessian Threshold to 1000, which increases the no. of features found in the image.
# surf = cv2.xfeatures2d.SURF_create(1000)

# Find keypoints and descriptors directly
kp, des = surf.detectAndCompute(img,None)

img = cv2.drawKeypoints(img,kp,None,(255,0,0),4)

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

print( "Descriptor Size : ",surf.descriptorSize() )
print( "No. of features : ",len(kp) )