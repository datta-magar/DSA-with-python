'''### **Valid Parentheses**

#### **Problem Description**
Given a string `s` containing just the characters `'(', ')', '{', '}', '[' and ']'`, determine if the input string is valid. 

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

---

#### **Examples**
**Example 1:**
```plaintext
Input: s = "()"
Output: true
Explanation: The string has a single pair of parentheses correctly matched.
```

**Example 2:**
```plaintext
Input: s = "()[]{}"
Output: true
Explanation: Each open bracket has a corresponding matching close bracket in the correct order.
```

**Example 3:**
```plaintext
Input: s = "(]"
Output: false
Explanation: The string contains mismatched brackets.
```

**Example 4:**
```plaintext
Input: s = "([)]"
Output: false
Explanation: The string has brackets closed in the wrong order.
```

**Example 5:**
```plaintext
Input: s = "{[]}"
Output: true
Explanation: The string contains correctly nested brackets.
```

---

#### **Constraints**
- \( 1 \leq |s| \leq 10^4 \) (Length of the string)
- `s` consists of parentheses only: `'(', ')', '{', '}', '[', ']'`.

---

#### **Default Function Signature**
```python
def isValid(s: str) -> bool:
    # Write your code here
    pass
```

---

#### **Approach**
1. Use a **stack** to keep track of the opening brackets.
2. When encountering a closing bracket, check if the stack has a corresponding opening bracket at the top:
   - If yes, pop it off the stack.
   - If no, the string is invalid.
3. At the end, if the stack is empty, the string is valid.

---

#### **Test Cases**
- **Case 1: Simple Valid Pair**
  ```python
  assert isValid("()") == True
  ```
- **Case 2: Multiple Valid Brackets**
  ```python
  assert isValid("()[]{}") == True
  ```
- **Case 3: Mismatched Brackets**
  ```python
  assert isValid("(]") == False
  ```
- **Case 4: Incorrect Order of Closing Brackets**
  ```python
  assert isValid("([)]") == False
  ```
- **Case 5: Nested Brackets**
  ```python
  assert isValid("{[]}") == True
  ```
- **Case 6: Unmatched Closing Bracket**
  ```python
  assert isValid("]") == False
  ```
- **Case 7: Long Valid String**
  ```python
  assert isValid("(({{[[]]}}))") == True
  ```
- **Case 8: Single Opening Bracket**
  ```python
  assert isValid("(") == False
  ```

---

#### **Solution Skeleton**
```python
def isValid(s: str) -> bool:
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        # If it's a closing bracket
        if char in bracket_map:
            # Check the top of the stack
            top_element = stack.pop() if stack else '#'
            # If mismatch, return False
            if bracket_map[char] != top_element:
                return False
        else:
            # Otherwise, it's an opening bracket, push to stack
            stack.append(char)

    # Stack should be empty if valid
    return not stack

# Testing
if __name__ == "__main__":
    print(isValid("()"))  # True
    print(isValid("()[]{}"))  # True
    print(isValid("(]"))  # False
    print(isValid("([)]"))  # False
    print(isValid("{[]}"))  # True
```

You can use this code and customize it further as per your preferences!'''

def isValid(s: str) -> bool:
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {'(':')','{':'}','[':']'}
    stack = []

    for char in s:
        stack.push(char)
    
    


# Testing
if __name__ == "__main__":
    print(isValid("()"))  # True
    print(isValid("()[]{}"))  # True
    print(isValid("(]"))  # False
    print(isValid("([)]"))  # False
    print(isValid("{[]}"))  # True
