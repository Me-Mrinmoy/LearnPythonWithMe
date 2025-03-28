'''Q6.Wite a program to calculate the factorial of a given number using for loop. '''


# n! = 1 x 2 x 3 x ...x  n


num = int(input("Enter the number\n"))
factorial = 1
for i in range(1,num+1):
    factorial = factorial * i
    print(f"The factorial of the number is:",{factorial})
    