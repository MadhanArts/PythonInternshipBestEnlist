import re

words = ['ABCD', 'abcd', 'AbCd', 'AbCD']
pattern = re.compile('[^A-Z]')      # OR We can also use '[A-Z]+$'
for word in words:
    if not re.findall(pattern, word):
        print("All characters in '", word, "' are uppercase", sep="")
    else:
        print("All characters in '", word, "' are not uppercase", sep="")
