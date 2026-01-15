#read n from user and display
#fact of n using while loop
num=int(input("enter any number"))
n=1
fact=1
while n<=num:
    fact=fact*n
    n+=1
print(f"fact of {num} is {fact}")
'''
1*1=1
1*2=2
2*3=6
6*4=24
24*5=120
'''
