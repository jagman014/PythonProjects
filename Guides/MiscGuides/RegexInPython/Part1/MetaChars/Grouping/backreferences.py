import re

# \<n> matches the contents of the nth captured group (n -> [1, 99])
regex = r'(\w+),\1'

m = re.search(regex, 'foo,foo')
print(m)

print(m.group(1))

n = re.search(regex, 'qux,qux')
print(n)

print(n.group(1))

o = re.search(regex, 'foo,qux')
print(o)
