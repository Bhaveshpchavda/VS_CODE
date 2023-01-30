import random
lottary_num = str(random.randint(0,99))
print(lottary_num)
num = input("Enter a number: ")
if((lottary_num[0] == num[0]) and lottary_num[1] == num[1]):
    print("You matched the number exactly and won $10000")
elif(lottary_num[0] == num[0] or lottary_num[1] == num[1]):
    print("You matched the number half correctly so you will get $2000 as reward")
elif(lottary_num[0] == num[1] and lottary_num[1] == num[0]):
    print("You haven't guessed the number in the correct order but the numbers are right so you will get $5000")
else:
    print("You lost")
