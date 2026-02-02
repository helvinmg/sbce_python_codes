try:
    print(1/0)
except Exception as e:
    print("Im handling the exception")
    print("Exception: ",e)
finally:
    print("I work always")
    #closing resources, cleaning
