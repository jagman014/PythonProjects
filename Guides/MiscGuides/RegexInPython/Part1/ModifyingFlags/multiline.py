import re

# re.M or re.MULTILINE, modifies ^ and $ to match at newlines
# no effect on \A or \Z

s = 'foo\nbar\nbaz'

print(re.search('^foo', s))
print(re.search('^bar', s))
print(re.search('^baz', s))

print(re.search('foo$', s))
print(re.search('bar$', s))
print(re.search('baz$', s))

print(s)

print(re.search('^foo', s, re.MULTILINE))
print(re.search('^bar', s, re.MULTILINE))
print(re.search('^baz', s, re.MULTILINE))

print(re.search('foo$', s, re.M))
print(re.search('bar$', s, re.M))
print(re.search('baz$', s, re.M))
