#!/usr/bin/env python3

# strip() -> Removes Spacings at the beginning and the end of a string
# len()   -> Returns the length of a String (w/0 \n)
# lower() -> Returns the string with all lowercase-letters
# upper() -> Returns the string with all uppercase-letters
# split() -> Split a string into a list where each word is a list item

_text = input('Input something: ')
print('Strip:',_text.strip())
print('Length:', len(_text))
print('Lower:', _text.lower())
print('Upper:', _text.upper())
print('Split:', _text.split()) # Default-Deliminator: Spacing; Other Indicator e.g: _text.split('.')
