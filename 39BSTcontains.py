class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right
        
    def contains(self, value):
        temp = self.root
        while True:
            if temp == None:
                return False
            if temp.value == value:
                return True
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right

my_bst = BinarySearchTree()
print(my_bst.root)
my_bst.insert(2)
my_bst.insert(1)
my_bst.insert(3)
print(my_bst.root)
print(my_bst.root.value)
print(my_bst.root.left.value)
print(my_bst.root.right.value)

print(my_bst.contains(1))
print(my_bst.contains(2))
print(my_bst.contains(3))
print(my_bst.contains(-1))

'''Ideal code
def contains(self, value):
    # Start by setting 'temp' to the root of the tree
    temp = self.root
    
    # Loop until 'temp' becomes None (end of tree)
    while (temp is not None):
        
        # If value to find is less than the current node's value
        if value < temp.value:
            # Move 'temp' to the left child and continue loop
            temp = temp.left
            
        # If value to find is greater than the current node's value
        elif value > temp.value:
            # Move 'temp' to the right child and continue loop
            temp = temp.right
            
        # If value is neither less nor greater, it must be equal
        else:
            # Value found! Return True.
            return True
            
    # If loop ends, value was not found in tree. Return False.
    return False
'''