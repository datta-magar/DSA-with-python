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

my_bst = BinarySearchTree()
print(my_bst.root)
my_bst.insert(2)
my_bst.insert(1)
my_bst.insert(3)
print(my_bst.root)
print(my_bst.root.value)
print(my_bst.root.left.value)
print(my_bst.root.right.value)

'''Ideal code
def insert(self, value):
    # Create a new node with the provided value
    new_node = Node(value)
 
    # Check if the tree is empty
    if self.root is None:
        # Make the new node the root and return True
        self.root = new_node
        return True
 
    # Start at the root of the tree
    temp = self.root
 
    # Loop until the correct spot is found
    while (True):
 
        # Check for duplicate values
        if new_node.value == temp.value:
            # Duplicate found, return False
            return False
 
        # Check if the new value is less than current node's value
        if new_node.value < temp.value:
            # Is the left child spot empty?
            if temp.left is None:
                # Insert new node as left child, return True
                temp.left = new_node
                return True
            # If not empty, move to left child
            temp = temp.left
 
        # If new value is greater, go to the right child
        else:
            # Is the right child spot empty?
            if temp.right is None:
                # Insert new node as right child, return True
                temp.right = new_node
                return True
            # If not empty, move to right child
            temp = temp.right
'''