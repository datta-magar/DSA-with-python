'''
LL: Remove Duplicates ( ** Interview Question)
You are given a singly linked list that contains integer values, where some of these values may be duplicated.

Note: this linked list class does NOT have a tail which will make this method easier to implement.

Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.

Your method should not create a new list, but rather modify the existing list in-place, preserving the relative order of the nodes.

You can implement the remove_duplicates() method in two different ways:



Using a Set - This approach will have a time complexity of O(n), where n is the number of nodes in the linked list. You are allowed to use the provided Set data structure in your implementation.

Without using a Set - This approach will have a time complexity of O(n^2), where n is the number of nodes in the linked list. You are not allowed to use any additional data structures for this implementation.



Here is the method signature you need to implement:

def remove_duplicates(self):


Example:

Input:

LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5

Output:

LinkedList: 1 -> 2 -> 3 -> 4 -> 5

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
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values))

    def remove_duplicates(self):
        # #without using any data structure
        # current = prev_temp = temp = self.head
        # while temp:
        #     if temp is current:
        #         temp = temp.next
        #     else:
        #         if current.value == temp.value:
        #             prev_temp.next = temp.next
        #             temp = prev_temp.next
        #         else:
        #             prev_temp = temp
        #             temp = temp.next
        #     if temp is None and current.next is not None:
        #         current = current.next
        #         prev_temp = current
        #         temp = current.next
                
        
        # #using list and without using set
        # temp = prev_temp = self.head
        # memory_list = []
        # while temp:
        #     if temp.value not in memory_list:
        #         memory_list.append(temp.value)
        #         prev_temp = temp
        #         temp = temp.next
        #     else:
        #         prev_temp.next = temp.next
        #         temp = prev_temp.next

        # #using set
        # first and best approach
        values = set()
        previous = None
        current = self.head
        while current:
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                previous = current
            current = current.next
                
        # set1 = set()
        # temp = self.head
        # while temp:
        #     set1.add(temp.value)
        #     temp = temp.next
        # first_num = True
        # temp_node = self.head
        # for num in set1:
        #     if first_num:
        #         temp_node = Node(num)
        #         self.head = temp_node
        #         first_num = False
        #     else:
        #         new_node = Node(num)
        #         temp_node.next = new_node
        #         temp_node = temp_node.next
        


#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+


def test_remove_duplicates(linked_list, expected_values):
    print("Before: ", end="")
    linked_list.print_list()
    linked_list.remove_duplicates()
    print("After:  ", end="")
    linked_list.print_list()

    # Collect values from linked list after removal
    result_values = []
    node = linked_list.head
    while node:
        result_values.append(node.value)
        node = node.next

    # Determine if the test passes
    if result_values == expected_values:
        print("Test PASS\n")
    else:
        print("Test FAIL\n")

# Test 1: List with no duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 2: List with some duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
test_remove_duplicates(ll, [1, 2, 3])

# Test 3: List with all duplicates
ll = LinkedList(1)
ll.append(1)
ll.append(1)
test_remove_duplicates(ll, [1])

# Test 4: List with consecutive duplicates
ll = LinkedList(1)
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 5: List with non-consecutive duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
ll.append(4)
test_remove_duplicates(ll, [1, 2, 3, 4])

# Test 6: List with duplicates at the end
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 7: Empty list
ll = LinkedList(None)
ll.head = None  # Directly setting the head to None
ll.length = 0   # Adjusting the length to reflect an empty list
test_remove_duplicates(ll, [])

'''
#commented code
def remove_duplicates(self):
    # 1. Initialize a set called 'values' to store unique node values.
    values = set()
    
    # 2. Initialize 'previous' to None. 
    # This will point to the last node we've seen that had a unique value.
    previous = None
    
    # 3. Start at the head of the linked list.
    current = self.head
 
    # 4. Traverse through the linked list.
    while current:
        # 4.1. Check if the value of the current node is already in the set.
        if current.value in values:
            # 4.1.1. If yes, bypass this node by pointing the next of 
            # 'previous' to the next of 'current'.
            previous.next = current.next
            
            # 4.1.2. Decrement the length of the list.
            self.length -= 1
        else:
            # 4.2. If not, add the value to the set.
            values.add(current.value)
            
            # 4.2.1. Update the 'previous' to point to 'current' now.
            previous = current
 
        # 4.3. Move to the next node in the list.
        current = current.next

        
#solution without using set
    def remove_duplicates(self):
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                    self.length -= 1
                else:
                    runner = runner.next
            current = current.next
'''