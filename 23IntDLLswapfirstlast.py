class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def swap_first_last(self):
        if self.length <= 1:
            return
        temp = self.head.value
        self.head.value = self.tail.value
        self.tail.value = temp
    
    
    

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)


print('DLL before swap_first_last():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.swap_first_last()


print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before swap_first_last():
    1
    2
    3
    4

    DLL after swap_first_last():
    4
    2
    3
    1

"""

'''code with comments
def swap_first_last(self):
    # 1. Check if the doubly linked list is empty or has only one node. 
    # If so, there's nothing to swap, hence exit the function early.
    if self.head is None or self.head == self.tail:
        return
    
    # 2. If the list has more than one node, swap the values of the 
    # head (first node) and tail (last node).
    # Note: We're only exchanging the data stored in the nodes, 
    # using tuple t swap rather than altering the structure of the linked list itself.
    self.head.value, self.tail.value = self.tail.value, self.head.value'''