'''Q2.Write a program to greet all the person names stored in a
list l1 and which starts with S.'''


l1 = ["Mrinmoy","Subrata","Somu","Sahini","Akash"]

for name in l1:
    if name.startswith("S"):
        print("Hello" + name, "you are one of the best part of my life")
        