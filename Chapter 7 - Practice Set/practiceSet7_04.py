'''Q4.Write a program to find wheather
a number is prime or not.'''


num = int(input("Enter a number to check if it is prime: "))
prime = True

if num <= 1:
    prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

if prime:
    print("This number is prime")
else:
    print("This number is not prime")
        