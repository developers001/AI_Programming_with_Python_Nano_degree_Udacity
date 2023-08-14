# Number 1
def functionNumberOne(listOfNumber: list):
    sum = 0
    max = 0
    min = 0
    for i in listOfNumber:
        sum += i
        if i > max:
            max = i
        if i < min:
            min = i
    mean = sum/len(listOfNumber)
    print("Sum: {}".format(sum))
    print("Max: {}".format(max))
    print("Min: {}".format(min))
    print("Mean: {}".format(mean))
# call functionNumberOne, uncomment code below
# functionNumberOne([1,2,3,4,5])

# Number 2
def functionNumberTwo(firstList: list, secondList: list):
    for i in firstList:
        if i in secondList:
            return True
    return False
# call functionNumberTwo, uncomment code below
# print(functionNumberTwo(["Tom", "Bob", "Sue", "Rachel"], ["Bob", "Susan", "Roger", "Mike"]))

# Number 3
def functionNumberThree(dicOne: dict, dicTwo: dict):
    newDic = dict()
    for key in dicOne:
        if key in dicTwo:
            newDic[key] = dicOne[key] + dicTwo[key]
        else:
            newDic[key] = dicOne[key]

    for key in dicTwo:
        if key not in newDic:
            newDic[key] = dicTwo[key]
    
    print(newDic)
# call functionNumberThree, uncomment code below
# functionNumberThree({'a': 100, 'b': 200, 'c':300}, {'a': 300, 'b': 200, 'd':400})

# Number 4
def functionNumberFor():
    for i in range(0, 100):
        print(i)
        if i > 0:
            if (i % 3 == 0) and (i % 5 == 0):
                print("FizzBuzz")
            elif i % 5 == 0:
                print("Fizz")
            elif i % 3 == 0:
                print("Buzz")
# call functionNumberFor, uncomment code below
# functionNumberFor()

# Number 5
def functionNumberFive(password: str):
    valid = True
    listOfChar = ['$', '#', '@']
    passwordLength = len(password)
    if 6<passwordLength<16:
        if not any(i.isdigit() for i in password):
            valid = False
        if not any(i.isupper() for i in password):
            valid = False
        if not any(i.islower() for i in password):
            valid = False
        if not any(i in listOfChar for i in password):
            valid = False
    if valid:
        print("Password is valid")
    else:
        print("Password is not valid")
# call functionNumberFive, uncomment code below
# functionNumberFive("Password1#")

# Number 6
def functionNumberSix(sampleList: list):
    uniqueList = set()
    for i in sampleList:
        uniqueList.add(i)
    print(uniqueList)
# call functionNumberSix, uncomment code below
# functionNumberSix([1,2,2,3,3,3,4,4,5])

# Number 7
import math
def functionNumberSeven(height, base):
    print("Hypetonuse: {}". format(math.sqrt((pow(height,2))+(pow(base, 2)))))
# call functionNumberSeven, uncomment code below
# functionNumberSeven(4,3)

# Number 8
def functionNumberEight(words: str):
    value = 0
    one = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
    two = ['D', 'G']
    three = ['B', 'C', 'M', 'P']
    four = ['F','H','V','W','Y']
    five = ['K']
    eight = ['J', 'X']
    ten = ['Q', 'Z']
    for i in words:
        if i.upper() in one:
            value += 1
        if i.upper() in two:
            value += 2
        if i.upper() in three:
            value += 3
        if i.upper() in four:
            value += 4
        if i.upper() in five:
            value += 5
        if i.upper() in eight:
            value += 8
        if i.upper() in ten:
            value += 10
    print("Value: {}".format(value))
# call functionNumberEight, uncomment code below
# functionNumberEight("Cabbage")

# Number 9
def functionNumberNine(firstNumber, secondNumber):
    if secondNumber == 0:
        return firstNumber
    else:
        return functionNumberNine(secondNumber, firstNumber % secondNumber)
# call functionNumberNine, uncomment code below
# print(functionNumberNine(12,2))
