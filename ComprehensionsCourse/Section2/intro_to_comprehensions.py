# Comprehensions
#  list, set, dict

numbers = list((range(10)))
print(numbers)

# traditional method
squares = []
for num in numbers:
    squares.append(num * num)

print(squares)

# list comprehension method
squares_1 = [num * num for num in numbers]
print(squares_1)

# [] <- list, format [(expression) for (variable) in (list of values)]

# better formatting, looks similar to the for loop
squares_2 = [num * num
             for num in numbers]
print(squares_2)

# strings
words = 'this is a bunch of words'.split()

caps = [word.capitalize()
        for word in words]
print(caps)

# order remains the same
