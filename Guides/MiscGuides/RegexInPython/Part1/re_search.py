import re

s = "foo123bar"

# re.search will return a re.Match object if found or None if not
print(re.search('123', s))

# can be used for truthiness
if re.search('123', s):
    print('Found a match')

else:
    print('No match found')

# returned span in match object is the slice for the match
# match property returns which values matched in the given string
print(f"span: {re.search('123', s).span()} -> s[3, 6] = {s[3:6]}")
