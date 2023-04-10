
fname = input("Enter the file name: ")
with open(fname, 'r') as f:
 char_count = 0
 word_count = 0
 line_count = 0
 
 for line in f:
  line_count += 1
 
 words = line.split()
 word_count += len(words)
 char_count += len(line)
 
 
 print(f"Number of characters: {char_count}")
 print(f"Number of words: {word_count}")
 print(f"Number of lines: {line_count}")
