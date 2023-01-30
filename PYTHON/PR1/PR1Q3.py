import random

def add(x):
    sum =0
    for i in str(x):
        sum = sum + int(i)
    print("the sum of the units of the given number is (", sum, ")")
    x = random.randint(0,1000)
    print("your random number generated is (", x, ")")
    x=str(x)
    print(x)
    return sum

x = random.randint(0,1000)
print(add(x))
