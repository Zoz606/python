from asyncio.log import logger
import imp
from helper import validateAndExecute, userInputMessage
import logging

userInput = ''
while userInput != "exit":
    userInput = input(userInputMessage)
    daysAndUnits = userInput.split(":")
    daysAndUnitsDictionary = {
        'days': daysAndUnits[0],
        'unit': daysAndUnits[1]
    }
    validateAndExecute(daysAndUnitsDictionary)
