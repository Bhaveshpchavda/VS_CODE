import random
#------------------------------------------------------ 1
def prac5_1():
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    cpy = [1,1,1,1]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
    "Queen", "King", "Ace"]
    cnts,n = 0,0
    ans = []
    while cnts!=4:
        r = random.randint(0,3)
        if cpy[r]:
            rnks = random.choice(ranks)
            string = rnks+" of "+suits[r]
            ans.append(string)
            cpy[r] = 0
            cnts+=1
        n+=1
    for i in ans:
        print(i)
    print("No. of picks = ",n)
    
prac5_1()