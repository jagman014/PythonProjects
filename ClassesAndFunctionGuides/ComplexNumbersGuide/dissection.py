import math, cmath
from pprint import pprint
from typing import NamedTuple

# testing equality, floating point errors are abound
z1 = cmath.rect(1, math.radians(60))
z2 = complex(0.5, math.sqrt(3) / 2)

print(z1 == z2)
print(z1.real, z2.real)
print(z1.imag, z2.imag)

print(math.isclose(z1.real, z2.real))
print(cmath.isclose(z1, z2))

# ordering
# tuples ordered and compared from left to right
planets = [
            (6, "saturn"),
            (4, "mars"),
            (1, "mercury"),
            (5, "jupiter"),
            (8, "neptune"),
            (3, "earth"),
            (7, "uranus"),
            (2, "venus")
        ]

pprint(sorted(planets))
print((6, "saturn") < (4, "mars"))
print((3, "earth") < (3, "moon"))

# no natural ordering relation for complex numbers
try:
    print((3 + 2j) < (2 + 3j))

except TypeError as e:
    print(e.__class__.__name__, e)

# need to be sorted by a custom mannor, i.e. abs()
cities = {
        complex(-64.78303, 32.2949): "Hamilton",
        complex(-66.105721, 18.466333): "San Juan",
        complex(-80.191788, 25.761681): "Miami"
        }

for city in sorted(cities, key=abs, reverse=True):
    print(abs(city), cities[city])

# sting formatting
z = pow(3 + 2j, 0.5)
print(z)

print(f"{z:.2f}")
print(f"{z.real:.2f} + {z.imag:.2f}j")

# custom complex type
class Point(NamedTuple):
    x: float
    y: float


class Vector(NamedTuple):
    start: Point
    end: Point

    def __complex__(self):
        real = self.end.x - self.start.x
        imag = self.end.y - self.start.y

        return complex(real, imag)


vector = Vector(Point(-2, -1), Point(1, 1))
print(vector)

print(complex(vector))

v1 = Vector(Point(-2, -1), Point(1, 1))
v2 = Vector(Point(10, -4), Point(8, -1))

print(math.degrees(cmath.phase(v2) - cmath.phase(v1)))
