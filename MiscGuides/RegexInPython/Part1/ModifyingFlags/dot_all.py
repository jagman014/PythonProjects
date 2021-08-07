import re

# re.S or re.DOTALL, '.' matches newline character

print(re.search('foo.bar', 'foo\nbar'))
print(re.search('foo.bar', 'foo\nbar', re.DOTALL))
print(re.search('foo.bar', 'foo\nbar', re.S))
