#Write a program to check whether the given number is greater than 15 or smaller than 15.

num=int(input("Enter any number to check if it is greater than 15 or smaller than 15: "))
if num > 15:

    print(f"{num}>15")
elif num < 15:
    print(f"{num}<15")
else:
    print(f"{num} is equal to 15")