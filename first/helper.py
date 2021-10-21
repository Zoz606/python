

def daysToUnits(days, conversionUnit):
    if conversionUnit == 'hours':
        return f"{days} days are {days * 24} hours"
    elif conversionUnit == 'minutes':
        return f"{days} days are {days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validateAndExecute(daysAndUnitsDictionary):
    try:

        userInputNum = int(daysAndUnitsDictionary['days'])

        # We want to do conversion only for positive intigers
        if userInputNum > 0:
            calculatedValue = daysToUnits(
                userInputNum, daysAndUnitsDictionary['unit'])
            print(calculatedValue)
        elif userInputNum == 0:
            print("You entered a 0")
        else:
            print('You enterded a negative number')
    except:
        print("your input is not a valid number ")


userInputMessage = "enter a number of days and conversion unit : "
