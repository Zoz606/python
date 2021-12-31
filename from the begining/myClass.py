class Human:

    def __init__(self):
        self.name = None
        self.age = 0
        self.skinColor = None

    def readData(self):
        name = input('Enter your name :')
        age = int(input('Enter your age :'))
        skinColor = input('Enter your skin color :')
        self.name = name
        self.age = age
        self.skinColor = skinColor

    def printData(self):
        print(f'Human data : {self.name}, {self.age}, {self.skinColor} ')
