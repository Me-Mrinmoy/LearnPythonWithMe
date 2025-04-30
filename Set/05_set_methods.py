## Creating an empty set
b = set()
print(b)
print(type(b))

##  Adding values to an empty set
b.add(4)
b.add(5)
b.add(5)
b.add(5)  # adding a value does not change a set
b.add(4)
b.add((4,5,6))  # this is not possible because set.add() takes only one argument 

## Accessing elements
# b.add({4:5}) cannot add list or dictionary to sets
print(b)

## Length of the set
print(len(b))  # Prints the length of this set

## Removal of the item
b.remove(5)   # Removes 5 from set b
b.remove(15)  # Throws an error while trying to remove 15(which is not present in the set)
print(b)

print(b.pop())
print(b)