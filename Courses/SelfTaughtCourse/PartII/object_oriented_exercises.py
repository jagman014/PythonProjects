# Exercises 1
class Apple:
    def __init__(self, s, w, c, t):
        self.size = s
        self.weight = w
        self.colour = c
        self.type = t


apple = Apple('small', '100 g', 'green', 'granny smith')

print(apple)
print(apple.size)
print(apple.colour)
print(apple.weight)
print(apple.type)


# Exercise 2
class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        import math
        area = math.pi * (self.radius ** 2)
        return area


circle = Circle(1)

print(round(circle.area(), 2))


# Exercise 3
class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return 0.5 * self.base * self.height


triangle = Triangle(2, 2)

print(triangle.area())


# Exercise 4
class Hexagon:
    def __init__(self, sl):
        self.side_length = sl

    def calculate_perimeter(self):
        return self.side_length * 6


hexagon = Hexagon(3)

print(hexagon.calculate_perimeter())
