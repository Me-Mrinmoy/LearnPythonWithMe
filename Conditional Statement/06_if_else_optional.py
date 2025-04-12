# Here returns nothing and here is no errors because 4 is not match the two conditions
'''a = 4
if(a == 7):
    print("yes")
elif(a>56):
    print("no and yes")'''


# Here returns yes because 7 is equal to 7 which is matched first condition
'''a = 7
if(a == 7):
    print("yes")
elif(a>56):
    print("no and yes")'''


# Here returns no and yes because 67 is greater than 56 so here matched the second condition
'''a = 67
if(a == 7):
    print("yes")
elif(a>56):
    print("no and yes")'''


 # Here prints i am optional because a =6 did not matched the two condition    
a = 6
if(a == 7):
    print("yes")
elif(a>56):
    print("no and yes")
else:
    print("I am optional")