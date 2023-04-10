text = "Swachh Bharat Mission\nLorem ipsum dolor sit amet,consectetur adipiscing elit.\n"
with open('read.txt', 'w') as f:
 f.write(text)
with open('read.txt', 'r') as f:
 circular = f.read()
 print(circular)
while True:
 suggestion = input("Enter your suggestion:\n")
 with open('circular.txt', 'a') as f:
  f.write(f"\nsuggestion")
 confirm = input("Enter another suggestion[Y/N]: ")
 if confirm == 'N':
  break
 elif confirm != 'Y':
  print("Error: Invalid input!")
 break
