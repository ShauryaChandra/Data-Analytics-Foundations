# WAP to create a billing system at supermarket

while True:
    name = input("Enter customer's name: ")
    total = 0

    while True:
        print("enter amount and quantity: ")

        amount = float(input("enter amount: "))
        quantity = int(input("enter quantity: "))

        total += amount*quantity
        repeat = input("do you want to add more items? ")
        if repeat == "no" or repeat == "No":
            break

    print("-" * 40)
    print("Name: ",name)
    print("Amount to be paid: ", total)
    print("-" * 40)
    print("*****Happy Shopping*****")

    repeat1= input("do you want to go to the next customer?(yes/no)")
    if repeat1 == "no" or repeat == "No":
        break