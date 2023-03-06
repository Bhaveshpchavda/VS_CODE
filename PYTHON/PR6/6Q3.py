import random

b = random.randint(0,5)
a = random.randint(1,10)
i = 0
c = 1
while i < b:
    c *= a
    i += 1
print("Find the value of x for",a,"^ x = ",c)
n = int(input("Enter your answer : "))
if n == b:
    print("Correct Answer")
else:
    print("The correct answer is ",b)