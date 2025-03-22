'''Q1.Write a program to find greatest of four
numbers entered by the user.'''


num1 = int(input("Enter the 1st number:"))
num2 = int(input("Enter the 2nd number:"))
num3 = int(input("Enter the 3rd number:"))
num4 = int(input("Enter the 4th number:"))

greatest = num1

if num2 > greatest:
    greatest = num2

if num3 > greatest:
    greatest = num3

if num4 > greatest:
    greatest = num4

print("The greatest of four number is:", greatest)