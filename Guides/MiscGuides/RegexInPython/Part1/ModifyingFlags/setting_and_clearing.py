import re

# (?<flags>) setting flags -> values of a, i, L, m, s, u, x
# (?<flags>:<regex>) or (?-<flags>:<regex>) setting or clearing flags for group

print(re.search('^bar', 'FOO\nBAR\nBAZ', re.I|re.M))
print(re.search('(?im)^bar', 'FOO\nBAR\nBAZ'))

print(re.search('(?i:foo)bar', 'FOObar'))
print(re.search('(?i:foo)bar', 'FOOBAR'))

print(re.search('(?-i:foo)bar', 'FOOBAR', re.I))

s = 'sch\u00f6n'
print(s)

# can only set encoding, cannot remove it
print(re.search('(?a:\w+)', s))
print(re.search('(?u:\w+)', s))
