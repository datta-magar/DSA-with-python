"""
Set: Find Pairs ( ** Interview Question)
You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.

Write a function called find_pairs that takes in three arguments: arr1, arr2, and target, and returns a list of all such pairs.  Assume that each array does not contain duplicate values.

The tests for this exercise assume that arr1 is the list being converted to a set.

Input

Your function should take in the following inputs:

arr1: a list of integers

arr2: a list of integers

target: an integer


Output

Your function should return a list of tuples, where each tuple contains two integers from arr1 and arr2 that add up to target.



Example 1:

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
target = 9
 
pairs = find_pairs(arr1, arr2, target)
print (pairs)
# Expected output: [(3, 6)]
# Explanation: There's only one pair that adds up to 9: 3 from arr1 and 6 from arr2.


Example 2:

arr1 = [0, 1, 2]
arr2 = [7, 8, 9]
target = 10
 
pairs = find_pairs(arr1, arr2, target)
print (pairs)
# Expected output: [(1, 9), (2, 8)]
# Explanation: The pairs that add up to 10 are (1, 9) and (2, 8).


Example 3:

arr1 = [1, 2, 3, 5]
arr2 = [1, 3, 4, 5]
target = 6
 
pairs = find_pairs(arr1, arr2, target)
print(pairs)
# Expected output: [(5, 1), (3, 3), (2, 4), (1, 5)]
# Explanation: The pairs that add up to 6 are (5, 1), (3, 3), 
# (2, 4), and (1, 5). Each pair consists of one element from arr1 
# and one element from arr2 that together sum to the target value.


Example 4:

arr1 = [1, 2, 3, 5]
arr2 = [1, 3, 4, 5]
target = 11
 
pairs = find_pairs(arr1, arr2, target)
print(pairs)
# Expected output: []
# Explanation: There are no pairs in arr1 and arr2 that add up to 11.

"""

def find_pairs(arr1, arr2, target):
    tuple_list = []
    for num in arr1:
        complement = target - num
        if complement in arr2:
            tuple_list.append((num,complement))
    return tuple_list




arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""

"""
def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    pairs = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))
    return pairs




The find_pairs function takes three arguments: arr1, arr2, and target.

arr1 and arr2 are lists of integers.

The function creates a set called set1 containing all the elements in arr1.

target is also an integer, which represents the target sum that the function is looking for.

The function then initializes an empty list called pairs.

The function then loops through each element in arr2 and for each element, it calculates its complement as complement = target - num.

The function then checks if complement is present in set1 using the in operator.  If it is, then the function has found a pair of numbers that add up to target, and it appends this pair (in the form of a tuple) to the pairs list.

Finally, the function returns the pairs list, which contains all pairs of numbers from arr1 and arr2 that add up to target.



Code with inline comments:



def find_pairs(arr1, arr2, target):
    # Convert arr1 to a set for O(1) lookup
    set1 = set(arr1)
    # Initialize an empty list to store the pairs
    pairs = []
    # Loop through each number in arr2
    for num in arr2:
        # Calculate the complement of the current number
        complement = target - num
        # Check if the complement is in set1
        if complement in set1:
            # If it is, add the pair to the pairs list
            pairs.append((complement, num))
    # Return the list of pairs that add up to the target value
    return pairs



"""