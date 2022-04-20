import re

# follow portion of regex, say how many repitions can occur

# * matches with zero or more of the preceeding
print(re.search('foo-*bar', 'foobar'))
print(re.search('foo-*bar', 'foo-bar'))
print(re.search('foo-*bar', 'foo--bar'))

# combine with wildcard to match anything between regex strings
print(re.search('foo.*bar', '# foo $qux@grault % bar #'))

# + matches one or more of the preceeding
print(re.search('foo-+bar', 'foobar'))
print(re.search('foo-+bar', 'foo-bar'))
print(re.search('foo-+bar', 'foo--bar'))

# ? match zero or one of the preceeding
print(re.search('foo-?bar', 'foobar'))
print(re.search('foo-?bar', 'foo-bar'))
print(re.search('foo-?bar', 'foo--bar'))

# more examples of the above
print(re.match('foo[1-9]*bar', 'foobar'))
print(re.match('foo[1-9]*bar', 'foo42bar'))

print(re.match('foo[1-9]+bar', 'foobar'))
print(re.match('foo[1-9]+bar', 'foo42bar'))

print(re.match('foo[1-9]?bar', 'foobar'))
print(re.match('foo[1-9]?bar', 'foo42bar'))

# the above are all greedy -> will find the longest possible match
print(re.search('<.*>', '%<foo> <bar> <baz>%'))

# can be made lazy with another ?
print(re.search('<.*?>', '%<foo> <bar> <baz>%'))

print(re.search('<.+>', '%<foo> <bar> <baz>%'))
print(re.search('<.+?>', '%<foo> <bar> <baz>%'))

print(re.search('ba?', 'baaaa'))
print(re.search('ba??', 'baaaa'))

# {m} matches exactly m repetitions
print(re.search('x-{3}x', 'x--x'))
print(re.search('x-{3}x', 'x---x'))
print(re.search('x-{3}x', 'x----x'))

# {m,n} matches repitions from m to n inclusive
# omitting m -> {0,n}, omitting n -> {m,inf}, omitting both -> *
# omitting all -> literal match of {}
for i in range(1, 6):
        s = f"x{'-' * i}x"
        print(f'{i}  {s:10}', re.search('x-{2,4}x', s))

# can also be made lazy -> {m,n}?
print(re.search('a{3,5}', 'aaaaaaaa'))
print(re.search('a{3,5}?', 'aaaaaaaa'))
