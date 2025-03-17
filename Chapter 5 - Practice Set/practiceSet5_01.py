'''Q1.Write a program to create a dictionary of hindi words 
with values as their english translation. Provide user with 
an option to look it up!'''


myDict = {
    "pankha": "Fan",
    "dabba": "Box",
    "vastu" : "Item"

}
print("Optins are", myDict.keys())
a = input("Enter the hindi word\n")
print("The meaning of your word is:",myDict[a])

# Below line will throw an error if the key is not present in the dict
print("The meaning of your word is:",myDict.get(a))