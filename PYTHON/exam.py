def compute_hcf(x, y):
    hcf=0
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1=int(input())
num2=int(input())

print(compute_hcf(num1, num2))




# notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

# amount = int(input("Enter an integer value: "))

# note_counts = [0] * len(notes)
# # print(len(notes))
# # print(note_counts)

# for i in range(len(notes)):
#     note_counts[i] = amount // notes[i]
#     amount -= note_counts[i] * notes[i]

# for i in range(len(notes)):
#     if note_counts[i] >= 0:
#         print(str(notes[i]) + " Rs. notes: " + str(note_counts[i]))


