def mutate_string(string, position, character):
    listOfString = list(string)
    listOfString[position] = character
    string = ''.join(listOfString)
    return string


string = 'abracadabra'
print(mutate_string(string, 5, 'k'))
