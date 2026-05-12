a = "Hello World"
print(a)
print(len(a))
print(a.count("o"))
print(a.upper())
print(a.lower())
print(a.index("o"))
print(a.capitalize())
print(a.casefold())
print(a.find("l"))

text = "am saying {}"
print (text.format(a))

name = "shaur"
print(name.center(11,"*"))


"""
String methods:
1. .length       6. .capitalize
2. .count        7. .casefold
3. .upper        8. .find
4. .lower        9. .format
5. .index        10. .center


1. .length: len(a = 11
2. .count: a.count("o") = 2
3. .upper: a.upper() = HELLO WORLD
4. .lower: a.lower() = hello world
5. .index: a.index("o") = 4
6. .capitalize: a.capitalize() = Hellow world #capitalizes only first letter 
7. .casefold: a.casefold() = hello world
8. .find: a.find("l"): 2
9. .format: text = "am saying {}"
            print (text.format(a)) = am saying Hello World
10. .center: name = "shaur"
             print(name.center(11,"*")) = ***shaur***
"""