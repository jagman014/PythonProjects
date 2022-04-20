import re

# re.split, uses regex match as delimiter to split string by
print(re.split(r'\s*[,;/]\s*', 'foo,bar  ;  baz / qux'))

# will return the delimiters if given a capturing group
print(re.split(r'(\s*[,;/]\s*)', 'foo,bar  ;  baz / qux'))

# can be useful for rejoining strings
string = 'foo,bar  ;  baz / qux'
regex = r'(\s*[,;/]\s*)'

a = re.split(regex, string)

print(a)

for i, s in enumerate(a):
    if not re.fullmatch(regex, s):
        a[i] = f'<{s}>'

print(''.join(a))

# can get rid of delimiters by using non-capturing groups
regex = r'(?:\s*[,;/]\s*)'

print(re.split(regex, string))

# maxsplit will limit the number of splits
s = 'foo, bar, baz, qux, quux, corge'

print(re.split(r',\s*', s))
print(re.split(r',\s*', s, maxsplit=3))

# including delimiters at the start / end with capturing groups with return ''
print(re.split(r'(/)', '/foo/bar/baz/'))


# re.escape, escapes special regex characters
print(re.match('foo^bar(baz)|qux', 'foo^bar(baz)|qux'))
print(re.match('foo\^bar\(baz\)\|qux', 'foo^bar(baz)|qux'))

print(re.escape('foo^bar(baz)|qux') == 'foo\^bar\(baz\)\|qux')

print(re.match(re.escape('foo^bar(baz)|qux'), 'foo^bar(baz)|qux'))
