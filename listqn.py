'''
Create a list of marks by
reading 5 integer values from user
'''
marks=[]
for _ in range(5):
    mark=int(input("enter the mark:"))
    marks.append(mark)
print("marks=",marks)

'''
Increase marks by 5 for those who
scored less than 20 '''
for i in range(0,len(marks)):
    if marks[i]<20:
        marks[i]=marks[i]+5





