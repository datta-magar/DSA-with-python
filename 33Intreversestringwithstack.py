'''Stack: Reverse String ( ** Interview Question)
The reverse_string function takes a single parameter string, which is the string you want to reverse.

Return a new string with the letters in reverse order.

This will use the Stack class we created in the last three coding exercises:

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



def reverse_string(my_string):
    my_stack = Stack()
    for char in my_string:
        my_stack.push(char)
    new_string = ''
    while not my_stack.is_empty():
        new_string += my_stack.pop()
    return new_string




my_string = 'hello'

print ( reverse_string(my_string) )



"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""
'''commected code
def reverse_string(string):
    # create a new stack
    stack = Stack() 
    # create an empty string to store the reversed string       
    reversed_string = ""   
 
    # push each character in the string onto the stack
    for char in string:
        stack.push(char)
 
    # pop each character off the stack and append it to the reversed string
    while not stack.is_empty():
        reversed_string += stack.pop()
 
    # return the reversed string
    return reversed_string'''