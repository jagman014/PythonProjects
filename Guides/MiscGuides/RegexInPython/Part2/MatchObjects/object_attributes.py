import re

# pos and endpos given positions used to create object
# if not included in create return start and end of string
re_obj = re.compile(r'\d+')
m = re_obj.search('foo123bar', 2, 7)

print((m, m.pos, m.endpos))

m = re.search(r'\d+', 'foo123bar')
print((m, m.pos, m.endpos))

# lastindex returns the index of the last captured group
# for potentially non-matching, only returns matched group
m = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')

print(m.lastindex, m[m.lastindex])

m = re.search(r'(\w+),(\w+),(\w+)?', 'foo,bar,baz')

print(m.groups())
print(m.lastindex, m[m.lastindex])

# lastgroup returns the name of the lastgroup captured
# returns none if the last group captured is not named
s = 'foo123bar456baz'
m = re.search(r'(?P<n1>\d+)\D*(?P<n2>\d+)', s)

print(m.lastgroup)

m = re.search(r'(\d+)\D*(\d+)', s)

print(m.groups(), m.lastgroup)

# re is the compiled regex object
# allows for use of compiled object attributes and methods on match objects
regex = r'(\w+),(\w+),(\w+)'

m1 = re.search(regex, 'foo,bar,baz')

print(m1, m1.re)

re_obj = re.compile(regex)

print(re_obj)

print(re_obj is m1.re)

m2 = re_obj.search('qux,quux,corge')

print(m2, m2.re)

print(m2.re is re_obj is m1.re)

print(m1.re.match('qux,quux,corge'))

# string returns the search string
m = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')

print(m)
print(m.string)
