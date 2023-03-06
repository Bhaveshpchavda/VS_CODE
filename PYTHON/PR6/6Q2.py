import string
alphabet  = list(string.ascii_lowercase)
text = input("Enter a Text : ")
text = text.lower()
text = list(text)
num = []
for z in range(26):
    num.append(0)

for i in range(len(text)):
    for j in range(0,26):
        if(alphabet[j] == text[i]):
            num[j] += 1
            break

for x in range(26):
    if num[x] == 0:
        continue
    print(num[x],alphabet[x])