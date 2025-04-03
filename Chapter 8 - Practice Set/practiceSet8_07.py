def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     harry is a good    "
n = remove_and_split(this,"harry")
print(n)
# print(this)
# print(this.strip())