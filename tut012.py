#!/usr/bin/env python3


def addTwo(x):
	return x + 2

def subtractTwo(number):
	return number - 2

def addTwoAndSquare(x):
	return addTwo(x)**2

def getRectArea(a, b):
	return a * b

def printResult(res): # res -> Parameter
	print(res)


_new_number = addTwoAndSquare(12) # 12 -> Argument
printResult(_new_number)

_new_number = subtractTwo(7)
printResult(_new_number)

printResult(getRectArea(4, 5))
printResult('TechNIGGER')
