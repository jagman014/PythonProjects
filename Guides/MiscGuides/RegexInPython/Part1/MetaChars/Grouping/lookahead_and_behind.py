import re

# (?=<lookahead regex>) what follows parsers current position must match
# parser doesn't advance its current position after this check

# what follows foo must be lowercase letters
print(re.search('foo(?=[a-z])', 'foobar'))
print(re.search('foo(?=[a-z])', 'foo123'))

# matches foo followed by a lowercase letter
print(re.search('foo([a-z])', 'foobar'))

# doesn't capture following character
m = re.search('foo(?=[a-z])(?P<ch>.)', 'foobar')
print(m.group('ch'))

# does capture following character
m = re.search('foo([a-z])(?P<ch>.)', 'foobar')
print(m.group('ch'))

# (?!<lookahead regex>) negative lookahead
print(re.search('foo(?![a-z])', 'foobar'))
print(re.search('foo(?![a-z])', 'foo123'))

# (?<=<lookbehind regex>) what preceeds current parser position must match
# parser doesn't retreat current position
# requires a regex of fixed width -> cannot be of variable width

# what preceeds bar must be foo
print(re.search('(?<=foo)bar', 'foobar'))

# must be proceeded by qux
print(re.search('(?<=qux)bar', 'foobar'))

# (?<!<lookbehind regex>) negative lookbehind
print(re.search('(?<!foo)bar', 'foobar'))
print(re.search('(?<!qux)bar', 'foobar'))
