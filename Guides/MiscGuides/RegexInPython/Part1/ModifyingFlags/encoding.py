import re

# re.A or re.ASCII -> ASCII econding
# re.U or re.UNICODE -> unicode encoding, default
# re.L or re.LOCALE -> locale encoding, non-reliable and outdated

# non-western chars, i.e. devanagari numerals
s = '\u0967\u096a\u096c'
print(s)

print(re.search('\d+', s))

s = 'sch\u00f6n'
print(s)

print(re.search('\w+', s, re.ASCII))
print(re.search('\w+', s, re.UNICODE))
print(re.search('\w+', s))
