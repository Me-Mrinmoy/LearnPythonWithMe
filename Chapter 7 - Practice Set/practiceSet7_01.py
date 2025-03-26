'''Q1. Write a program to print a multiplication 
table of a given number--'''


num = int(input("Enter the number\n"))
for i in range(1,11):
     '''print(str(num)+ "X" + str(i) + "=" + str(i*num))'''
     print(f"{num}X{i}={num*i}")