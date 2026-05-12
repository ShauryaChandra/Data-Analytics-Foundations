#endswith() - returns true if a string ends with the specific value
"""
a = "Harry Potter"

print(a.endswith("r"))
print(a.endswith("t", 6, 9))

#startswith() - returns true if a string starts with the specific value

print(a.startswith("H"))
print(a.startswith("P", 6,9))
"""
"""
# swapcase() - swap cases, lower to upper and vice versa

#strip() - returns a trimmed version of the string
a = "   ...harry potter****     "
print(a)
print(a.strip("., *, "))
"""
"""
#split() - splits the string at the specified separator, and returns a list

a = "#OOFD#BRB#OMW"
b = "hello. my name is shaur. i am 20 years old"

print(b.split("."))
print(a.split("#"))
"""
"""
#ljust() - returns a left justified version of the string
#rjust() - returns a right justified version of the string
a = "Harry potter"
x = a.ljust(20)
y = a.rjust(20,"-")

print(x, "is my fav movie")
print(y, "is not my fav movie") 
"""       
"""
#replace() - returns a string where a specified value is replaced with a specified value

a = "my name is shaur"
print(a.replace("shaur", "Shaurya"))
"""
"""
#rindex() / rfind - searches a string for a specified value and returns the last position of where it was found
a = "Doctor Strange in the Multiverse of Madness"
print(a.rindex("Madness"))
"""
#string slicing - cutting strings in small pieces
a = "Doctor Strange in the Multiverse of Madness"
b = "0123456789"
print(a[0:7])
print(a[7:14])
print(a[-7:])
print(b[::2])
print(b[:7])
print(b[::-1])      #gives reverse as gap goes towards minus
print(b[6:0:-1])