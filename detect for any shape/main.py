import cv2 as cv
import numpy as np

black = (0, 0, 0)
purble = (255, 0, 179)

# read the image
img = cv.imread('shapes.png')

# convert to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# threshold of gray image
_, threshold = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

# find contour
contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

flag = 0

for contour in contours:
    if flag == 0:
        flag = 1
        continue

      # initializ the shape name and approximate the contour
    perimeter = cv.arcLength(contour, True)
    approximate = cv.approxPolyDP(contour, 0.01 * perimeter, True)

    # using drawContours() function
    cv.drawContours(img, [contour], 0, purble, 2)

    # finding center point of shape
    M = cv.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])

    # putting shape name at center of each shape
    if len(approximate) == 3:
        cv.putText(img, 'Triangle', (x, y),
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, black, 2)
    elif len(approximate) == 4:
        cv.putText(img, 'Quadrilateral', (x, y),
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, black, 2)
    elif len(approximate) == 5:
        cv.putText(img, 'Pentagon', (x, y),
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, black, 2)
    elif len(approximate) == 6:
        cv.putText(img, 'Hexagon', (x, y),
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, black, 2)
    else:
        cv.putText(img, 'circle', (x, y),
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, black, 2)


cv.imshow('shapes', img)
cv.imshow('gray', gray)
cv.imshow('thresh', threshold)


cv.waitKey(0)  # waits for keypress
cv.destroyAllWindows()  # destroy all the windowsm when keypress
