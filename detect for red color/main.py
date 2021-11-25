import cv2 as cv
from cv2 import imshow
import numpy as np



# import image
img = cv.imread('supe.png')

# hsv and gray
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgHsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# low and upper
low = np.array([0, 50, 50])
upper = np.array([8, 255, 255])
mask = cv.inRange(imgHsv, low, upper)


# find contour
cnt, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
img = cv.drawContours(img, cnt, -1, (0, 255, 0), 2)

# Show results
cv.imshow('mask', mask)
cv.imshow('res', img)
# cv.imshow('res', thresh)


cv.waitKey()
cv.destroyAllWindows()
