import numbers

# complex superclasses real
print(issubclass(numbers.Real, numbers.Complex))

# this means many objects are an instance of complex
print(isinstance(3.14, numbers.Complex))
print(isinstance(3.14, numbers.Integral))

# complex numbers have real and imag attributes
# these attributes are read-only
z = 3 + 2j

print(z.real, z.imag)

try:
    z.real = 3.14

except AttributeError as e:
    print(e.__class__.__name__, e)

# because all numbers subclass complex, all numbers have these attributes
x = 42

print(x.real, x.imag)

# complex numbers have a conjucate() method, for the complex conjugates
print(z.conjugate())
