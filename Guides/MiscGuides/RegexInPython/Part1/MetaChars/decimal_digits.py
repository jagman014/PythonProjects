import re

# \d matches any decimal digits, [0-9]
print(re.search('\d', 'abc4def'))

# \D matches any non-decimal digits, [^0-9]
print(re.search('\D', '234Q678'))
