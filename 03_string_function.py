
# EXAMPLE 1.
'''story = "once upon a time there was a youtuber named Mrinmoy who uploaded python course with notes"

# string functions
print(len(story))
print(story.endswith("notes"))
print(story.count("c"))
print(story.capitalize())
print(story.find("Mrinmoy"))
print(story.replace("Mrinmoy","Code with Mrinmoy"))'''


# EXAMPLE 2.
name = "mrinmoyIsGood"

# String functions---
print(len(name))   # len function printed the length of the word not his index his length 
print(name.endswith("d"))  # endsWith function checked that the end of the word is ends with d or not if ends with d return True nor False
print(name.find("n"))      # find() function finds the first occurence of the specified value
print(name.count("o"))     # count() function returns the count number of the characters of that string
print(name.replace("I","i"))  # replace("") function replace the old word and add a new word 
print(name.capitalize())   # capitalize() function convert the word first letter into capital.
print(name.center(65))     # center() function used to align a string to the center by filling paddings to the left and right to the string
print(name.casefold())     # casefold() method has converted all the uppercase letters in the string to lowercase letters. 
print(name.encode())      # encode() method encodes the string using the specified encoding
