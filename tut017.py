#!/usr/bin/env python3

def func(x, txt='2'):
	print(x)

	if txt == '1':
		print('txt is 1')
	else:
		print('txt is not 1')


func(25) # Optional Parameter: func(25, '1'), returns 25 and txt is not 1
