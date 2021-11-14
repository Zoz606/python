import cv2
import numpy as np


def nothing():
    pass


cv2.namedWindow('trackbar')

cv2.createTrackbar('lowHue', 'trackbar', 0, 255, nothing)
cv2.createTrackbar('lowSat', 'trackbar', 0, 255, nothing)
cv2.createTrackbar('lowBri', 'trackbar', 0, 255, nothing)
cv2.createTrackbar('upperHue', 'trackbar', 0, 255, nothing)
cv2.createTrackbar('upperSat', 'trackbar', 0, 255, nothing)
cv2.createTrackbar('upperBri', 'trackbar', 0, 255, nothing)

#cap = cv2.VideoCapture(2)
img = cv2.imread('PLSkillsBall.png')

#_, image = cap.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


while True:
    low = np.array([
        cv2.getTrackbarPos('lowHue', 'trackbar'),
        cv2.getTrackbarPos('lowSat', 'trackbar'),
        cv2.getTrackbarPos('lowBri', 'trackbar')
    ])
    upper = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, low, upper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))

    cnt, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cnt = cv2.sort(cnt, key=cv2.contourArea, reverse=True)

    img2 = cv2.drawContours(img, cnt, -1, (0, 255, 0), 2)

    cv2.imshow('ball', img)
    cv2.imshow('img2', img2)
    cv2.imshow('result', mask)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
