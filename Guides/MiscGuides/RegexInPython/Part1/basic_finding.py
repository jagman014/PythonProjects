# basic substring lookup, done char by char only for exact matching

# example string
s = 'foo123bar'

# can easily test if substring is in string
print(f"123 in sting s: {'123' in s}")

# can also find starting index of substring if in string
print(f"Location of 123 in s: {s.find('123')}") 
print(f"or using index: {s.index('123')}")
