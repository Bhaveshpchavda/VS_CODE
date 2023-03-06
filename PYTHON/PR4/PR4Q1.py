s='[@_!#$%^&*()<>?/\|}{~:,"]'
name = input("Enter your name : ")
name = list(name)
print(name)
for i in range(0,len(name)):
    if name[i].isnumeric() or name[i] in s:
        print("Enter a valid name")

age = int(input("Enter your Age : "))
addr = input("Enter your address : ")

contact = input("Enter your contack no : ")
if not contact.isnumeric() or not len(contact) == 10:
    print("Enter a valid Contact no.")

pincode = input("Enter your pincode : ")
if not pincode.isnumeric() or not len(pincode) == 6:
    print("Enter a valid Pincode")
hobbies = input("Enter your hobbies : ")
lifegoal = input("Enter your life goal : ")
if age > 19:
    print("Visit www.retirement.com to getting excitting retirement policies")
elif age > 12:
    print("Here are some Education scholarships you should look for")
else:
    print("Here are some Education camps in your cities you should look for")