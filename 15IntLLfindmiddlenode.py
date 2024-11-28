'''LL: Find Middle Node ( ** Interview Question)
Implement the find_middle_node method for the LinkedList class.

Note: this LinkedList implementation does not have a length member variable.

If the linked list has an even number of nodes, return the first node of the second half of the list.

Keep in mind the following requirements:

The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.

When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.

The method should return the middle node when the number of nodes is odd or the first node of the second half of the list if the list has an even number of nodes.

The method should only traverse the linked list once.  In other words, you can only use one loop.

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            temp = fast_pointer.next
            if temp.next is not None:
                fast_pointer = temp.next
            else:
                fast_pointer = temp
        # while(fast_pointer != None and fast_pointer.next != None):
        #     slow_pointer = slow_pointer.next
        #     fast_pointer = fast_pointer.next.next
        # return slow_pointer
            
        return slow_pointer




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""

'''code with coments
def find_middle_node(self):
    # 1. Initialize two pointers: 'slow' and 'fast', 
    # both starting from the head.
    slow = self.head
    fast = self.head
 
    # 2. Iterate as long as 'fast' pointer and its next 
    # node are not None.
    # This ensures we don't get an error trying to access
    # a non-existent node.
    while fast is not None and fast.next is not None:
        
        # 2.1. Move 'slow' one step ahead.
        # This covers half the distance that 'fast' covers.
        slow = slow.next
        
        # 2.2. Move 'fast' two steps ahead.
        # Thus, when 'fast' reaches the end, 'slow' 
        # will be at the middle.
        fast = fast.next.next
 
    # 3. By now, 'fast' has reached or surpassed the end, 
    # and 'slow' is positioned at the middle node.
    # Return the 'slow' pointer, which points to 
    # the middle node.
    return slow
'''