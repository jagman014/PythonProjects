from stack import Stack

# Exercise 1
stack = Stack()

for i in 'Yesterday':
    stack.push(i)

reversed_string = ''

for i in range(len(stack.items)):
    reversed_string += stack.pop()

print(reversed_string)

# Exercise 2
stack_2 = Stack()

for i in range(1, 6):
    stack_2.push(i)

reversed_list = []

for i in range(len(stack_2.items)):
    reversed_list.append(stack_2.pop())

print(reversed_list)
