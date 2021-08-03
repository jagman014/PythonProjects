import re

# \s matches any whitespace chars
print(re.search('\s', 'foo\nbar baz'))

# \S matches any non-whitespace chars
print(re.search('\S', '  \n foo  \n  '))
