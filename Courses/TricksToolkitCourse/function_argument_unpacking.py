# Example
def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))


print_vector(0, 1, 0)

list_vector = [1, 2, 3]
print_vector(*list_vector)  # * unpacks list as separate variables

gen_expr = (x * x for x in range(3))
print_vector(*gen_expr)  # unpacks tuples and comprehensions

dict_vec = {'x': 1, 'y': 2, 'z': 3}
print_vector(*dict_vec)  # * unpacks keys, only ordered as dictionaries are ordered in 3.6+
print_vector(**dict_vec)  # ** unpacks values only if keys match defined function arguments
