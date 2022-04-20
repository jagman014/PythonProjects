# Example

# everything is a object means:
# (1) everything has a type / class
# (2) everything has attributes

x = 100
print(type(x))

y = 'abcd'
print(type(y))

z = [10, 20, 30]
print(type(z))

print(type(int))  # every classes type is type

print(type(type))

# a is an object of some sort: identifier, name, variable, or function
# python searches LEGB = Local -> Enclosing -> Global -> Built-in
# a.b means look for the name ('attribute') b inside of a

a = 'abcd'
print(dir(a))  # dir() shows attributes / methods of an object
