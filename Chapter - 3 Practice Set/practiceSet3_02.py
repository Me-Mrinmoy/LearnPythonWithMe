'''Q2.Write a program to fill in a letter template
given below with name and date
letter = Date <|NAME|>
           You are Selected
           <|DATE|>'''



letter = '''Dear <|NAME|>
 This is GOOGLE.I am happy to share with you that You are selected in our company i wish your future more bright with us.
 Thanks,regards
 SUNDAR PICHAI

Date = <|DATE|>
'''
name = input("Enter Your Name\n")
date = input("Enter date\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>", date)
print(letter)