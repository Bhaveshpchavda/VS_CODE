def checkalphabet(alpha):
 alphabetlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 for check in alphabetlist:
  if check not in alpha.lower():
   return False
 return True
string = input()
if(checkalphabet(string) == True):
 print("Yes it is a panagram")
else:
 print("No not a panagram")