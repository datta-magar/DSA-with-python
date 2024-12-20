# Used singly linked list to do enqueue dequeue operation in O(1) time complexity.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

        def enqueue(self, value):
            new_node = Node(value)
            if self.length == 0:
                self.first = new_node
                self.last = new_node
            else:
                # temp = self.last
                # temp.next = new_node
                # self.last = new_node
                self.last.next = new_node
                self.last = new_node
            self.length += 1
            return True
    
    def dequeue(self):
        if self.length == 0:
            return
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        self.first = self.first.next
        temp.next = None
        self.length -= 1
        return temp
    
my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.dequeue()
my_queue.dequeue()
# print(my_queue.dequeue().value)
my_queue.print()
