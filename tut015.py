#!/usr/bin/env python3

# .find()  -> returns the index of a certain character in the string e.g hello returns 4
# .count() -> returns the occurrence of a certain character in a string e.g hello returns 1

string = input('Input something: ')

print(string.find('o'))
print(string.count('o'))

if string.count('_') > 0:
	print('Noot good!')
else:
	print('Good!')
