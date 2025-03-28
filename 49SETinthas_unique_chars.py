"""
Set: Has Unique Chars ( ** Interview Question)
Write a function called has_unique_chars that takes a string as input and returns True if all the characters in the string are unique, and False otherwise.

For example, has_unique_chars('abcdefg') should return True, while has_unique_chars('hello') should return False.


"""
def has_unique_chars(string):
    string_set = set(string)
    if len(string) == len(string_set):
        return True
    return False




print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""

"""
def has_unique_chars(string):
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)
    return True




The has_unique_chars function takes a single argument, string, which is the string we want to check for unique characters.

The first thing the function does is create an empty set called char_set. This set will be used to keep track of the characters we have seen in the string so far.

Next, the function loops through each character in the string using a for loop. For each character, the function checks if it is already in the char_set set by using the in operator. If the character is already in the set, that means it is a duplicate, so the function immediately returns False.

If the character is not already in the set, the function adds it to the set using the add method. This way, we can keep track of all the characters we have seen so far.

After the loop has finished, the function returns True. This means that the string has no duplicates, since the function has not returned False at any point during the loop.



Code with inline comments:



def has_unique_chars(string):
    # Create an empty set to store characters
    char_set = set()
    # Loop through each character in the string
    for char in string:
        # Check if the character is already in the set
        if char in char_set:
            # If it is, return False (the string has duplicate characters)
            return False
        # If the character is not in the set, add it to the set
        char_set.add(char)
    # If we get to the end of the string without finding duplicates, return True
    return True

"""