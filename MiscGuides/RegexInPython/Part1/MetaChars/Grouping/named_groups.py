import re

# (?P<name><regex>) creates a named group
m = re.search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,quux,baz')
print(m.groups())

# can refer to groups via names or numbers
print(m.group('w1'))
print(m.group('w1'))
print(m.group('w3', 'w2'))

# (?P=<name>) refers to a previous named group acts like a backreference
m = re.search(r'(?P<word>\w+),(?P=word)', 'foo,foo')
print(m)
print(m.group('word'))
