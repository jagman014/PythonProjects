import re

# compiled regex objects have the same methods as base functions
# have optional start and end params
re_obj = re.compile(r'\d+')
s = 'foo123barbaz'

print(re_obj.search(s))

print(s[6:9])

print(re_obj.search(s, 6, 9))

# anchors still refer to the start of a string
re_obj = re.compile(r'^bar')
s = 'foobarbaz'

print(s[3:])

print(re_obj.search(s, 3))

# split, sub, and subn methods don't support start and end params
