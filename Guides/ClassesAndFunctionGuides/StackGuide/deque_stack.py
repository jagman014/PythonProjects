# collections module contains 'deque' (double ended queue)

from collections import deque

my_stack = deque()

# acts similar to a list for adding and removing elements

my_stack.append('a')
my_stack.append('b')
my_stack.append('c')

print(my_stack)

print(my_stack.pop())
print(my_stack)

# unlike list, deque is based on a doubly linked-list 
# requiring less memory to append items
# but requiring more to search for items
