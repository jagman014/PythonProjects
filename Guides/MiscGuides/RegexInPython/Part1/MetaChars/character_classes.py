import re
from types import resolve_bases

s = 'foo123bar'

# "[]" make up a character class, matches anything in the char class
# search for three consecutive digits
print(re.search('[0-9][0-9][0-9]', s))
print(re.search('[0-9][0-9][0-9]', 'foo456bar'))
print(re.search('[0-9][0-9][0-9]', '234baz'))
print(re.search('[0-9][0-9][0-9]', 'qux678'))

# non-group of threes wont match
print(re.search('[0-9][0-9][0-9]', '12foo34'))

# "." matches any char except newline
print(re.search('1.3', s))
print(re.search('1.3', 'foo13bar'))

# char classes match anything within the "[]"
print(re.search('ba[artz]', 'foobarqux'))
print(re.search('ba[artz]', 'foobazqux'))

# classes can also contain a range using "-"
print(re.search('[a-z]', 'FOObar'))

# match any hexadecimal char
print(re.search('[0-9a-fA-F]', '--- a0 ---'))

# match not in class using "^"
print(re.search('[^0-9]', '12345foo'))

# can remove these special effects with escaping or positioning
print(re.search('[#:^]', 'foo^bar:baz#qux'))
print(re.search('[ab\-c]', '123-456'))

# other special chars lose meaning in char classes
