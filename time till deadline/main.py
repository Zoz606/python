from datetime import datetime

userInput = input('Enter your goal with a deadline seperated by colon : ')
inputList = userInput.split(':')

goal = inputList[0]
deadline = inputList[1]

deadlineDate = datetime.strptime(deadline, "%d.%m.%Y")
todayDate = datetime.today()

# how many days from now till the deadline

deadlineEnd = deadlineDate - todayDate
deadlineEndInHours = int(deadlineEnd.total_seconds() / 60 / 60)

print(f"Time remaining for your goal : {goal} is {deadlineEndInHours} hours")
