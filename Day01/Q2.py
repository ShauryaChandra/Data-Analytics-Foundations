# write a program to swap 2 variables

x = 12
y = 30

#Method 1 using temporary variable
'''temp = x
x = y
y = temp

print(x)
print(y)''' 

#method 2
x, y = y, x
print(x)
print(y) # Logic: left, right = right, left