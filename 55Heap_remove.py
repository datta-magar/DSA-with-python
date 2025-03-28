"""
Heap: Remove
You have been provided with a MaxHeap class that includes the _sink_down method.

** We will be writing the _sink_down method in the next exercise so please do not peek at it in this exercise.  ;-)

The class includes a method for initialization, plus helper methods for getting the left child, the right child, and the parent of a node and swapping elements in the heap.

Your task is to finalize this class by implementing the remove method.

This method is designed to remove the maximum element from the heap, i.e., the root element, and reorganize the heap so it maintains its max heap property. The max heap property states that for any given node i other than the root, the value of i is at most the value of its parent.

Here's what your remove method should do in detail:

If the heap is empty, the remove method should return None.

If the heap has only one element, the remove method should remove and return this element.

If the heap has more than one element, the remove method should remove the root of the heap, place the last element in the heap at the root, and then call the _sink_down method to reorganize the heap, maintaining the max heap property.



Your remove method should be efficient, aiming for a time complexity of O(log n), where n is the number of elements in the heap.

Remember to consider edge cases where the heap is empty or contains only a few elements.


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
        self.append(value)
        pass