import cv2 as cv
from cv2 import imshow
import numpy as np


# import image
img = cv.imread('supe.png')

# hsv and gray
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgHsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# low and upper
low = np.array([4, 50, 50])
upper = np.array([4, 255, 255])
mask = cv.inRange(imgHsv, low, upper)
mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, np.ones((20, 20), np.uint8))

# find contour
cnt, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cnt = sorted(cnt, key=cv.contourArea, reverse=True)

img = cv.drawContours(img, cnt, -1, (0, 255, 0), 2)



# Show results
cv.imshow('mask', mask)
cv.imshow('res', img)
# cv.imshow('res', thresh)

 
cv.waitKey()
cv.destroyAllWindows()
