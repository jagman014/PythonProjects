# legal code, but unreadable and error prone
class Car:
    """Car with methods as lambda functions."""

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    brand = property(lambda self: getattr(self, '_brand'),
                     lambda self, value: setattr(self, '_brand', value))

    year = property(lambda self: getattr(self, '_year'),
                    lambda self, value: setattr(self, '_year', value))

    __str__ = lambda self: f'{self.brand} {self.year}'  # 1: error E731

    honk = lambda self: print('Honk!')  # 2: error E731


# better implementation with decorators and functions
class Car1:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def __str__(self):
        return f'{self.brand} {self.year}'

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
