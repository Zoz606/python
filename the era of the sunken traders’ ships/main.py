from cv2 import imread
import functions as f
import cv2 as cv
import numpy as np

# read Image
img = cv.imread('shapes.png')

#detection
img = f.detect(img)

# Show
cv.imshow('img', img)


cv.waitKey(0)
cv.destroyAllWindows()
