"""
Heap: Insert
You are provided with a partial implementation of a MaxHeap class.

The class includes a method for initialization, plus helper methods for getting the left child, the right child, and the parent of a node and swapping elements in the heap.

Your task is to complete this class by implementing the insert method.

This method should take an integer as input and add it to the heap. The insertion of a new element should preserve the Max Heap property, i.e., for every node i other than the root, the value of node i is less than or equal to the value of its parent, with the maximum value at the root of the heap.

Your insert method should be efficient, ideally achieving a time complexity of O(log n), where n is the number of elements in the heap. After inserting the new element at the end of the heap, you should appropriately restructure the heap to maintain the Max Heap property. This typically involves 'bubbling up' the inserted element to its correct position in the heap.

Remember to handle edge cases, for example when the heap is empty or contains only one or two elements.
"""
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        value_index = len(self.heap)-1
        while value_index > 0 and self.heap[value_index] > self.heap[self._parent(value_index)]:
            # if self.heap[value_index] > self.heap[self._parent(value_index)]:
            self._swap(value_index, self._parent(value_index))
            value_index = self._parent(value_index)
    
    
    
myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)

print(myheap.heap)  


myheap.insert(100)

print(myheap.heap)  


myheap.insert(75)

print(myheap.heap)


"""
    EXPECTED OUTPUT:
    ----------------
    [99, 72, 61, 58]
    [100, 99, 61, 58, 72]
    [100, 99, 75, 58, 72, 61]

"""
    
"""
def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
 
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)




self.heap.append(value): The method starts by appending the value at the end of the heap (which is represented as a list here). This maintains the complete binary tree property of the heap.

current = len(self.heap) - 1: It then sets a variable current to point to the index of the newly inserted value (which is at the end of the list).

while current > 0 and self.heap[current] > self.heap[self._parent(current)]:: It then starts a loop that continues until one of the following conditions is violated:

current is not greater than 0, which means the newly inserted value has been compared with all its ancestors in the heap.

The value of the current node is not greater than its parent's value.

self._swap(current, self._parent(current)): Inside the loop, if the current node's value is greater than its parent's value, it swaps the two values to maintain the max heap property. This is done using the _swap method.

current = self._parent(current): It then moves the current index up to the parent's index for the next iteration.



This process is also known as "percolating up" or "heapify up". It ensures that the max heap property (where each parent is greater than or equal to its children) is maintained even after the new insertion.

The complexity of the insert operation in a heap is O(log n), where n is the number of elements in the heap. This is because in the worst case, we might have to traverse up to the root of the heap, and the height of a binary heap is log(n).





Code with inline comments:



def insert(self, value):
    # Add the new value at the end of the heap. This maintains
    # the complete binary tree property of the heap.
    self.heap.append(value)  
 
    # Set 'current' to the index of the newly inserted value. 'current'
    # will be used to track the value as it may move up the heap.
    current = len(self.heap) - 1  
 
    # Start a loop that continues until the heap property is restored.
    # The heap property for a max heap states that every parent node
    # must be greater than or equal to its child nodes.
    while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
        # If the newly inserted value is greater than its parent,
        # swap them to restore the heap property.
        self._swap(current, self._parent(current))
 
        # Move 'current' to its parent index for the next iteration.
        # This allows the newly inserted value to continue moving up
        # the heap until the heap property is restored.
        current = self._parent(current)

"""