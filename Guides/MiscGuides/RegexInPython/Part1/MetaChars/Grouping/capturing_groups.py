import re

# re match objects can be used to return the matching groups
m = re.search('(\w+),(\w+),(\w+)', 'foo,qux,baz')
print(m)

# return tuple of captured groups
print(m.groups())

# print specific group, 1 indexed, group(0) -> group() -> groups()
for i in range(0, 4):
    print(i, m.group(i))

# can specify multiple indicies
print(m.group(2, 1))

# (?:<regex>) non-capturing groups
n = re.search('(\w+),(?:\w+),(\w+)', 'foo,qux,baz')
print(n.groups())
