# WAP to create area calculator

print("****AREA CALCULATOR****")
print("""Press 1 to get area of square
      press 2 to get area of rectangle
      press 3 to get area of circle""")

choice = int(input("Enter number between 1-3: "))

if choice == 1:
    side = float(input("Enter side of the square: "))
    area = side ** 2
    print("Area of the square: ", area)

elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    area = length * breadth
    print("Area of the rectangle: ", area)

elif choice == 3:
    radius = float(input("enter the radius of the circle: "))
    area = ((22/7)* (radius ** 2))
    print("the area of the circle: ", area)

else:
    print("invalid input")