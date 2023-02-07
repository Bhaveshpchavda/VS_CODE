import random

def prac5_1():
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    ans = deck[:4]
    for card in ans:
        print(f"{card[0]} of {card[1]}")
    print("No. of picks=", 4)

    