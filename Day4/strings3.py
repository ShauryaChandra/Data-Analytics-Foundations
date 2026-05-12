#endswith() - returns true if a string ends with the specific value

a = "Harry Potter"

print(a.endswith("r"))
print(a.endswith("t", 6, 9))

#startswith() - returns true if a string starts with the specific value

print(a.startswith("H"))
print(a.startswith("P", 6,9))

# swapcase() - swap cases, lower to upper and vice versa

#strip() - returns a trimmed version of the string
a = "   ...harry potter****     "
print(a)
print(a.strip("., *, "))

#split() - splits the string at the specified separator, and returns a list

a = "#OOFD#BRB#OMW"
b = "hello. my name is shaur. i am 20 years old"

print(b.split("."))
print(a.split("#"))