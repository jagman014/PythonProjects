import re

# re.sub, returns a new string from substituing regex matches
s = 'foo.123.bar.789.baz'

print(re.sub(r'\d+', '#', s))
print(re.sub(r'[a-z]+', '(*)', s))

# replaces backreferences with approriate captured group
print(re.sub(
            r'(\w+),bar,baz,(\w+)', 
            r'\2,bar,baz,\1', 
            'foo,bar,baz,qux'
            ))

# can backreference with \g<group>
print(re.sub(
            r'foo,(?P<w1>\w+),(?P<w2>\w+),qux', 
            r'foo,\g<w2>,\g<w1>,qux', 
            'foo,bar,baz,qux'
            ))
print(re.sub(
            r'foo,(\w+),(\w+),qux', 
            r'foo,\g<2>,\g<1>,qux', 
            'foo,bar,baz,qux'
            ))

# can be used to avoid ambiguity
# print(re.sub(r'(\d+)', r'\10', 'foo 123 bar')) -> re.error, invalid reference
print(re.sub(r'(\d+)', r'\g<1>0', 'foo 123 bar'))

# \g<0> refers to the text of the entire match, always valid
print(re.sub(r'\d+', r'/\g<0>/', 'foo 123 bar'))

# specifying a match length of zero, puts the substitution between every char
print(re.sub(r'x*', r'-', 'foo'))


# can use string functions as substitutions
def f(match_obj: re.Match):
    s = match_obj.group(0)  # the matching string

    if s.isdigit():
        return str(int(s) * 10)
    
    else:
        return s.upper()


print(re.sub(r'\w+', f, 'foo.10.bar.20.baz.30'))

# can limit the number of replacements with the "count" keyword
print(re.sub(r'\w+', 'xxx', 'foo.bar.baz.qux'))
print(re.sub(r'\w+', 'xxx', 'foo.bar.baz.qux', count=2))


# re.subn, identical to re.sub, but returns the number of subs as well
print(re.subn(r'\w+', 'xxx', 'foo.bar.baz.qux'))
print(re.subn(r'\w+', 'xxx', 'foo.bar.baz.qux', count=2))
print(re.subn(r'\w+', f, 'foo.10.bar.20.baz.20'))
