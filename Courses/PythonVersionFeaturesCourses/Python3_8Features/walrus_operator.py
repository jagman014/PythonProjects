# Assignment expression

# allow for the assignment and return value in the same expression
# name := expression

walrus = False
print(walrus)

# combine into one line
print(walrus := True)
# prints True, and assigns it to the variable name

# example with looping
inputs = list()
current = input('Write something: ')

while current != 'quit':
    inputs.append(current)
    current = input('Write something: ')

# better implementation
inputs_1 = list()

while True:
    current = input('Write something: ')
    if current == 'quit':
        break
    inputs_1.append(current)

# Walrus edition
inputs_2 = list()

while (current := input('Write something: ')) != 'quit':
    inputs_2.append(current)
# cleaner code, maybe less readable
