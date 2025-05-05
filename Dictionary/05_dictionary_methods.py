myDict ={
"fast": "In a quick maanner",
"mrinmoy":"A coder",
"marks": [1,2,5],
"anotherdict":{'mrinmoy': 'player'},
1: 2
}

# Dictionary Methods--
print(list(myDict.keys())) # prints the keys of the dictionary
print(myDict.values())      # prints the values of the dictionary
print(myDict.items())      # prints the key value of the items
print(myDict)
updateDict = {
    "Lovish":"Friend",
    "Divya": "Friend",
    "Shubam": "Friend",
    "mrinnmoy":"a dancer"

}
myDict.update(updateDict)   # Updates the dictionary by adding key values pairs from updateDict
print(myDict)

print(myDict.get("mrinmoy"))  # prints value associated with key "mrinmoy"
print(myDict["mrinmoy"])      # prints value associated with key "mrinmoy"

# The difference between get and [] syntax in Dictionaries
print(myDict.get("mrinmoy2"))      # returns none as mrinmoy2 is not present in the dictionary
print(myDict["mrinmoy2"])          # throws an error as  mrinmoy2 is not present in the dictionary


# if you want to know any methods of dictionaries get in google buddy hey! 
