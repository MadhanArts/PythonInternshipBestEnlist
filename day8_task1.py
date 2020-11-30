"""
Error types:
* ZeroDivisionError -- raise when a number is divided by 0
* NameError -- raise when name is note defined globally
* TypeError -- raise when the required type is different
* ValueError -- raise when there is inappropriate value
* IndexError -- raise when the specified index is not suited to the required
* KeyError  -- raise when specified key is not in dictionary
"""
try:
    print("Hello Arts")
except ZeroDivisionError:
    print("Zero Division Error occurred")
except NameError:
    print("Name Error occurred")
except TypeError:
    print("Type Error occurred")
except ValueError:
    print("Type Error occurred")
except IndexError:
    print("Type Error occurred")
except KeyError:
    print("Type Error occurred")
finally:
    print("finally block executed")
