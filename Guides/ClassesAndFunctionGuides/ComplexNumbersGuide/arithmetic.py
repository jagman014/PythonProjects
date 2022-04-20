import math

# addition, sum real and imag separately
z1 = 2 + 3j
z2 = 4 + 5j

print(z1 + z2)

# automatic promoton to complex when mixing values
print(z1 + 7)

# subtraction, difference of real and imag
print(z1 - z2)

# can make negative with -
print(-z1)

# multiplication, (x1 + y1j)(x2 + y2j) -> (x1x2 + x1y2j + x2y1j - y1y2)
print(z1 * z2)

# division, z1 / z2 -> z1z2* / |z2|^2 
# -> [(x1x2 + y1y2) / (x2^2 + y2^2)] + [(y1x2 - x1y2) / (x2^2 + y2^2)]j
print(z1 / z2)

# cannot do floor division of complex
try:
    print(z1 // z2)

except TypeError as e:
    print(e.__class__.__name__, e)

# exponents, work with (**), pow(), but not math.pow()
z = 3 + 2j

print(z ** 2)
print(pow(z, 2))

try:
    print(math.pow(z, 2))

except TypeError as e:
    print(e.__class__.__name__, e)

# exponents and base can be of any numeric type
print(2 ** z)
print(z ** 0.5)
print(z ** 2j)
print(z ** z)
