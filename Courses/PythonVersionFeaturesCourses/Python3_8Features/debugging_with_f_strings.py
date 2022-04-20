# f strings, format string literals
import math

style = 'formatted'
print(f'This is a {style} string')

r = 3.6
print(f'A circle with radius {r}, has an area of {math.pi * r * r:.2f}')
# format specifiers: https://docs.python.org/library/string.html#format-specification-mini-language

r = 3.8
print(f'Diameter {(diam := 2 * r)} gives a circumference of {math.pi * diam:.2f}')
# can use assignment operators as well

# debugging
python = 3.8
print(f'{python=}')
# '=' tells the f-string to print the variable name and value
# can add spaces

name = 'Jag'
print(f'{name = }')

# right align
print(f'{name = :>10}')

# string methods
print(f'{name.upper()[::-1] = }')
