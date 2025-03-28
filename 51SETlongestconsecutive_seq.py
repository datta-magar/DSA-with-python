"""
Set: Longest Consecutive Sequence ( ** Interview Question)
Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).

Use sets to optimize the runtime of your solution.

Input: An unsorted array of integers, nums.

Output: An integer representing the length of the longest consecutive sequence in nums.

Example:



Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.

"""

def longest_consecutive_sequence(nums):
    nums_set = set(nums)
    longest_seq = 0 
    for num in nums:
        if num - 1 not in nums_set:
            current_num = num
            current_seq = 1
            while current_num + 1 in nums_set:
                current_num += 1
                current_seq += 1
                
            longest_seq = max(longest_seq, current_seq)
    return longest_seq

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""

"""
def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_sequence = 0
    
    for num in nums:
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1
            
            longest_sequence = max(longest_sequence, current_sequence)
    
    return longest_sequence




The longest_consecutive_sequence function takes an unsorted array of integers called nums as input, and returns the length of the longest consecutive sequence in the array.

Here's how it works:

First, the function creates a set called num_set that contains all the elements of nums. Creating a set from the array allows the function to check whether an element is in the array in constant time, which optimizes the runtime of the solution.

The function initializes the variable longest_sequence to zero, which will be updated as the function finds longer sequences.

Next, the function loops through each number in the nums array. For each number, it checks if the previous number is not in num_set, which means the current number is the start of a new sequence. If the previous number is not in num_set, the function initializes a variable current_num to the current number and a variable current_sequence to 1, since the current number is the first element of a new sequence.

The function then loops through the remaining elements of the sequence, incrementing the current_num and current_sequence variables for each element that is one more than the previous element. This loop stops when the next element is not in num_set, which means the sequence has ended.

Once the loop has ended, the function updates the longest_sequence variable to the maximum of its current value and the current_sequence value, since current_sequence represents the length of the sequence that has just been found.

Finally, the function returns the longest_sequence.


The use of sets to check whether an element is in the array in constant time allows this algorithm to run in O(n) time, where n is the number of elements in the input array nums.



Code with inline comments:



def longest_consecutive_sequence(nums):
    # Create a set to keep track of the numbers in the array
    num_set = set(nums)
    longest_sequence = 0
    
    # Loop through the numbers in the nums array
    for num in nums:
        # Check if the current number is the start of a new sequence
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1
            
            # Keep incrementing the current number until the end of the sequence is reached
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1
            
            # Update the longest sequence if the current sequence is longer
            longest_sequence = max(longest_sequence, current_sequence)
    
    return longest_sequence

"""