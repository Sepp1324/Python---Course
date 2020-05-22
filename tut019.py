#!/usr/bin/env python3

# Global Variables
var = 9
loop = True
new_var = 3


def func(x):
	new_var = 7 # Local Variable
	print(loop)

	if x == 5:
		return new_var

def otherFunc():
	print(var)
	new_var = 5
	print(new_var)


print(new_var)
otherFunc()
print(func(5))
