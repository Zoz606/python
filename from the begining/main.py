
from myClass import Human
import cv2 as cv
import numpy as np

'''num1 = input('please enter first number: ')
num2 = input('please enter second number: ')
op = input('please enter the operator: ')


if op == '+':
    print(f"sum = {int(num1) + int(num2)}")
elif op == '-':
    print(f"sub = {int(num1) - int(num2)}")
elif op == '*':
    print(f"mul = {int(num1) * int(num2)}")
elif op == '/':
    print(f"div = {int(num1) / int(num2)}")
elif op == '^':
    print(f"pow = {int(num1) ** int(num2)}")
'''
'''for i in range(10):
    if i % 2 == 0:
        print(f'{i} : even')
    else:
        print(f'{i} : odd')

print('Finish')
'''
'''
num = int(input('please Enter a number : '))

while num < 10:
    print('smaller than 10')
    num = int(input('please Enter a number : '))
'''
'''numberOfStudents = 3
subjectNumber = 4


for student in range(numberOfStudents):
    degree = 0
    print(f'Enter the data of the student number {student + 1}  ')
    for subject in range(subjectNumber):
        subjectScore = int(
            input(f'please enter the degree of the subject number {subject + 1} :'))
        degree += subjectScore

    if degree >= 0 and degree < 50:
        print('fail')
    elif degree >= 50 and degree < 65:
        print('pass')
    elif degree >= 65 and degree < 75:
        print('Good')
    elif degree >= 75 and degree < 85:
        print('Very Good')
    elif degree >= 85 and degree <= 100:
        print('Excelent')
    else:
        print('Error recognizing the degree')
'''

'''students = []
studentNum = 5
subjectNum = 3

for i in range(studentNum):
    studentData = []
    name = input('Please enter the student name : ')
    studentData.append(name)

    for subject in range(3):
        subjectDegree = float(input('Enter the degree of the subject : '))
        studentData.append(subjectDegree)

    students.append(studentData)

print(students)
'''

'''img = cv.imread('Aboutrika.png', cv.IMREAD_GRAYSCALE)

cv.imshow('Trika', img)

k = cv.waitKey(0)

if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('majico.png', img)
    cv.destroyAllWindows()
'''
'''
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
'''

'''img = np.zeros((512, 512, 3), np.uint8)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 255, 255))

cv.imshow('img', img)


cv.waitKey()
cv.destroyAllWindows()
'''

'''x = np.uint8([250])
y = np.uint8([10])

print(cv.add(x, y))

print(x + y)'''

'''img = cv.imread('Aboutrika.png')

_, thresh = cv.threshold(img, 200, 255, cv.THRESH_BINARY)

cv.imshow('thresh', thresh)


cv.waitKey(0)
cv.destroyAllWindows()
'''

'''
def read():
    username = input('Please enter user name : ')
    password = int(input('Please enter the password : '))

    return username, password


def verify(username, password, database):
    if username in database:
        p = database[username]
        if password == p:
            return 'Access Accepted'
        else:
            return 'Incorrect Password'
    else:
        return 'Error 404 Not Found'


def printMessage(message):
    print(message)


database = {
    'Hazem': 123,
    'Mohamed': 456,
    'zezo': 789
}

username, password = read()

res = verify(username, password, database)

print(res)
'''
'''
h1 = Human()
h2 = Human()


h1.readData()
h1.printData()
'''

'''
cap = cv.VideoCapture(0)
_, f = cap.read()

avg1 = np.float32(f)
avg2 = np.float32(f)

while True:
    _, f = cap.read()

    if f is not None:
        f = np.float32(f)
        grayFrame = cv.cvtColor(f, cv.COLOR_BGR2GRAY)
        cv.accumulateWeighted(f, avg1, 1)
        res1 = cv.convertScaleAbs(avg1)
        grayAvg = cv.cvtColor(avg1, cv.COLOR_BGR2GRAY)
        difference = cv.absdiff(grayFrame, grayAvg)
        

        cv.imshow('img', f)
        cv.imshow('avg1', res1)
        cv.imshow('diif', difference)

        if cv.waitKey(20) == 27:
            break

cv.destroyAllWindows()
'''

# Face detection
faceCascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeCascade = cv.CascadeClassifier('haarcascade_eye.xml')

cap = cv.VideoCapture(0)

while True:
    _, img = cap.read()
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)

    print(f'found {len(faces)} face(s) ')

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        regionGray = imgGray[y:y+h, x:x+w]
        regionColor = img[y:y+h, x:x+w]
        eyes = eyeCascade.detectMultiScale(regionGray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(regionColor, (ex, ey),
                         (ex + ew, ey + eh), (0, 255, 0), 2)

    cv.imshow('window', img)

    if cv.waitKey(20) == 27:
        break

cv.destroyAllWindows()
