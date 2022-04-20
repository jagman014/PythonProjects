import re

# can combine flags with bitwise or, |

print(re.search('^bar', 'FOO\nBAR\nBAZ', re.I|re.M))
