a = "Samsung", "Apple", "Pixel"     #tuple (before conversion)
print(type(a))

a = list(a)     #conversion to list
print(type(a))

#now we can mutate 
a.append("Vivo")
print(a)

#converting back to tuple
a = tuple(a)
print(a)

#some more functions
print(a.count("Vivo"))      #how many times it has appeared
print(a.index("Apple"))     #tells you the index