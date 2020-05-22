#!/usr/bin/env python3

file = open('file.txt', 'r')
f = file.readlines() # Default with '\n'

print(f) # With Backspacke

# Shitty-Method: Iterating
new_list = []

for line in f:
	if line[-1] == '\n': # -1 -> Last Character
		new_list.append(line[:-1]) # -1 -> Last Character
	else:
		new_list.append(line)

print(new_list) # w/o Backspacke

# Better Method: String-Function
new_list = []

for line in f:
	new_list.append(line.strip())

print(new_list) # w/o Backspacke
