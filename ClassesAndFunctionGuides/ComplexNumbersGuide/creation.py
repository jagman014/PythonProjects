# complex literal with sqrt(-1) = j, can have either int or float
z = 3 + 2j

print(z, type(z))

# j is the imaginary part, but 0 + 2j is still of the complex type
z = 3.14j

print(z, type(z))

# adding 0j will also produce a complex object
z = 3.14 + 0j

print(z, type(z))

# addition and subtraction is as expected
print(2 + 3j + 4 - 5j)


# complex() factory function
print(complex(3, 2), 3 + 2j, complex(3, 2) == 3 + 2j)

# both arguments are optional
print(complex(3), complex())

# can convert strings to complex, cannot have whitespace, nor two string args
print(complex("3+2j"))

try:
    print(complex("3 + 2j"))

except ValueError as e:
    print(e.__class__.__name__, e)

try:
    print(complex("3", "2"))

except TypeError as e:
    print(e.__class__.__name__, e)

# complex(a, b) returns a + b*j
# supplying a complex as one of the args may return unexpected results
print(complex(1, complex(3, 2)))  
# 1 + (3 + 2j)j -> 1 + (-2 + 3j) -> -1 + 3j

print(complex(complex(3, 2), 1))  
# (3 + 2j) + 1j -> 3 + 3j

print(complex(complex(3, 2), complex(3, 2)))  
# (3 + 2j) + (3 + 2j)j -> (3 + 2j) + (-2 + 3j) -> 1 + 5j
