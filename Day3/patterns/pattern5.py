# WAP to display this pattern 
"""
        *
      * *
    * * *
  * * * *
* * * * *
"""
for i in range(1,6):    #rows

    for j in range(5, i, -1):   #spaces
        print(" ", end = " ")

    for k in range(i):      #stars
        print("*", end = " ")

    print()