# WAP to display this pattern 
"""
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
"""
for i in range(1,6):    # for rows
    for j in range(1,6):    # for columns
        print(j, end = " ")
    print()