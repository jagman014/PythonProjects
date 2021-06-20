# neither list nor deque are explicitly thead safe

from queue import LifoQueue

# works in the same way but with put() and get()

my_stack = LifoQueue()

my_stack.put('a')
my_stack.put('b')
my_stack.put('c')

print(my_stack)

print(my_stack.get())
print(my_stack.get())

# get() will wait forever on an empty stack, 
# can use get_nowait() but will error on an empty stack

# this full thread safety costs time for it
