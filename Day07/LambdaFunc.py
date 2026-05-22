# Lambda Function: anonymous function required for a short period of time
# it can take numerous arguments
# it can have only 1 expression

a = lambda b: b * 5     # b becomes a temporary function which can not be used after this
print(a(4))

x = lambda a,b,c : (a + b) * c
print(x(2,3,5))