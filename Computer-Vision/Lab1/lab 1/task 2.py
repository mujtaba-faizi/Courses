import cv2

# reads image as RGB
img = cv2.imread('4.PNG')

# shows the image
cv2.imshow('image', img)
cv2.waitKey(0)

#Convert to grayscale color space
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Shows the image
cv2.imshow('grayscale', img1)
cv2.waitKey(0)

# Convert to YCrCb color space
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# Shows the image
cv2.imshow('YCrCb', img2)
cv2.waitKey(0)

# Converts to HSV color space
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Shows the image
cv2.imshow('HSV', img3)
cv2.waitKey(0)

# Converts to LAB color space
img4 = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# Shows the image
cv2.imshow('LAB', img4)
cv2.waitKey(0)