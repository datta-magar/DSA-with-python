#1. check pointer for integer (int is immutable so pointer will change) #2 dict(is mutable so pointer will be same) pointer behave exact opposite to integer
num1 = 11
num2 = num1

print('Before num2 is updated')
print('num1 =', num1)
print('num2 =', num2)

print('\nnum1 points to:', id(num1))
print('num2 points to:', id(num2))

num2 = 22

print('\nAfter num2 is updated')
print('num1 =', num1)
print('num2 =', num2)

print('\nnum1 points to:', id(num1))
print('num2 points to:', id(num2))

#intger is immutable so thats why we cannot modify it and it will change the pointer by creating new id

#2. check pointer for dict

dict1= {
    'value': 11
}

dict2 = dict1

print('\nBefore value is updated')
print('dict1 = ',dict1)
print('dict2 = ',dict2)

print('\nndict1 points to:', id(dict1))
print('ndict2 points to:', id(dict2))

dict2['value'] = 22

print('\nAfter value is updated')
print('dict1 = ',dict1)
print('dict2 = ',dict2)

print('\nndict1 points to:', id(dict1))
print('ndict2 points to:',   id(dict2))

#so the value of bith dict1 and dict2 changing, now we can set the pointer of dict2 to another pointer

print('\nset dict1, dict2 pointer to dict3')
dict3 = 33
dict1 = dict3
dict2 = dict3

print('dict1 = ',dict1)
print('dict2 = ',dict2)
print('dict3 = ',dict3)

print('\nndict1 points to:', id(dict1))
print('ndict2 points to:', id(dict2))
print('ndict3 points to:',   id(dict3))

#the previous pointer value python will remove this through process of garbage collection