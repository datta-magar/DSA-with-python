#implement stack using list
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peak(self):
        if self.is_empty():
            raise ImportError("peak form empty stack")
        return self.stack[-1]
        
    def size(self):
        return len(self.stack)
    
#test the Stack 
stack = Stack()
stack.push(11)
stack.push(22)
print("size ",stack.size())
print("peak ", stack.peak())
print("popped ",stack.pop())
print("is empty ", stack.is_empty())
print("popped ", stack.pop())
print("is empty ", stack.is_empty())
        
    