# Write a python function to sum all the number in a list

def add(nums):
    total = 0
    for i in nums:
        total = total + i
    
    return (total)
print(add([2,3,5,6]))

