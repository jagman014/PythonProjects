import re

# "." acts as a wildcard outside of a char class for any char except newline
print(re.search('foo.bar', 'fooxbar'))
print(re.search('foo.bar', 'foobar'))
print(re.search('foo.bar', 'foo\nbar'))
