# Examples
my_items = ['a', 'b', 'c']

# C / Java style
i = 0
while i < len(my_items):
    print(my_items[i])
    i += 1

print()

# Better version
for i in range(len(my_items)):
    print(my_items[i])

print()

# Even better version
for item in my_items:
    print(item)

print()

# With use of indexing
for i, item in enumerate(my_items):
    print(i, item)

# can use range(start, end, step_size) to convert loops
print()

# from comments
print('\n'.join(my_items))
print()

print(*my_items, sep='\n')
