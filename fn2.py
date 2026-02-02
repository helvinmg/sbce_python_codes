#default parameters
def findsum(a,b=0,c=0):
    print(a+b+c)

findsum(10,25)
findsum(10,10,10)
findsum(10)
#special parameters
def findmult(*args):
    prod=1
    for n in args:
        prod=prod*n
    print("product is",prod)

