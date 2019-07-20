import cv2 as cv
img = cv.imread('lena.png')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift = cv.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
#it will draw a circle with size of keypoint and it will even show its orientation
img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('dst',img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
sift = cv.xfeatures2d.SIFT_create()

#Here kp will be a list of keypoints and des is a numpy array of shape Number_of_Keypoints×128.
# Here kp will be a list of keypoints and des is a numpy array of shape Number_of_Keypoints×128.
kp, des = sift.detectAndCompute(gray,None)
print("Descriptors representation:",des)
for a in kp:
    print (a)