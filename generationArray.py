from random import randint
import re


def isPositiveInt(s):
    pattern = r'^\d+$'
    return re.match(pattern, s) is not None


def checkInterval(a, b, size):
    return (b-a) > size and b > a


def validateInterval(size):
    global a, b
    valid = False
    while not valid:
        a = input("Enter a:")
        validA = isPositiveInt(a)
        b = input("Enter b:")
        validB = isPositiveInt(b)
        if validA and validB:
            a = int(a)
            b = int(b)
            valid = checkInterval(a, b, size)
            #print(valid)
            if not valid:
                #valid = False
                print("An interval must be bigger or equal to size of array!!!")
        else:
            valid = False
            print("Invalid input, enter positive integers without any characters!!!")
    return a, b


size = 300
a, b = validateInterval(size)
arr = []
i = 0
while i != size:
    temp = randint(a, b)
    if temp not in arr:
        arr.append(temp)
        i += 1

print(arr)
