lst1=[5,6,7]
lst2=lst1
lst3=lst1.copy()#shallow copy
lst1[0]=50
'''
lst1 & lst2 are refering to same memory
'''
print("lst2:",lst2)#[50,6,7]
print("lst3:",lst3)#[5,6,7]
