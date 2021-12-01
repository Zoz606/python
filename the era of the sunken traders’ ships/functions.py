import cv2 as cv
import numpy as np


def detect(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # threshold
    _, thresh = cv.threshold(gray, 240, 255, cv.THRESH_BINARY)

    # find contour
    cnt, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in cnt:
        permiter = cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, 0.01 * permiter, True)

        # draw contour
        cv.drawContours(img, [approx], -1, (0, 255, 0), 3)

        # Coardinates of the begining of the text
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        # Shape detection
        # Triangle
        if len(approx) == 3:
            cv.putText(img, "3rd Centry BC", (x, y),
                       cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

        elif len(approx) == 4:
            x, y, w, h = cv.boundingRect(approx)
            aspectRatio = float(w)/h
            # square
            if aspectRatio >= 0.95 and aspectRatio < 1.05:
                cv.putText(img, "4th Centry BC", (x, y),
                           cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            # rectangle
            else:
                cv.putText(img, "6th Centy BC", (x, y),
                           cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        # Star
        elif len(approx) == 10:
            cv.putText(img, "5th Centy BC", (x, y),
                       cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        # Circle
        else:
            cv.putText(img, "2nd Centry BC", (x, y),
                       cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    return img
