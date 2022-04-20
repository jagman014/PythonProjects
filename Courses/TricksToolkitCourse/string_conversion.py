import datetime


# Example
class Car:
    def __init__(self, colour, mileage):
        self.colour = colour
        self.mileage = mileage

# Control string representation of class, i.e. print / str functions
    def __str__(self):
        return f'a {self.colour} car'

# Control representation of class, i.e. repr() / call in console
    def __repr__(self):
        return f'a car with {self.mileage} miles'


my_car = Car('red', 13785)
print(my_car)

# __str__ vs __repr__
today = datetime.date.today()

print(str(today))
print(repr(today))

# __str__ ==> easy to read, for human consumption
# __repr__ ==> unambiguous, explicit


class Car1:
    def __init__(self, colour, mileage):
        self.colour = colour
        self.mileage = mileage

    def __repr__(self):
        return f'{self.__class__.__name__}({self.colour}, {self.mileage})'


# str() calls repr() internally
my_car_1 = Car1('blue', 151515)
print(my_car_1)
print(str(my_car_1))
print(repr(my_car_1))
