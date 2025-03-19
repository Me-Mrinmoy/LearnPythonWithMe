'''Q4.What will be the length of the following set S :
s = set()
s.add(20)
s.add(20.0)
s.add("20")'''

# Answer--
s = {20, 20.0, "20"}
print(s)
print(len(s))
#  Since there are two unique elements ("20" and 20.0), the output will be:2
