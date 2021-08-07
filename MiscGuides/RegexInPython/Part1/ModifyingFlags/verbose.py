import re

# re.X or re.VERBOSE, allows whitespace and comments in regex

# american style phone numbers
regex = r'^(\(\d{3}\))?\s*\d{3}[-.]\d{4}$'

print(re.search(regex, '414.9229'))
print(re.search(regex, '414-9229'))
print(re.search(regex, '(712)414-9229'))
print(re.search(regex, '(712) 414-9229'))

regex = r"""
            ^               # start of string
            (\(\d{3}\))?    # optional area code
            \s*             # optional whitespace
            \d{3}           # three-digit prefix
            [-.]            # separator character
            \d{4}           # four-digit line number
            $               # end of string
        """

print(re.search(regex, '414.9229', re.VERBOSE))
print(re.search(regex, '414-9229', re.VERBOSE))
print(re.search(regex, '(712)414-9229', re.X))
print(re.search(regex, '(712) 414-9229', re.X))

# need to be mindful of intentional whitespace not escaped

print(re.search('foo bar', 'foo bar'))
print(re.search('foo bar', 'foo bar', re.VERBOSE))
print(re.search('foo\ bar', 'foo bar', re.VERBOSE))
print(re.search('foo[ ]bar', 'foo bar', re.VERBOSE))
