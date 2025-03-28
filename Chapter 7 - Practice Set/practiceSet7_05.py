'''Q5. Write a program to find the sum of first n 
natural numbers using while loop--'''


# Get the value of n from the user
n = int(input("Enter a positive integer: "))

# Initialize variables
sum_natural_numbers = 0
i = 1

# Use a while loop to calculate the sum
while i <= n:
    sum_natural_numbers += i
    i += 1

# Print the result
print(f"The sum of the first {n} natural numbers is {sum_natural_numbers}")
