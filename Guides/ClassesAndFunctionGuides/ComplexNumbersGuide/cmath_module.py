# math modul for complex numbers, redefines all math constants
import math, cmath
import numpy as np

for name in "e", "pi", "tau", "nan", "inf":
    print(name, getattr(math, name) == getattr(cmath, name))

# special complex nan and inf
print((cmath.nanj.real, cmath.nanj.imag))
print((cmath.infj.real, cmath.infj.imag))

# cmath sqrt for complex numbers
try:
    print(math.sqrt(-1))

except ValueError as e:
    print(e.__class__.__name__, e)

print(cmath.sqrt(-1))

# root of x^4 + 1 = 0, z0 = -(sqrt(2) / 2) + (sqrt(2) / 2)j
z0 = (-cmath.sqrt(2) / 2) + (cmath.sqrt(2) / 2) * 1j

print(z0)
print(z0 ** 4)  # floating point errors do occur
print(cmath.isclose(z0 ** 4, -1))

# cannot compute other roots with pure python require numpy
print(pow(-1, 1/4))

print(np.roots([1, 0, 0, 0, 1]))  # x^4 + 1 coefficients

# cartessian to polar
z = 3 + 2j

print(cmath.polar(z))
print("abs: ", abs(z), " phase: ", cmath.phase(z))

# can use trigonometry
print(math.acos(z.real / abs(z)))
print(math.asin(z.imag / abs(z)))
print(math.atan(z.imag / z.real))

print(cmath.acos(z.real / abs(z)))

# be careful with atan, doesn't take into acount signs or zeroerrors
try:
    print(math.atan(1 / 0))

except ZeroDivisionError as e:
    print(e.__class__.__name__, e)

print(math.atan2(1, 0))

print(math.atan(1 / 1) == math.atan(-1 / -1))
print(math.atan2(1, 1) == math.atan2(-1, -1))

# convert degrees to radians
print(math.degrees(0.5880026035475675))
print(math.radians(180))

# cmath cartessian from polar requires 2 arguments
radius, angle = cmath.polar(z)

print(cmath.rect(radius, angle))

print(radius * (cmath.cos(angle) + cmath.sin(angle) * 1j))

# many complex representations
algebraic = 3 +2j
geometric = complex(3, 2)
radius, angle = cmath.polar(algebraic)
trigonometric = radius * (cmath.cos(angle) + 1j * cmath.sin(angle))
expoential = radius * cmath.exp(1j * angle)

for number in algebraic, geometric, trigonometric, expoential:
    print(f"{number:g}")
