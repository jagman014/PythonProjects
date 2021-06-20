# str library has two new methods for removing
# prefixes and suffixes

# before 3.9 use of strip function
print('3 cool features in Python 3.9'.strip(' 3.9'))
# removes any chars in the grouping
# alternate using splicing
print('3 cool features in Python 3.9'[:-len(' 3.9')])

# in 3.9 allows for .removesuffix
# will only remove from the end of the string
print('3 cool features in Python 3.9'.removesuffix(' 3.9'))

# removeprefix only looks at the start of the string
print('3 cool features in Python 3.9'.removeprefix(' 3.9'))

# both look for exact matches
# only removes the first match found
print('Waikiki'.removesuffix('ki'))
