''' Attempt problem 1 using while loop-'''


# Get the number from the user
number = int(input("Enter a number to print its multiplication table: "))

# Initialize the starting point of the table
i = 1

# Use a while loop to print the multiplication table
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1
