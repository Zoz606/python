# this code detects the name of some Geometric forms

import cv2 as cv
import numpy as np

img = cv.imread("shape.png")


cv.imshow('shapes', img)


cv.waitKey(0)  # waits for keypress
cv.destroyAllWindows()  # destroy all the windowsm when keypress
