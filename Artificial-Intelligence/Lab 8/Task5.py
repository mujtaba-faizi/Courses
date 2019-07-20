
import cv2
img = cv2.imread('F:\Pics & Videos\NUST Events 2017\CS-5A\_DSC6837(1).jpg')
detector = cv2.FeatureDetector_create("SIFT")
descriptor = cv2.DescriptorExtractor_create("SIFT")

skp = detector.detect(img)
skp, sd = descriptor.compute(img, skp)
