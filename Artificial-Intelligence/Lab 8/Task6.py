
import cv2
img1 = cv2.imread('F:\Pics & Videos\NUST Events 2017\CS-5A\_DSC6837(1).jpg')
img2=cv2.imread('F:\Pics & Videos\NUST Events 2017\CS-5A\_DSC6837.jpg')
detector = cv2.FeatureDetector_create("SIFT")
descriptor = cv2.DescriptorExtractor_create("SIFT")

skp = detector.detect(img1)
skp, sd = descriptor.compute(img1, skp)

tkp = detector.detect(img2)
tkp, td = descriptor.compute(img2, tkp)
flann_params = dict(algorithm=1, trees=4)
flann = cv2.flann_Index(sd, flann_params)
idx, dist = flann.knnSearch(td, 1, params={})
del flann