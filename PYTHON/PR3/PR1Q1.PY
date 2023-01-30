import random

ranks = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

random_number = random.randint(1, 52)

rank = ranks[(random_number-1) % 13]
