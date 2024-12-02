'''DLL: Swap Nodes in Pairs ( ** Interview Question)

ATTENTION: Advanced Doubly Linked List Challenge Ahead!

This question is acknowledged as one of the more intricate challenges within the Doubly Linked List section. It's not unusual for students to find this task quite formidable at this point in the course.

If you're considering diving into this problem, it's crucial to approach it methodically. I recommend drawing out the list structures and operations to better visualize the problem. This challenge demands a deep understanding of Doubly Linked Lists' unique characteristics and manipulation techniques.

Use this opportunity to deepen your understanding, but also remember it's absolutely fine to come back to this problem later if it feels overwhelming now. Progress in complex concepts like these sometimes requires stepping back and revisiting with fresh insights. Good luck, and remember that perseverance is key in mastering these advanced topics!

Now, here is the problem:

_________________________________



You are given a doubly linked list.

Implement a method called swap_pairs within the class that swaps the values of adjacent nodes in the linked list. The method should not take any input parameters.

Note: This DoublyLinkedList does not have a tail pointer which will make the implementation easier.

Example:

1 <-> 2 <-> 3 <-> 4 should become 2 <-> 1 <-> 4 <-> 3

Your implementation should handle edge cases such as an empty linked list or a linked list with only one node.

Note: You must solve the problem WITHOUT MODIFYING THE VALUES in the list's nodes (i.e., only the nodes' prev and next pointers may be changed.)

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
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True
        
    def swap_pairs(self):
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
    
        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next
    
            previous_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
    
            second_node.prev = previous_node
            first_node.prev = second_node
    
            if first_node.next:
                first_node.next.prev = first_node
    
            self.head = first_node.next
            previous_node = first_node
    
        self.head = dummy_node.next
    
        if self.head:
            self.head.prev = None

    # def swap_pairs(self):
    #     if self.length <= 1:
    #         return
    #     first_node = self.head
    #     second_node = first_node.next
    #     self.head = second_node
    #     while first_node and second_node:
    #         first_node.next = second_node.next
    #         if second_node.next is not None:
    #             second_node.next.prev = first_node
    #         second_node.next = first_node
    #         second_node.prev = first_node.prev
    #         first_node.prev = second_node
    #         if second_node.prev is not None:
    #             second_node.prev.next = second_node
    #         first_node = first_node.next
    #         if first_node is not None:
    #             second_node = first_node.next
            



my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""
'''solution
Are you finding this coding exercise a bit challenging?

You're not alone—many students feel the same way. If you need some help understanding the code, just check out the "Hints" tab.

I've added some extra explanations there to guide you through it. Happy coding! 🌟





    def swap_pairs(self):
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
    
        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next
    
            previous_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
    
            second_node.prev = previous_node
            first_node.prev = second_node
    
            if first_node.next:
                first_node.next.prev = first_node
    
            self.head = first_node.next
            previous_node = first_node
    
        self.head = dummy_node.next
    
        if self.head:
            self.head.prev = None




In this function, the goal is to swap every two adjacent nodes in the doubly linked list.

Given a doubly linked list like:

1 <-> 2 <-> 3 <-> 4

After performing the swap_pairs operation, it should look like:

2 <-> 1 <-> 4 <-> 3



Method Walkthrough:

def swap_pairs(self):


Initialize a dummy node and connect it to head for easier manipulation:

dummy_node = Node(0)
dummy_node.next = self.head
This dummy node simplifies the swapping process, especially at the beginning of the list. We link the dummy's next to the head.



Set up the previous pointer:

previous_node = dummy_node
previous_node pointer always points to the node just before the first node in the pair we're about to swap.



Iterate through the list as long as there are at least two nodes left to swap:

while self.head and self.head.next:


Assign the two nodes to be swapped to first_node and second_node:

first_node = self.head
second_node = self.head.next


Swapping logic:
a. Point previousNode's next to second_node:

previous_node.next = second_node
previous_node should point to the second node of the pair after swapping.



b. Link the end of our swapped pair to the rest of the list:

first_node.next = second_node.next
This ensures that after swapping, the list remains intact.



c. Make the actual swap by reversing their next pointers:

second_node.next = first_node


Update the previous pointers for a doubly linked list:

a. Link the prev pointer of second_node:

second_node.prev = previous_node


b. Update the prev pointer for the first_node:

first_node.prev = second_node


c. Ensure that the node after our swapped pair has its prev updated:

if first_node.next:
    first_node.next.prev = first_node


Move the head pointer two nodes ahead for the next iteration:

self.head = first_node.next
This is essential since we've swapped the current pair and need to move to the next pair.



Update the previous_node pointer to point to the first_node after the swap:

previous_node = first_node
As we move on to the next pair, our previous pointer should move two nodes ahead, but since we've swapped them, it now needs to point to what was originally the first node of our pair.



Finally, reset the head of the list:

self.head = dummy_node.next
Once we've swapped all possible pairs, we adjust our head to point to the node following our dummy node.



Ensure the new head's previous pointer is None:

if self.head:
    self.head.prev = None
After all swaps, it's crucial to reset the prev pointer of the head to ensure the integrity of the doubly linked list.



Conclusion: The swap_pairs function effectively swaps adjacent nodes in pairs for a doubly linked list. By employing a dummy node, we simplify the task of swapping, especially at the beginning of the list. After all operations, we ensure the head is correctly placed, and the previous pointers are updated to retain the doubly linked list's structure. In our given example, the nodes of 1 <-> 2 <-> 3 <-> 4 get swapped to become 2 <-> 1 <-> 4 <-> 3.





Code with inline comments:



def swap_pairs(self):
    # Step 1: Initialize a dummy node to act as a placeholder
    # for the start of the list.
    dummy_node = Node(0)
 
    # Connect this dummy node to the actual head of the list.
    # This simplifies the swapping process.
    dummy_node.next = self.head
 
    # Step 2: Initialize 'previous_node' to 'dummy_node'.
    # This helps us remember the node just before the pair
    # we are about to swap.
    previous_node = dummy_node
 
    # Step 3: Loop through the list as long as there are pairs
    # of nodes available to swap.
    while self.head and self.head.next:
 
        # Identify the first node in the pair to be swapped.
        first_node = self.head
 
        # Identify the second node in the pair to be swapped.
        second_node = self.head.next
 
        # Update 'previous_node' to point to 'second_node',
        # effectively skipping over 'first_node'.
        previous_node.next = second_node
 
        # Connect 'first_node' to the node that comes after
        # 'second_node'. This ensures we don't lose the
        # rest of the list.
        first_node.next = second_node.next
 
        # Swap 'first_node' and 'second_node' by connecting
        # 'second_node' back to 'first_node'.
        second_node.next = first_node
 
        # Update the 'prev' pointers for both 'first_node'
        # and 'second_node' to maintain the doubly-linked
        # structure.
        second_node.prev = previous_node
        first_node.prev = second_node
 
        # If there's a node after 'first_node', update its
        # 'prev' to point back to 'first_node'.
        if first_node.next:
            first_node.next.prev = first_node
 
        # Move the 'head' to the node just after 'first_node'
        # to prepare for the next iteration.
        self.head = first_node.next
 
        # Update 'previous_node' to point to 'first_node'
        # for the next pair to swap.
        previous_node = first_node
    
    # After the loop, set the new head of the list to the
    # node that comes after 'dummy_node'.
    self.head = dummy_node.next
 
    # Make sure the new head's 'prev' is set to None, as it
    # is now the first node in the list.
    if self.head:
        self.head.prev = None
'''
