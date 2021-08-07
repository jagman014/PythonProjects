import re

# (?(<n>)<yes-regex>|<no-regex>)
# (?(<name>)<yes-regex>|<no-regex>)
# matches <yes-regex> if group numbered <n> 
# or named <name> exists else matches <no-regex>

# optially starts with ###, match foo, matches bar if group 1 exists else baz
regex = r'^(###)?foo(?(1)bar|baz)'

print(re.search(regex, '###foobar')) # starts with ### -> creates group 1
print(re.search(regex, '###foobaz')) # doesn't match bar
print(re.search(regex, 'foobar')) # doesn't start with ### -> no group created
print(re.search(regex, 'foobaz')) # matches baz

# matches starts with optional non-word char, literal foo, 
# same non-word char if group ch exists, else nothing end of string
named_regex = r'^(?P<ch>\W)?foo(?(ch)(?P=ch)|)$'

print(re.search(named_regex, 'foo')) # ch group not created, matches empty
print(re.search(named_regex, '#foo#')) # same non-word char at start and end, matches
print(re.search(named_regex, '@foo@'))
print(re.search(named_regex, '#foo')) # no non-word char at end, doesn't match
print(re.search(named_regex, '@foo'))
print(re.search(named_regex, '#foo@')) # different non-word chars, doesn't match
print(re.search(named_regex, '@foo#'))

