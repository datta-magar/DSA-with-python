'''
LL: Find Kth Node From End ( ** Interview Question)
Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.

Given this LinkedList:

1 -> 2 -> 3 -> 4

If k=1 then return the first node from the end (the last node) which contains the value of 4.

If k=2 then return the second node from the end which contains the value of 3, etc.

If the index is out of bounds, the program should return None.

The find_kth_from_end function should follow these requirements:

The function should utilize two pointers, slow and fast, initialized to the head of the linked list.

The fast pointer should move k nodes ahead in the list.

If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.

The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.

The function should return the slow pointer, which will be at the k-th position from the end of the list.



This is a separate function that is not a method within the LinkedList class. This means you need to indent the function all the way to the LEFT. 

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
        

def find_kth_from_end(ll, k):
    slow = fast = ll.head   
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
 
    while fast:
        slow = slow.next
        fast = fast.next
        
    return slow

# def find_kth_from_end(self, k):
    # fast = self.head
    # slow = self.head
    # prev = self.head
    # while fast is not None:
    #     for _ in range(k):
    #         if fast is not None:
    #             fast = fast.next
    #         elif slow == self.head:
    #             return None
    #         else:
    #             return slow.next
    #     prev = slow
    #     slow = slow.next
    # return prev
        


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

'''code with comments
def find_kth_from_end(ll, k):
    # 1. Initialize two pointers, 'slow' and 'fast', both pointing to the 
    # starting node of the linked list.
    slow = fast = ll.head   
    
    # 2. Move the 'fast' pointer 'k' positions ahead.
    for _ in range(k):
        # 2.1. If at any point during these 'k' movements, the 'fast' 
        # pointer reaches the end of the list, then it means the list 
        # has less than 'k' nodes, and thus, returning None is appropriate.
        if fast is None:
            return None
        
        # 2.2. Move the 'fast' pointer to the next node.
        fast = fast.next
 
    # 3. Now, move both 'slow' and 'fast' pointers one node at a time until 
    # the 'fast' pointer reaches the end of the list. Since the 'fast' pointer 
    # is already 'k' nodes ahead of the 'slow' pointer, by the time 'fast' 
    # reaches the end, 'slow' will be at the kth node from the end.
    while fast:
        slow = slow.next
        fast = fast.next
        
    # 4. Return the 'slow' pointer, which is now pointing to the kth node 
    # from the end.
    return slow
'''
