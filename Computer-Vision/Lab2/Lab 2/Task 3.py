import numpy as np
import cv2
import imutils

# load the puzzle and waldo images
puzzle = cv2.imread("waldo1.jpg")
waldo = cv2.imread("twaldo.png")
(waldoHeight, waldoWidth) = waldo.shape[:2]

result = cv2.matchTemplate(puzzle, waldo, cv2.TM_CCOEFF)
(_, _, minLoc, maxLoc) = cv2.minMaxLoc(result)
# the puzzle image
topLeft = maxLoc
botRight = (topLeft[0] + waldoWidth, topLeft[1] + waldoHeight)
roi = puzzle[topLeft[1]:botRight[1], topLeft[0]:botRight[0]]

# construct a darkened transparent 'layer' to darken everything
# in the puzzle except for waldo
mask = np.zeros(puzzle.shape, dtype="uint8")
puzzle = cv2.addWeighted(puzzle, 0.25, mask, 0.75, 0)

# put the original waldo back in the image so that he is
# 'brighter' than the rest of the image
puzzle[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] = roi
#draw a blue rectangle for more highlight
cv2.rectangle(puzzle, topLeft, botRight, 255, 5)
# display the images
cv2.imwrite('Task3.png',puzzle)
cv2.imshow("Puzzle", imutils.resize(puzzle, height=650))
cv2.imshow("Waldo", waldo)
cv2.waitKey(0)