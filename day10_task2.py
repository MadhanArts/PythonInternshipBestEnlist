import re

words = ["ABabsssaabb", "qwerty"]
pattern = re.compile('ab')
for word in words:
    if pattern.findall(word):
        print("Word '", word, "' contains 'ab'", sep="")
    else:
        print("Word '", word, "' not contain 'ab'", sep="")
