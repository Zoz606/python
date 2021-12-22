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

img = cv.imread('ball.png', 0)

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img)

cv.waitKey()
cv.destroyAllWindows()
