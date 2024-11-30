'''LL: Reverse Between ( ** Interview Question) This i last singly LL question and after this we will move on to Doubly LL
⚠️ Advanced Challenge Alert: Linked List Mastery!

Welcome to what many consider the pinnacle of Linked List challenges in this course! This exercise is not just a test of your coding skills, but also a measure of your problem-solving ability and understanding of complex data structures.

Here's how you can tackle it:

Visualize the Problem: Before diving into coding, grab a pen and paper. Sketch out the linked list and visualize each step of the process. This approach isn't just for beginners; it's exactly how seasoned developers plan their attack on complex problems.

Seek Understanding Over Speed: Take your time to really grasp each part of the problem. The goal here is deep understanding, not just a quick solution. If you find yourself stuck, that's a part of the learning process.

It's Okay to Take a Break: Feel free to step away from this challenge and return later. This course is designed to equip you with a growing set of skills, and sometimes, a bit of distance can bring new insights.

Approach Like a Pro: Remember, facing a challenging problem is what being a professional developer is all about. Use this exercise to think, plan, and code like a pro.



Now, let's dive into the exercise:

___________________________________



You are given a singly linked list and two integers start_index and end_index.

Your task is to write a method reverse_between within the LinkedList class that reverses the nodes of the linked list from start_index to  end_index (inclusive using 0-based indexing) in one pass and in-place.

Note: the Linked List does not have a tail which will make the implementation easier.

Assumption: You can assume that start_index and end_index are not out of bounds.



Input

The method reverse_between takes two integer inputs start_index and end_index.

The method will only be passed valid indexes (you do not need to test whether the indexes are out of bounds)



Output

The method should modify the linked list in-place by reversing the nodes from start_index to  end_index.

If the linked list is empty or has only one node, the method should return None.



Example

Suppose the linked list is 1 -> 2 -> 3 -> 4 -> 5, and start_index = 2 and end_index = 4. Then, the method should modify the linked list to 1 -> 2 -> 5 -> 4 -> 3 .



Constraints

The algorithm should run in one pass and in-place, with a time complexity of O(n) and a space complexity of O(1).



I highly recommend that you draw the Linked List out on a piece of paper so you can visualize the steps.

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index, end_index):
        #Ideal solution
        if self.length <= 1:
            return
        
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
        
        for _ in range(start_index):
            previous_node = previous_node.next
        
        current_node = previous_node.next
        
        for _ in range(end_index - start_index):
            node_to_move = current_node.next
            current_node.next = node_to_move.next
            node_to_move.next = previous_node.next
            previous_node.next = node_to_move
            
        self.head = dummy_node.next
        
        #My first solution
        # if start_i is not end_i:
        #     if self.length < 2:
        #         return None
        #     pre_s = start = temp = self.head
        #     for i in range(start_i):
        #         pre_s = temp
        #         temp = temp.next
        #     end = start = temp
        #     after_s = start.next
        #     for i in range(start_i, end_i):
        #         end = end.next
        #     if pre_s is not start:
        #         pre_s.next = end
        #     if end_i + 1 == self.length:
        #         start.next = None
        #     elif start is not pre_s:
        #         start.next = end.next
        #     if start == self.head:
        #         self.head = end
        #     while start is not end:
        #         temp = after_s.next
        #         after_s.next = start
        #         start = after_s
        #         after_s = temp
        


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""


'''
Solution 
Are you finding this coding exercise a bit challenging?

You're not alone—many students feel the same way. If you need some help understanding the code, just check out the "Hints" tab.

I've added some extra explanations there to guide you through it. Happy coding! 🌟



    def reverse_between(self, start_index, end_index):
        if self.length <= 1:
            return
    
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
    
        for i in range(start_index):
            previous_node = previous_node.next
    
        current_node = previous_node.next
    
        for i in range(end_index - start_index):
            node_to_move = current_node.next
            current_node.next = node_to_move.next
            node_to_move.next = previous_node.next
            previous_node.next = node_to_move
    
        self.head = dummy_node.next


Given the list:
1 → 2 → 3 → 4 → 5.

Our goal with 0-based indexing: Reverse nodes between indices 1 and 3 (inclusive) to get the result:
1 → 4 → 3 → 2 → 5.



Detailed Walkthrough:

Preliminary Steps:

1. Check if the list is empty or has only one node:

if self.length <= 1:
    return
It's pointless to reverse if there's only one or no nodes.

2. Create a dummy node:

dummy_node = Node(0)
dummy_node.next = self.head
This dummy node simplifies our code, especially if we need to reverse from the start of the list.

Preparation:

3. Navigate to the Preceding Node:

     Move to the node right before where the reversal starts.

previous_node = dummy_node
for i in range(start_index):
    previous_node = previous_node.next
Here, if we're reversing from index 1 onwards, prev will point to node 1 (index 0).

4. Set current to the node at position m:

current_node = previous_node.next
currentNode now points to the node at the index of 1, where our reversal starts.

The Core Loop:

5. Reverse nodes between start_index and end_index:

for i in range(end_index - start_index):
    node_to_move = current_node.next
    current_node.next = node_to_move.next
    node_to_move.next = previous_node.next
    previous_node.next = node_to_move
Using our example, where we reverse nodes at indices 1 through 3:



First iteration (Reversing node at index 2, i.e., node 3):

node_to_move will first point to node 3.

Node 2 (current_node) will then point to node 4.

Node 3 (node_to_move) will point to node 2.

Node 1 (previous_node) points to node 3.

Result: 1 → 3 → 2 → 4 → 5.



Second iteration (Reversing node at index 3, i.e., node 4):

node_to_move will next point to node 4.

Node 2 (current_node) will then point to node 5.

Node 4 (node_to_move) will point to node 3.

Node 1 (previous_node) points to node 4.

Result: 1 → 4 → 3 → 2 → 5.
This is our desired reversed sequence!



Finalization:

6. Reset the head:

self.head = dummy_node.next
This ensures the head now correctly points to the new start of the list if the reversal included the original first node.

Visualizing this with diagrams on paper or on a board is usually very helpful. Consider each node as a box and each pointer as an arrow. Move the boxes around as you progress through the code, and redraw the arrows according to where the pointers point.





Code with inline comments:



def reverse_between(self, start_index, end_index):
    # 1. Edge Case: If list has only one node or none, exit.
    if self.length <= 1:
        return
 
    # 2. Create a dummy node to simplify head operations.
    dummy_node = Node(0)
    dummy_node.next = self.head
 
    # 3. Init 'previous_node', pointing just before reverse starts.
    previous_node = dummy_node
 
    # 4. Move 'previous_node' to its position.
    # It'll be at index 'start_index - 1' after this loop.
    for i in range(start_index):
        previous_node = previous_node.next
 
    # 5. Init 'current_node' at 'start_index', start of reversal.
    current_node = previous_node.next
 
    # 6. Begin reversal:
    # Loop reverses nodes between 'start_index' and 'end_index'.
    for i in range(end_index - start_index):
        # 6.1. 'node_to_move' is next node we want to reverse.
        node_to_move = current_node.next
 
        # 6.2. Disconnect 'node_to_move', point 'current_node' after it.
        current_node.next = node_to_move.next
 
        # 6.3. Insert 'node_to_move' at new position after 'previous_node'.
        node_to_move.next = previous_node.next
 
        # 6.4. Link 'previous_node' to 'node_to_move'.
        previous_node.next = node_to_move
 
    # 7. Update list head if 'start_index' was 0.
    self.head = dummy_node.next
'''
