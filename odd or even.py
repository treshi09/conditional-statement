#Write a program to check whether the given number is even or odd?

num=int(input("Enter any number to check if it is even or odd: "))
if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")