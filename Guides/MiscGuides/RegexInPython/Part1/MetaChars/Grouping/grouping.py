import re

# group represents a unit, with other meta chars applying to the entire unit
print(re.search('(bar)', 'foo bar baz'))
print(re.search('(bar)+', 'foo bar baz'))
print(re.search('(bar)+', 'foo barbar baz'))
print(re.search('(bar)+', 'foo barbarbarbar baz'))

# can get very complicated
# 2-4 occurances of bar or baz followed by an optional qux
print(re.search('(ba[rz]){2,4}(qux)?', 'barbarbazqux'))
print(re.search('(ba[rz]){2,4}(qux)?', 'barbar'))

# one or more foo optionally followed by bar 
# followed by one or zero triple digits
print(re.search('(foo(bar)?)+(\d\d\d)?', 'foofoobar'))
print(re.search('(foo(bar)?)+(\d\d\d)?', 'foofoobar123'))
print(re.search('(foo(bar)?)+(\d\d\d)?', 'foofoo123'))
