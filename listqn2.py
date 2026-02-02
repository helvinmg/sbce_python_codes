'''Read a list of n elements from user
Remove duplicate values from the list
'''
n=int(input("How many values "))
lst=[]#[1,2,2,3,4,4,1]
for _ in range(n):
    ele=int(input("Enter list value: "))
    lst.append(ele)
lst_unique=[]#[1,2,3,4]
for ele in lst:
    if ele not in lst_unique:
        lst_unique.append(ele)
print("list without duplicates: ",lst_unique)
    
