import cv2

img = cv2.imread('lena.png')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
#it will draw a circle with size of keypoint and it will even show its orientation
img1=cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('dst',img1)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
sift = cv2.xfeatures2d.SIFT_create(2000)   #Hessian Threshold = 2000

#Here kp will be a list of keypoints and des is a numpy array of shape Number_of_Keypoints×128.
# Here kp will be a list of keypoints and des is a numpy array of shape Number_of_Keypoints×128.
kp, des = sift.detectAndCompute(gray,None)
print( "Descriptor Size (SIFT) : ",sift.descriptorSize() )
print( "No. of features (SIFT): ",len(kp) )

# Create SURF object
surf = cv2.xfeatures2d.SURF_create(2000)  #Hessian Threshold = 2000

# Find keypoints and descriptors directly
kp, des = surf.detectAndCompute(gray,None)

img2 = cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('dst',img2)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

print( "Descriptor Size (SURF): ",surf.descriptorSize() )
print( "No. of features (SURF): ",len(kp) )