#read a list from user and
#check if its palindrome
lst=eval(input("Enter the list: "))
#['c','a','a','c']
if lst==lst[::-1]:
    print("palindrome")
else:
    print("not palindrome")

