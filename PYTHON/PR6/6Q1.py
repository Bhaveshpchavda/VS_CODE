import random
animals = {
 1: "Lion",
 2: "Dog",
 3: "goat",
 4: "cat",
 5: "pig",
 6: "sheep",
 7: "Dragon",
 8: "zebu",
 9: "chicken",
 10: "donkey",
 11: "duck",
 12: "rooster",
 13: "rabbit",
 14: "horse"
 }

num = []
res = set()
for i in range(20):
 num.append(random.randint(1, 100))
print(f"Randomly selected cage numbers : {num}")
for j in range(20):
 if num[j] == 1:
  res.add(animals[1])
 elif num[j] == 2:
  res.add(animals[2])
 elif num[j] == 3:
  res.add(animals[3])
 elif num[j] == 4:
  res.add(animals[4])
 elif num[j] == 5:
  res.add(animals[5])
 elif num[j] == 6:
  res.add(animals[6])
 elif num[j] == 7:
  res.add(animals[7])
 elif num[j] == 8:
  res.add(animals[8])
 elif num[j] == 9:
  res.add(animals[9])
 elif num[j] == 10:
  res.add(animals[10])
 elif num[j] == 11:
  res.add(animals[11])
 elif num[j] == 12:
  res.add(animals[12])
 elif num[j] == 13:
  res.add(animals[13])
 elif num[j] == 14:
  res.add(animals[14])
 elif num[j] == 15:
  res.add(animals[15])
 elif num[j] == 16:
  res.add(animals[16])
 elif num[j] == 17:
  res.add(animals[17])
 elif num[j] == 18:
  res.add(animals[18])
 elif num[j] == 19:
  res.add(animals[19])
 elif num[j] == 20:
  res.add(animals[20])
 else:
  res.add(animals[1])
print(f"Animals from selected cage numbers : {res}")


