try:
    name = 'String'
    print(nam)
except NameError:
    print("Name error occurred")
except:
    print("Other error occurred")
finally:
    print("Job Done")
