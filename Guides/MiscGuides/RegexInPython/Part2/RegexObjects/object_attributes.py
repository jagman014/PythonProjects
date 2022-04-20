import re

# flags returns any flags that are in effect
re_obj = re.compile(r'(?m)(\w+),(\w+)', re.I)

print(re_obj.flags)

print(re.I|re.M|re.UNICODE, int(re.I|re.M|re.UNICODE))

# groups returns the number of groups
print(re_obj.groups)

# pattern returns the regex string of the object
print(re_obj.pattern)

# groupindex returns a dict of each named groups indicies
re_obj = re.compile(r'(?P<w1>),(?P<w2>)')

print(re_obj.groupindex)
print(re_obj.groupindex['w1'])
print(re_obj.groupindex['w2'])
