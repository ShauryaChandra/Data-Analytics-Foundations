# Types: 1) Local 2) Global

# 1) Local: Restricted to one block of code
# 2) Global: Not restricted


#Local
x = 24
print("First Variable of x: ", x)
def hello():
    x = 25
    return x
print(hello())

print(x)


#Global
x = 24
print("First Variable of x: ", x)
def hello():
    global x
    x = 25
    return x
print(hello())

print(x)