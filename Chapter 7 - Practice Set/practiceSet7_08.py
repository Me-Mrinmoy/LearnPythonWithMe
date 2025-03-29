'''Q8. Write a program to 
print the following star pattern (for n = 3).
*
* * 
* * *
'''

n = 3  # Number of rows is fixed to 3

# Use nested loops to print the pattern
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()  # Move to the next line after printing each row
