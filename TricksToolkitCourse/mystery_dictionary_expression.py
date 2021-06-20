# Example dictionary
dict_0 = {
    True: 'yes',
    1: 'no',
    1.0: 'maybe'
}

print(dict_0)  # returns {True: 'maybe'}

xs = dict()
xs[True] = 'yes'
print(xs)  # returns {True: 'yes'}

xs[1] = 'no'
print(xs)  # returns {True: 'no'}

xs[1.0] = 'maybe'
print(xs)  # returns {True: 'maybe'}

# Overwrites value of True key, due to 1 or 1.0 == True
# seen as equivalent key values
