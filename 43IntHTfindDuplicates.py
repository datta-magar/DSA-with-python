"""
HT: Find Duplicates ( ** Interview Question)
find_duplicates()


Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).


Input:

A list of integers nums.


Output:

A list of integers representing the numbers in the input array nums that appear more than once. If no duplicates are found in the input array, return an empty list [].



Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
Output: [2, 3]
Explanation: The numbers 2 and 3 appear more than once in the input array.
 
Input: nums = [1, 2, 3, 4, 5]
Output: []
Explanation: There are no duplicates in the input array, so the function returns an empty list [].
 
Input: nums = [3, 3, 3, 3, 3]
Output: [3]
Explanation: The number 3 appears more than once in the input array.
 
Input: nums = [-1, 0, 1, 0, -1, -1, 2, 2]
Output: [-1, 0, 2]
Explanation: The numbers -1, 0, and 2 appear more than once in the input array.
 
Input: nums = []
Output: []
Explanation: There are no numbers in the input array, so the function returns an empty list [].
"""

def find_duplicates(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
        
    duplicates = []
    for num, count in num_counts.items():
        if count > 1:
            duplicates.append(num)
          
    return duplicates  
            
    




print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

"""
def find_duplicates(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
 
    duplicates = []
    for num, count in num_counts.items():
        if count > 1:
            duplicates.append(num)
 
    return duplicates




This function, find_duplicates, takes a list of numbers (nums) and returns a list of numbers that appear more than once in the input list. Let's go through it step by step:

Function Definition:

def find_duplicates(nums):
This line defines a function named find_duplicates that accepts one parameter, nums, which is expected to be a list of numbers.

Initializing a Dictionary to Count Numbers:

num_counts = {}
Here, we initialize an empty dictionary called num_counts. This dictionary will be used to keep track of how many times each number appears in the list nums.

Counting the Numbers:

for num in nums:
    num_counts[num] = num_counts.get(num, 0) + 1
This loop iterates over each number (num) in the list nums. For each number, it uses the get method to retrieve its current count from num_counts, defaulting to 0 if the number hasn't been encountered yet. It then increments this count by 1. This process effectively counts how many times each number appears in the list.

Initializing a List for Duplicates:

duplicates = []
An empty list called duplicates is created. This list will store all the numbers that are found to be duplicates (i.e., numbers that appear more than once in nums).

Identifying Duplicates:

for num, count in num_counts.items():
    if count > 1:
        duplicates.append(num)
This loop iterates over the key-value pairs in the num_counts dictionary. num is the number, and count is how many times it appeared in nums. If count is greater than 1, it means the number appeared more than once, so it's a duplicate. Such numbers are appended to the duplicates list.

Returning the Result:

return duplicates
Finally, the function returns the duplicates list, which contains all the numbers that were found more than once in the input list nums.

In summary, the function find_duplicates analyzes a list of numbers to find and return those numbers that appear multiple times in the list.





 Code with inline comments:



def find_duplicates(nums):
    # Create an empty dictionary named 'num_counts'.
    # This will be used to keep track of the frequency of each number
    # in the 'nums' list.
    num_counts = {}
 
    # Start a loop that iterates over each number in the 'nums' list.
    for num in nums:
        # For the current number 'num', update its count in the 'num_counts'
        # dictionary. If 'num' is not already in the dictionary, get(num, 0)
        # will return 0. Then, 1 is added to this value, effectively
        # initializing the count to 1 the first time 'num' is encountered.
        # If 'num' is already in the dictionary, its count is incremented by 1.
        num_counts[num] = num_counts.get(num, 0) + 1
 
    # Initialize an empty list called 'duplicates'.
    # This list will store all the numbers that appear more than once in 'nums'.
    duplicates = []
 
    # Iterate over each key-value pair in the 'num_counts' dictionary.
    # 'num' is the number from the list, and 'count' is its frequency.
    for num, count in num_counts.items():
        # Check if the count of the current number is greater than 1.
        # A count greater than 1 indicates that the number is a duplicate.
        if count > 1:
            # If the current number is a duplicate, append it to the
            # 'duplicates' list.
            duplicates.append(num)
 
    # After the loop, return the 'duplicates' list, which now contains
    # all numbers that were found more than once in the input list 'nums'.
    return duplicates
"""
