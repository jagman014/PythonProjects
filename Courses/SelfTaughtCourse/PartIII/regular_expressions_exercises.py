import os
import re

# Exercise 1
directory = os.path.dirname(__file__)
filename = os.path.join(directory, 'zen.txt')

with open(filename, 'r', encoding='utf-8') as fin:
    zen = fin.read()

print(re.findall('Dutch', zen, re.MULTILINE))

# Exercise 2
string = 'Arizona 479, 501, 870. California 209, 213, 650.'

print(re.findall('\d', string))

# Exercise 3
string_2 = 'The ghost that says boo haunts the loo.'

print(re.findall('.oo', string_2, re.IGNORECASE))
