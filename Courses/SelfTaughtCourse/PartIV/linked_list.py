import random


class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        if not self.head:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        node = self.head

        while node is not None:
            print(node.data, end=' ')
            node = node.next
        print('\n')

    def search(self, target):
        current = self.head

        while current is not None:
            if current.data == target:
                print('Found it!')
                return True
            else:
                current = current.next
        print('Not here!')
        return False


class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.next = nxt

    def print_node(self):
        print(self.data)


l_list = LinkedList()

for j in range(0, 20):
    i = random.randint(1, 30)
    l_list.append_node(i)

l_list.print_list()
l_list.search(10)
