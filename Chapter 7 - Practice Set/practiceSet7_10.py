'''Q10. Write a program to print the multiplication table 
of n using for loop in reversed order'''

# Get the value of n from the user
num = int(input("Enter a number to print its multiplication table in reverse order: "))

# Use a for loop to print the multiplication table in reverse order
for i in range(10, 0, -1):
    print(f"{num} x {i} = {num * i}")
