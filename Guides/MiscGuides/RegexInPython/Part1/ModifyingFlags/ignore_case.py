import re

# re.I or r.IGNORECASE, makes matches case insensitive

print(re.search('a+', 'aaaAAA'))
print(re.search('A+', 'aaaAAA'))
print(re.search('a+', 'aaaAAA', re.I))
print(re.search('A+', 'aaaAAA', re.IGNORECASE))

print(re.search('[a-z]+', 'aBcDeF'))
print(re.search('[a-z]+', 'aBcDeF', re.I))
