# Check for palindrome
num = int(input("Enter an integer: "))

temp = num
rev = 0
while num > 0:
    dig = num%10
    rev = rev*10 + dig
    num = num // 10

if rev == temp:
    print("It is a palindrome")

else:
    print("It;s not a palindrome")