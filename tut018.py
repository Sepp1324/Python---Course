#!/usr/bin/env python3

text = input('Username: ')

try:
	number = int(text)
	print(number)
except:
	print('Invalid Username!')
