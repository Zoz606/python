import cv2 as cv


class shapeDetector:
    def __init__(self):
        pass

    def detect(self, contour):
        # initializ the shape name and approximate the contour
        shape = ''
        perimeter = cv.arcLength(contour, True)
        approximate = cv.approxPolyDP(contour, 0.04 * perimeter, True)

        # Triangle
        if len(approximate) == 3:
            shape = 'Triangle'

        #Rectangle and square
        elif len(approximate) == 4:
            # compute the bounding box of the contour and use the
            # bounding box to compute the aspect ratio
            (x, y, w, h) = cv.boundingRect(approximate)
            aspictRatio = w/h
            float(aspictRatio)

            # Square    
            if aspictRatio >= 0.95 or aspictRatio <= 1.05:
                shape = 'Square'

            # Rectangle
            else:
                shape = 'Rectangle'

        # Pentagon
        elif len(approximate) == 5:
            shape = 'Pentagon'

        # circle
        else:
            shape = 'circle'

        return shape
