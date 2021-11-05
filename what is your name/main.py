firstName = input()
lastName = input()


def printFullName(firstName, lastName):
    print(f"Hello {firstName} {lastName}! You just delved into python.")


if len(firstName) <= 10 and len(lastName) <= 10:
    printFullName(firstName, lastName)
