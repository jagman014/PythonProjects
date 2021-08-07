import re

# re.DEBUG, displays debug information

print(re.search('foo.bar', 'fooxbar', re.DEBUG))

regex = r'^(\(\d{3}\))?\s*\d{3}[-.]\d{4}$'

print(re.search(regex, '414.9229', re.DEBUG))
