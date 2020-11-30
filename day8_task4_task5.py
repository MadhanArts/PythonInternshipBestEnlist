# Task 4
"""
When a try-catch scenario is not required?
try-catch block is not required when the developer assures that the
particular statement is not will not raise any error.
"""

# Task 5
try:
    a = int(input("Enter an integer number : "))
except ValueError:
    print("inappropriate value")
except:
    print("Some Error occurred")
else:
    print(a)
finally:
    print("Job done")
