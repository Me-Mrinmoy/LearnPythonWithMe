'''Q7. Write a program to find out wheather a given 
post is talking about "Harry" or not '''


# Input post from the user
post = input("Enter the post: ")


# Check if "harry" is in the post and print the result
if "harry" in post:
    print("This post is talking about harry")
else:
    print("This post is not talking about harry")