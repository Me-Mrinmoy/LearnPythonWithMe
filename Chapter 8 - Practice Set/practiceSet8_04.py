# Write a program using recursive function print the sum of n natural numbers--

# n! = (n-1)! * n
# sum(n) = sum(n-1) + n

def sum_recursive(n):
    if n==1 or n==0:
        return 1
    return n * sum_recursive(n-1)

# f = factorial_iter(5)
f = sum_recursive(0)
print(f)