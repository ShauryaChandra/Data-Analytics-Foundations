# recursion : means that a function can call itself, giving us a benefit of looping through data in order to get the result

# def hello():
#     print("hello")
#     return(hello()) 

# print(hello())


# TO FIND A FACTORIAL

def fact(n):
    if n == 1:
        return 1
    
    else:
        return(n * fact(n-1))
    
print(fact(5))