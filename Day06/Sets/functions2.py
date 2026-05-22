a = {"Thor", "Hulk", "Wanda"}
b = {"batman", "superman", "arrow"}
c = {"Thor", "Flash"}

# # union
# print(a.union(b))

# # difference
# print(a.difference(c))      # removes elements from the first set that are also present in second sets

# # difference update
# a.difference_update(c)      #modifies the original set a directly by removing elements that are also in b.
# print(a)

# # intersection
# x = (a.intersection(c))
# print(x)

# #intersection update
# a.intersection_update(c)
# print(a)

# # Symmetric difference
# print(a.symmetric_difference(c))

a.symmetric_difference_update(c)
print(a)
