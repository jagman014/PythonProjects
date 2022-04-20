# several bad coding styles
print((lambda _: list(map(lambda _: _ // 2, _)))([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# first better to name variables
print((lambda some_list: list(map(lambda n: n // 2, some_list)))([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# regular function is easier to read
def div_items(some_list):
    div_by_two = lambda n: n // 2
    return map(div_by_two, some_list)


print(list(div_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

# still not ideal, but is much more readable
