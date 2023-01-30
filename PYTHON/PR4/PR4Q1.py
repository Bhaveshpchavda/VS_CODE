import string

name = input("Enter Name:")

for ch in string.ascii_lowercase:
    if(ch not in name):
        print("invalid")
        break
    else:
        print("Valid")
        break 
