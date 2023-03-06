import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    return set(sentence.lower()) >= alphabet


sentence = "The quick brown fox jumps over the lazy dog"
if is_pangram(sentence):
    print("The sentence is a pangram")
else:
    print("The sentence is not a pangram")
    