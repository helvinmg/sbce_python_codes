from datetime import date
age=int(input("Enter the age in years: "))
birthyear=(date.today().year)-age
print("birthyear",birthyear)
if birthyear>=2025:
    print("Gen Beta")
elif birthyear>=2010:
    print("Gen Alpha")
elif birthyear>=1997:
    print("Gen Z")
elif birthyear>=1981:
    print("Gen Y")
else:
    print("Gen X or Previous")
    
