import string
import random
alpha = string.ascii_letters
random_alpha = []
n = 100
# generate random alphabets
for i in range(n):
 alpha_count = 0
 r = random_alpha.append(random.choice(alpha))
print(f"100 Randomly Generated alphabets : \n{random_alpha}\n")
# counting alphabets
print("Counting alphabets : ")
for i in string.ascii_letters:
 print(f"No of times '{i}' in list : {random_alpha.count(i)}")
