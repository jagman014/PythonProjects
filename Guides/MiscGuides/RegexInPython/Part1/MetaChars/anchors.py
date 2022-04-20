import re

# zero width characters, dictates location of search string

# ^ and \A match the start of the string
print(re.search('^foo', 'foobar'))
print(re.search('^foo', 'barfoo'))
print(re.search('\Afoo', 'foobar'))
print(re.search('\Afoo', 'barfoo'))

# $ and \Z match the end of the string
print(re.search('bar$', 'foobar'))
print(re.search('bar$', 'barfoo'))
print(re.search('bar\Z', 'foobar'))
print(re.search('bar\Z', 'barfoo'))

# $ matches with \n but \Z doesn't
print(re.search('bar$', 'foobar\n'))
print(re.search('bar\Z', 'foobar\n'))

# \b matches to a word boundary
print(re.search(r'\bbar', 'foo bar'))
print(re.search(r'\bbar', 'foo.bar'))
print(re.search(r'\bbar', 'foobar'))
print(re.search(r'foo\b', 'foo bar'))
print(re.search(r'foo\b', 'foo.bar'))
print(re.search(r'foo\b', 'foobar'))

# can be used to search for whole word
print(re.search(r'\bbar\b', 'foo bar baz'))
print(re.search(r'\bbar\b', 'foo(bar)baz'))
print(re.search(r'\bbar\b', 'foobarbaz'))

# \B is the opposite
print(re.search(r'\Bfoo\B', 'foo'))
print(re.search(r'\Bbar\B', 'bar'))
print(re.search(r'\Bfoo\B', 'barfoobaz'))
