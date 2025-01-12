'''
Stack: Sort Stack ( ** Interview Question)
The sort_stack function takes a single argument, a Stack object.  The function should sort the elements in the stack in ascending order (the lowest value will be at the top of the stack) using only one additional stack. 

The function should use the pop, push, peek, and is_empty methods of the Stack object.

Note: This is a new function, not a method within the Stack class. So, your indent should be all the way to the LEFT.

This will use the Stack class we created in these coding exercises:



The function should perform the following tasks:

Create a new instance of the Stack class called sorted_stack.

While the input stack is not empty, perform the following:

Pop the top element from the input stack and store it in a variable temp.

While the sorted_stack is not empty and its top element is greater than temp, pop the top element from sorted_stack and push it back onto the input stack.

Push the temp variable onto the sorted_stack.

Once the input stack is empty, transfer the elements back from sorted_stack to the input stack. To do this, while sorted_stack is not empty, pop the top element from sorted_stack and push it onto the input stack.



You can also click on "Hints" (above) to see the pseudo-code.

Overall, the function should have a time complexity of O(n^2), where n is the number of elements in the original stack, due to the nested loops used to compare the elements.  However, the function should only use one additional stack, which could be useful in situations where memory is limited.

'''
class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()




def sort_stack(my_stack):
    temp_stack = Stack()
    while not my_stack.is_empty():
        poped_element = my_stack.pop()
        while not temp_stack.is_empty() and temp_stack.peek() > poped_element:
            my_stack.push(temp_stack.pop())
        temp_stack.push(poped_element)
        
    while not temp_stack.is_empty():
        my_stack.push(temp_stack.pop())
                
    # return my_stack
                
    




my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""

'''Ideal solution
def sort_stack(stack):
    # Create a new stack to hold the sorted elements
    additional_stack = Stack()
 
    # While the original stack is not empty
    while not stack.is_empty():
        # Remove the top element from the original stack
        temp = stack.pop()
 
        # While the additional stack is not empty and 
        #the top element is greater than the current element
        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            # Move the top element from the additional stack to the original stack
            stack.push(additional_stack.pop())
 
        # Add the current element to the additional stack
        additional_stack.push(temp)
 
    # Copy the sorted elements from the additional stack to the original stack
    while not additional_stack.is_empty():
        stack.push(additional_stack.pop())
'''