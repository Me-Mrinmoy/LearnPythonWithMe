'''Q6.Create an empty dictionary. Allow 4 friends to enter their favourite 
language as values and use keys as their names. Assume that the names 
are unique.'''


favlang = {}
a = input("Enter your favurite language Nayan\n")
b = input("Enter your favurite language Apurba\n")
c = input("Enter your favurite language Biswajit da\n")
d = input("Enter your favurite language Esha\n")

favlang['Nayan'] = a
favlang['Apurba'] = b
favlang['Biswajit Da'] = c
favlang['Esha'] = d

print(favlang)