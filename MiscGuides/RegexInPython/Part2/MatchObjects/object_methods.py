import re

# match objects have multiple methods

# group, returns the captured text by the capturing group
# one-based indexing, calling non-existant groups will result in an IndexError
# a non-participating group will return None
m = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')

print(m.group(1))
print(m.group(3))

# multiple values return a tuple
print(m.group(1, 3))
print(m.group(3, 3, 1, 1, 2, 2))

# can use name references
m = re.match(r'(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'quux,corge,grault')

print(m.group('w1'))
print(m.group('w3'))

print(m.group('w3', 'w1', 'w1', 'w2'))

# group() or group(0) will return the entire match
print(m.group())

# group == __getitem__ == [] for match objects
print(m.group('w1'), m.__getitem__('w1'), m['w1'])

# groups returns all groups
# can overwrite the default value for non-participating groups
m = re.search(r'(\w+),(\w+),(\w+)?', 'foo,bar,')
print(m)

print(m.groups())

print(m.groups(default='---'))

# groupdict returns the dict of captured named groups
# same default overwrite for non-participating groups
m = re.match(r'foo,(?P<w1>\w+),(?P<w2>\w+)?,qux', 'foo,bar,,qux')

print(m.groupdict())
print(m.groupdict()['w1'])
print(m.groupdict(default='---'))

# expand returns the result from a backreferencing string
m = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')

print(m.groups())

print(m.expand(r'\2'))
print(m.expand(r'[\3] -> [\1]'))

m = re.search(r'(?P<num>\d+)', 'foo123qux')

print(m.groups())

print(m.expand(r'--- \g<num> ---'))

# start and end will return the span of the matching groups
# matching a null object will cause start and end to be equal
# non-participating groups result in -1 for both
s = 'foo123bar456baz'
m = re.search('\d+', s)

print(m.start(), m.end())
print(s[m.start():m.end()])

m = re.search(r'(\d+)\D*(?P<num>\d+)', s)

print(m.start(1), m.end(1))
print(m.start('num'), m.end('num'))

# span returns a tuple of the start and end values
print(m.span())
print(m.span(1))
print(m.span('num'))
