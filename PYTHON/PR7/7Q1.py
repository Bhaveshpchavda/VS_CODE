filename = input("Enter the filename: ")
with open(filename, "r") as f:
    content = f.read()

chapters = content.split("\n\n")  # Split the content into chapters

for i, chapter in enumerate(chapters, start=1):
    num_lines = chapter.count("\n") + 1
    num_words = len(chapter.split())
    num_chars = len(chapter)
    print(f"Chapter {i}: {num_lines} lines, {num_words} words, {num_chars} characters")
