# WAP to check whether the letter passed is a vowel or not

letter = input("Enter a letter: ")
if (letter in "aeiou") or (letter in "AEIOU"):
    print("It is a vowel")

else:
    print("it is not a vowel")