"""
HT: Subarray Sum ( ** Interview Question)
Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).

Your function should take two arguments:

nums: a list of integers representing the input array

target: an integer representing the target sum


Your function should return a list of two integers representing the starting and ending indices of the subarray that adds up to the target sum. If there is no such subarray, your function should return an empty list.

For example:



nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))  # should print [1, 3]


Note that there may be multiple subarrays that add up to the target sum, but your function only needs to return the indices of any one such subarray. Also, the input list may contain both positive and negative integers.


"""

def subarray_sum(nums, target):
    sum_index = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum - target in sum_index:
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i
    return []

nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = [9]
target = 9
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""

"""
def subarray_sum(nums, target):
    sum_index = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum - target in sum_index:
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i
    return []




The goal of this function is to find a subarray within the array nums whose sum equals the target. A subarray is a portion of the array. The function returns the indices that mark the start and end of this subarray. If there is no such subarray, it returns an empty list [].



Code Explanation

Initialize Dictionary sum_index:

sum_index = {0: -1}

A dictionary called sum_index is initialized.

The key 0 and its corresponding value -1 are added to the dictionary.

Why Initialize with {0: -1}?

Handling the Target in the List:

If the first number in nums is the target, current_sum - target would be 0. This 0 is already in our dictionary, allowing us to find the target right away.

Serving as a Placeholder for Logic:

This initial setup simplifies the for-loop code by providing a common starting point for summing and comparing.



Initialize current_sum:

current_sum = 0

current_sum will keep track of the sum of numbers in nums as we loop through the list.



Loop Through the Array:

for i, num in enumerate(nums):

The enumerate function helps us loop through nums and gives us both the index i and the value num at that index.



3.1 Update current_sum: current_sum += num  



3.2 Check for Target Sum: if current_sum - target in sum_index: - We check if the value (current_sum - target) exists as a key in our sum_index dictionary.



3.2.1  Return Indices

     return [sum_index[current_sum - target] + 1, i]



     - If the condition is true, return the start and end indices of the subarray whose sum is `target`.





3.3 Update Dictionary: sum_index[current_sum] = i - If (current_sum - target) is not found in sum_index, add current_sum as a new key with its corresponding index i.



Return Empty List if Subarray Not Found:

return []

If the loop completes without finding a subarray with sum equals to target, return an empty list.



This approach uses a technique often referred to as "prefix sum" and has a time complexity of O(n), where n is the length of the list nums, as it only needs to traverse the list once. It's a neat and efficient solution for finding a target sum in a continuous subarray.





Code with inline comments:



def subarray_sum(nums, target):
    # We create a dictionary called 'sum_index' to store 
    # running sums (as keys) and their corresponding 
    # indices in the array (as values).
    #
    # Why start with {0: -1}?
    # - '0' will serve as the default sum when looking for subarrays.
    # - '-1' indicates there's no subarray yet.
    # This setup helps handle special cases, such as when the 
    # first element itself is equal to the target.
    sum_index = {0: -1}
    
    # Initialize a variable 'current_sum' to keep track of the 
    # running sum as we iterate through the array.
    current_sum = 0
 
    # The enumerate function allows us to loop through 'nums'
    # while keeping track of both the index 'i' and the value 'num'.
    for i, num in enumerate(nums):
        # Update 'current_sum' by adding the current element 'num'.
        current_sum += num
 
        # We check if a subarray exists with a sum that equals the target.
        # Specifically, we check if 'current_sum - target' is already
        # a key in our 'sum_index' dictionary.
        if current_sum - target in sum_index:
            # If it is, then we have found the subarray we are looking for.
            # We return its start and end indices as a list.
            #
            # sum_index[current_sum - target] + 1 is the start index.
            # We add 1 to move past the element before the subarray starts.
            #
            # 'i' is the end index, where the subarray ends.
            return [sum_index[current_sum - target] + 1, i]
 
        # If we haven't yet found a subarray with the sum that matches
        # the target, we add the 'current_sum' and its index 'i' to
        # our 'sum_index' dictionary for future checks.
        sum_index[current_sum] = i
 
    # If we've gone through the entire list and didn't find any
    # subarray with a sum equal to the target, we return an empty list.
    return []
"""