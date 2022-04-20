# is vs ==
# 'is' compares identities
# == compares objects

a = [1, 2, 3]
b = a  # b points to a, changing a changes b

print(a == b)  # same values => True
print(a is b)  # same pointer => True

c = list(a)

print(a == c)  # same values => True
print(a is c)  # different pointers => False
