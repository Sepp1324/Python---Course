#!/usr/bin/env python3

_fruits = ['apple', 'pear', 'strawberry'] # List
_position = (2, 3) # Tuple
_color = (255, 255, 255)

print(type(_fruits))
print(type(_position))
print(type(_color))

print('\n')

print(_fruits)

_fruits.append('pineapple')
print(_fruits)

print(_fruits[3])

print(_fruits.pop())
print(_fruits)

_fruits[0] = 'blueberry'
print(_fruits)

