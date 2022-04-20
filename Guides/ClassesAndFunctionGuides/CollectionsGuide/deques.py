from collections import deque

# double ended queue, implemented as a double-linked list

ticket_queue = deque()
print(ticket_queue)

# people join the queue

ticket_queue.append("Jane")
ticket_queue.append("John")
ticket_queue.append("Linda")

print(ticket_queue)

# people bought tickets

print(ticket_queue.popleft())
print(ticket_queue.popleft())
print(ticket_queue.popleft())
# print(ticket_queue.popleft()) -> error on empty queue

# deque can take an iterable and a maxlen value to limit deque size

recent_files = deque(["core.py", "README.md", "__init__.py"], maxlen=3)

print(recent_files)

recent_files.appendleft("database.py")

print(recent_files)

recent_files.appendleft("requirements.txt")

print(recent_files)

# types of iterables

print(deque((1, 2, 3, 4)))
print(deque([1, 2, 3, 4]))
print(deque("abcd"))

# cannot .pop(n) on deque

# can extend and insert items

numbers = deque([1, 2])
numbers.extend([3, 4, 5])

print(numbers)

# does appendleft for each item in iterable
numbers.extendleft([-1, -2, -3, -4, -5])

print(numbers)

# position, value
numbers.insert(5, 0)

print(numbers)

# additional methods
# clear, clears deque
# copy, creates copy of deque
# count(x), counts all occorances of x
# remove(y), removes first occurance of y

# rotate, moves value indicies by an amount

ordinals = deque(["first", "second", "third"])
ordinals.rotate()

print(ordinals)

ordinals.rotate(2)

print(ordinals)

ordinals.rotate(-2)

print(ordinals)

ordinals.rotate(-1)

print(ordinals)

# can index a deque, but not sliceP
