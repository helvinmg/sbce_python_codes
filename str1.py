s="abcedef"
'''
0  1   2  3  4 5
a   b   c  d e  f
-6 -5 -4 -3 -2 -1
'''
#accessing
print(s[0])#a
print(s[1])#b
print(s[-1])#f
print(s[-2])#e
print("length",len(s))
#traversal
for ch in s:
    print(ch)
for i in range(0,len(s)):
    print(s[i])
