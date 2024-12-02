class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def print(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

my_stack = Stack(1)
my_stack.print()