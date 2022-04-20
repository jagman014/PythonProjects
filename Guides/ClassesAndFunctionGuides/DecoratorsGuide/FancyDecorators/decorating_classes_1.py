class Circle:
    # built-in class decorators
    def __init__(self, radius):
        self._radius = radius

    # sets as a non-callable property
    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    # allows for property to be mutable
    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    # without a setter, this is immutable
    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius ** 2

    # standard method
    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    # not instance bound
    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    # not class bound, but in the name space
    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535
