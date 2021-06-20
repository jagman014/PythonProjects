import math


# @classmethod vs @staticmethod vs 'instance' methods
class MyClass:
    # points to class instance, can modify class states and object instance states
    def method(self):
        return 'instance method called', self

    # can modify class states, but not object instance states
    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    # cannot modify anything
    @staticmethod
    def staticmethod():
        return 'static method called'


obj = MyClass()

print(obj.method())  # self gives instance of object, class, and memory location, requires an instance to be called
print(obj.classmethod())  # cls returns class type
print(obj.staticmethod())

# when to use classmethods
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'

    # can simplify implementation
    @classmethod
    def margherita(cls):
        return cls(['cheese', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['cheese', 'tomatoes', 'ham'])


# when to use staticmethods
class Pizza2:
    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return f'Pizza({self.ingredients})'

    def area(self):
        return self._circle_area(self.radius)

    # self contained, doesn't effect class
    # '_' states that it is a private method and shouldn't be used
    @staticmethod
    def _circle_area(r):
        return r ** 2 * math.pi
