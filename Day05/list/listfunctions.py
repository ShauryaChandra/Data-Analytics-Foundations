a = ["Thor", "Iron Man", "Hulk", "Captain America", "Hulk"]
print(a)
# to find the length of a list
print(len(a))

# to count an occurence of a particular element
print(a.count("Hulk"))

# to add to the list
a.append("Black Widow")
print(a)

# to add to a specific location
a.insert(1, "Spiderman")
print(a)

# to remove from a list
a.remove("Hulk")
print(a)

# to remove from a certain location
print(a.pop(1))
print(a)