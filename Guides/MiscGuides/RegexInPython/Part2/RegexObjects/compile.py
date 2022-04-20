import re

# re.compile can create a reusable object with the re methods available
print(re.search(r'(\d+)', 'foo123bar'))

re_obj = re.compile(r'(\d+)')
print(re.search(re_obj, 'foo123bar'))

print(re_obj.search('foo123bar'))

print(re.search('ba[rz]', 'FOOBARBAZ', flags=re.I))

re_obj = re.compile('ba[rz]', flags=re.I)
print(re.search(re_obj, 'FOOBARBAZ'))

print(re_obj.search('FOOBARBAZ'))
