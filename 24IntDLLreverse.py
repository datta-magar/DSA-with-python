'''DLL: Reverse ( ** Interview Question)
Create a new method called reverse that reverses the order of the nodes in the list, i.e., the first node becomes the last node, the second node becomes the second-to-last node, and so on.

To do this, you'll need to traverse the list and change the direction of the pointers between the nodes so that they point in the opposite direction.

Do not change the value of any of the nodes.

Once you've done this for all nodes, you'll also need to update the head and tail pointers to reflect the new order of the nodes.

Pseudo-code can be found under "Hints" (above).

'''
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
   
    def reverse(self):
        temp = self.head
        while temp is not None:
            # swap the prev and next pointers of node points to
            temp.prev, temp.next = temp.next, temp.prev
            
            # move to the next node
            temp = temp.prev
            
        # swap the head and tail pointers
        self.head, self.tail = self.tail, self.head
        
    # def reverse(self):
    #     if self.length <= 1:
    #         return
    #     dummy = Node(0)
    #     dummy.next = self.head
    #     previous_node = self.head
    #     current_node = previous_node.next
    #     while current_node:
    #         if previous_node == self.head:
    #             previous_node.next = None
    #         if current_node == self.tail:
    #             current_node.prev = None
    #         temp = current_node.next
    #         current_node.next = previous_node
    #         previous_node.prev = current_node
    #         previous_node = current_node
    #         current_node = temp
    #     self.tail = dummy.next
    #     self.head = previous_node




my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)


print('DLL before reverse():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.reverse()


print('\nDLL after reverse():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before reverse():
    1
    2
    3
    4
    5

    DLL after reverse():
    5
    4
    3
    2
    1

"""

