import re
pattern =r"[a-zA-Z0-9!@#$%^&*()]"
n=input("Enter Password")
print(len(n))
if re.search(pattern,n):
    if len(n)<8:
        print("Invalid")
    elif len(n)>=8 and len(n)<10:
        print("Weak")
    elif len(n)<10:
        print("Medium")
    else:
        print("Strong")  
else:
    print("Invalid")
    
    
