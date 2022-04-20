# Using python lists as a stack

my_stack = []

# instead of push(), lists use .append() to add last element

my_stack.append('a')
my_stack.append('b')
my_stack.append('c')

print(my_stack)

# then can use .pop() to remove the last element
# will raise an index error for an empty list

print(my_stack.pop())
print(my_stack)

# lists aren't ideal use to memory allocation and uses of .insert()
