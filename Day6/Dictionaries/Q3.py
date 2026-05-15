# WAP to multiply all the items in a dictionary

a = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5}

product = 1

for i in a:
    product *= a[i]

print(product)