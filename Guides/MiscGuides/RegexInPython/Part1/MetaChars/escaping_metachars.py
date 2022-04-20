import re

# \ will escape most meta characters
print(re.search('.', 'foo.bar'))
print(re.search('\.', 'foo.bar'))

# single \ in string
s = r'foo\bar'
print(s)

# results in an re.error bad escape pattern -> single \ passed to re
# print(re.search('\\', s))

# solution of four \ to pass \\ to re, or pass raw string
print(re.search('\\\\', s))
print(re.search(r'\\', s))

# best to specify raw strings for regex in python
