#!/usr/bin/env python3

_fruits = ['apples', 'pears', 'strawberries']

# Better Version!
for fruit in _fruits:
	if fruit == 'pears':
		print(fruit)
	else:
		print('not pears')

print('-' * 30)

# Shitty Version
for x in range(len(_fruits)):
	if _fruits[x] == 'pears':
		print(_fruits[x])
	else:
		print('not pears')
