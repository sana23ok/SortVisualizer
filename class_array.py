from random import randint
import re


# class Validation:


class Array:
    def __init__(self, size: int, a: int, b: int):
        self.__size = size
        self.__a = a
        self.__b = b

    def generateArr(self):
        arr = set()
        i = 0
        while i != self.__size:
            temp = randint(self.__a, self.__b)
            if temp not in arr:
                arr.add(temp)
                i += 1

        arr = list(arr)
        return arr
