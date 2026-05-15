a = {"Thor", "Hulk", "Wanda"}
b = {"batman", "superman", "arrow"}
c = {"Thor", "Flash"}

# isdisjoint : checks if the values in set 2 are in set 1 or not (if yes then false)
print(a.isdisjoint(b))      #true
print(a.isdisjoint(c))      #false

# issubset : same is isdisjoint but gives true if yes

# superset : ALL values should be in another set
print(c.issuperset(a))      #false

# update : can add a set to another
a.update(c)
print(a)
