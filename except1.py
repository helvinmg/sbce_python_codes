'''Exception - Runtime Errors
Exception Handling
'''
try:
    L=[]
    #print(L[0])
    print(1/0)
except IndexError:
    print("I'm handling IndexError")
except Exception as e:
    print("Im handling the exception")
    print("Exception: ",e)
