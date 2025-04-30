# Importsnt: This syntax will create an empty dictionary and not an empty set
a = {}
print(type(a))

# An empty set can be created using the below syntax:
b = set()
print(b)
print(type(b))
b.add(4)
b.add(5)
print(b)