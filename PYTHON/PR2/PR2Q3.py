import random
num = random.randrange(0,101)
print(num)
guess = int(input("Enter a number: "))
while guess != num:
    if guess < num:
        print("Number is too low, kindly enter a higher number: ")
        guess = int(input("Enter a number: "))
    elif guess > num:
        print("The number is too high, kindly enter a lower number: ")
        guess = int(input("Enter a number: "))
    else:
        print("You guessed the number")
