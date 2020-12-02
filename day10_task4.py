import re

sentence = "1, 2, 12, 123, 1234"
result = re.findall('[0-9]{1,3}', sentence)
print(sentence, "contains numbers of length 1 to 3 are ", result)
