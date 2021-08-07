import re

# (?#...) regex comment
print(re.search('bar(?#This is a comment) *baz', 'foo bar baz qux'))

# | match alternatives (or)
print(re.search('foo|bar|baz', 'bar'))
print(re.search('foo|bar|baz', 'baz'))
print(re.search('foo|bar|baz', 'qux'))

# | is lazy and will return only the first match
print(re.search('foo|grault', 'foograult'))

# one or more matching foo, bar, or baz
print(re.search('(foo|bar|baz)+', 'foofoofoo'))
print(re.search('(foo|bar|baz)+', 'bazbazbazbaz'))
print(re.search('(foo|bar|baz)+', 'barbazfoo'))

# one or more digits, or one or more letters
print(re.search('([0-9]+|[a-f]+)', '456'))
print(re.search('([0-9]+|[a-f]+)', 'ffda'))
