name = input("What is your name? ")
age = int (input("Enter age: "))
print(name)
print(age)

length = float(input("length of a line: "))
print(length)

exp1 = eval(input("enter any equation here: "))
print(exp1) #eval is used to evaluate the expression given by the user. It can be used to perform calculations or execute code. However, it should be used with caution as it can execute arbitrary code if the input is not properly sanitized.