# WAP to get fibonacci series upto 10 numbers
# fibonacci series: a sequence where each number is the sum of the two preceding ones

a = 0
b = 1
print(a)
print(b)
for i in range(3,11):
    c = a + b
    a = b
    b = c
    print(c)