import random
animal = []
for i in range(50):
    animal.append(random.randint(1,30))

if 1 in animal:
    for j in range(len(animal)):
        if animal[j] == 1:
            print("The lion in in cage ",j)
            break
else:
    animal.append(1)
    print("The lion is in cage : ",len(animal)-1)