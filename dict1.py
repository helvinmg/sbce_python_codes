#dictionary
'''{key:value,key:value}, unordered
keys must be unique, immutable type
values can be repeated'''
d1={}#will be a set
d2=dict()
fruits={'a':'apple','b':'banana'}
print(fruits)
#access - dict[key]
print("first ele",fruits['a'])
#adding pairs
fruits['k']="kiwi"
#updating
fruits['b']="berry"
print(fruits)
#deletion
del fruits['b']
#dict.pop(key),dict.clear()
fruits2={'m':'mango','p':'papaya'}
fruits.update(fruits2)
print(fruits)
#add fruits2 pairs to fruits
