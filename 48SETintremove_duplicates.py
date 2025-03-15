"""
Set: Remove Duplicates ( ** Interview Question)
You have been given a list my_list with some duplicate values. Your task is to write a Python program that removes all the duplicates from the list using a set and then prints the updated list.

You need to implement a function remove_duplicates(my_list) that takes in the input list my_list as a parameter and returns a new list with no duplicates.

Your function should not modify the original list, instead, it should create a new list with unique values and return it.

Example:



Input:
my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
 
Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]


Note:

The order of the elements in the updated list may be different from the original list, as sets are unordered.


"""

def remove_duplicates(my_list):
    my_set = set(my_list)
    return list(my_set)



my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)
print(new_list)



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    (Order may be different as sets are unordered)

"""

"""
def remove_duplicates(my_list): 
    # Convert the list to a set and then back to a list to remove duplicates 
    new_list = list(set(my_list)) 
    return new_list


In this code, we have defined a function remove_duplicates that takes in a list my_list as a parameter.

Inside the function, we convert the input list to a set using set(my_list).

Since sets only contain unique elements, this will automatically remove any duplicates.

We then convert the set back to a list using list(set(my_list)) and store the result in a new list variable called new_list.

Finally, we return the updated new_list.


"""