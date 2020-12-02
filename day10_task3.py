import re

words = ["jan 27", "qwerty"]
pattern = re.compile('[0-9]$')
for word in words:
    if pattern.findall(word):
        print("Word '", word, "' ends with the number", sep="")
    else:
        print("Word '", word, "' does not ends with the number", sep="")
