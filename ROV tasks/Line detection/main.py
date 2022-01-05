import ColourDetector as cd
import cv2 as cv
import numpy as np

'''
img = cv.imread('1.jpg')

lowerRed = np.array([0, 0, 0])
upperRed = np.array([50, 255, 255])
_, mask = cd.DetectColour(img, lowerRed, lowerRed, 50)
edges = cv.Canny(mask, 75, 150)
lines = cv.HoughLinesP(edges, 1, np.pi/180, 50)

img = cd.DetectColour.show(False)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)


cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()'''


cap = cv.VideoCapture('road_car_view.mp4')
while True:
    
    _,frame = cap.read() 
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lowerRed = np.array([18, 94, 140])
    upperRed = np.array([48, 255, 255])
    mask= cv.inRange(hsv, lowerRed, upperRed)
    edges = cv.Canny(mask, 75, 150)
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, maxLineGap=50)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)


    cv.imshow('frame', frame)
    cv.imshow('edges', edges)
    if cv.waitKey(25) == 27:
        break

cv.destroyAllWindows()

'''

lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, maxLineGap = 50)



for line in lines: 
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
    

cv.imshow('edges', edges)
cv.imshow('detected', img)
'''
