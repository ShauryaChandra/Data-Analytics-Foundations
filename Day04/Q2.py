#WAP to check if a number is prime or not

num = int(input("Enter an integer: "))

if num <= 1:
    print("it's not a prime number")

else:
    for i in range(2, num):
        if num % i == 0:
            print("It's not a prime number")
            break
        
    else:
        print("It is a prime number")