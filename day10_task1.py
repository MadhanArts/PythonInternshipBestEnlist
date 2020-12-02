import re

words = ["ABCDabcd12340", "ABCD &&12$%*("]
pattern = re.compile('[^a-zA-Z0-9]')

for word in words:
    if not pattern.findall(word):
        print("Word '", word, "' contains only [a-z, A-Z, 0-9]", sep="")
    else:
        print("Word '", word, "' not contains only [a-z, A-Z, 0-9]", sep="")
