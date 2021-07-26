from collections import namedtuple

# allows for named tuple sublcasses
# allow for access via attribute selection, or list slices

# example of need in naming elements from  integer division


def custom_divmod(x, y):
    # namedtuple needs two arguments,
    # the name of the class, and a list/string of field names
    DivMod = namedtuple("DivMod", "quotient remainder")
    return DivMod(*divmod(x, y))


original = divmod(12, 5)
print(f'Standard divmod: {original}')

new = custom_divmod(12, 5)
print(f"Custom divmod: {new}")

print(f"Quotient: {new.quotient},\nRemainder: {new.remainder}")

# list of field names can be a list of strings, a generator expression,
# a whitespace or comma seperated string

Point = namedtuple("Point", ["x", "y"])
point = Point(2, 4)

print(f"Point: {point}")
print(f"x: {point.x}, y: {point.y}")

# can have default values, as well as other useful methods

Person = namedtuple("Person", "name job", defaults=["Python Developer"])

person = Person("Jane")

print(person)

# create a dictionary

print(person._asdict())

# replace field values

person = person._replace(job="Web Developer")

print(person)
