#!/usr/bin/env python3

_fruits = ['apples', 'pears', 'strawberries']
_text = 'Hello I like python'

print(_text[2:(len(_text) / 2):2]) # Slice-Operator: [start:stop:step]

# Insert with Slice
_fruits[2:2] = 'blueberries'
print(_fruits)
