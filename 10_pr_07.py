def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Anish is a good      "
n = remove_and_split(this, "Anish")
print(n)
print(this)
print(this.strip())