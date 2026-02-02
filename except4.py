try:
    #for raising exceptions by the user
    raise ValueError("key not found")
except KeyError:
    print("There is an keyerror exception")
except Exception as e:
    print("There is an exception")
    print("Exception: ",e)
