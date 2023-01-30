import random
# n = int(input("Pick a Card from 1 to 52 : "))
n = random.randint(1,52)
print(n)
nums = ["Ace",2,3,4,5,6,7,8,9,10,"jack","Queen","King"]
if n < 14:
    print(f"The Card you picked is Clubs of {nums[(n%13)+1]}")
elif n < 27:
    print(f"The Card you picked is Hearts of {nums[(n%13)+1]}")
elif n < 40:
    print(f"The Card you picked is Spades of {nums[(n%13)+1]}")
else:
    print(f"The Card you Picked is Dimonds of {nums[(n%13)+1]}")
