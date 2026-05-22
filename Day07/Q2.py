# Write a python function that takes a number as a parameter and checks if it's prime or not 

def check_prime(num):
    if num == 1:
        print("not a prime number")

    if num == 2:
        print("It is a prime number")

    
    if num > 2:
        for i in range(2, num):
            if num % i == 0:
                print("it is not a prime number")
                break

            else:
                print("it is a prime number")
                break

check_prime(10)
check_prime(37)