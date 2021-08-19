import re

# re.search, scans string for a match
print(re.search(r'(\d+)', 'foo123bar'))
print(re.search(r'[a-z]+', '123FOO456', re.IGNORECASE))
print(re.search(r'\d+', 'foo.bar'))

# re.match, only looks for a match at the start of the string
# not affected by re.MULTILINE flag
print(re.match(r'\d+', '123foobar'))
print(re.match(r'\d+', 'foo123bar'))

# re.fullmatch, looks for a match over the entire string
print(re.fullmatch(r'\d+', '123foo'))
print(re.fullmatch(r'\d+', 'bar123foo'))
print(re.fullmatch(r'\d+', '123'))

# re.findall, returns a list of all matches / matching groups
print(re.findall(r'\w+', '...foo,,,,bar:%$baz//|'))
print(re.findall(r'#(\w+)#', '#foo#.#bar#.#baz#'))
print(re.findall(r'(\w+),(\w+)', 'foo,bar,baz,qux,quux,corge'))
print(re.findall(r'(\w+),(\w+),(\w+)', 'foo,bar,baz,qux,quux,corge'))

# re.finditer, returns an iterable for non-overlapping matches
it = re.finditer(r'\w+', '...foo,,,,bar:%$baz//|')

print(next(it))
print(next(it))
print(next(it))

for i in re.finditer(r'\w+', '...foo,,,,bar:%$baz//|'):
    print(i)
