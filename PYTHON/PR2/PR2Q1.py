amount = 11.56
dollars = int(amount)
quarters= int((amount-dollars)/0.25)
dimes= int(((amount-dollars)-quarters*0.25)/0.10)
nickels= int(((amount-dollars) - quarters*0.25 - dimes*0.10)/0.05)
pennies= int(((amount-dollars) - quarters*0.25 - dimes*0.10 -
nickels*0.05)/0.01)
total= dollars+ quarters + dimes + nickels + pennies
print(f"Your amount {amount} consists of:")
print ("dollars ", dollars)
print("Quarters ", quarters)
print("Dimes ", dimes)
print("Nickels ", nickels)
print("Pennies ", pennies)


