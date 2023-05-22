class BankAccount:
    def __init__(self, name, acc_type, balance):
        self.name = name
        self.acc_type = 'Current' if acc_type == 0 else 'Saving'
        self._balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} deposited successfully!")
            print(f"Your balance: {self._balance}\n")
        else:
            raise ValueError(f"Error: Invalid amount, try again! [Amount:{amount}]")

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError(f"Error: Insufficient balance! [Requested amount: {amount}, Available balance: {self._balance}]")
        else:
            self._balance -= amount
            print(f"{amount} withdrawn successfully!")
            print(f"Your balance: {self._balance}\n")

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, bal):
        if bal >= 1000:
            self._balance = bal
        else:
            raise ValueError(f"Error: Minimum balance must be 1000")

    def show_details(self):
        print(f"{self.name}'s Account Details:")
        print(f"Account Name: {self.name}")
        print(f"Account Type: {self.acc_type}")
        print(f"Account Balance: {self.balance}\n") 

acc = BankAccount("John", 1, 1000)

while True:
    print("<1> ACCOUNT DETAILS")
    print("<2> DEPOSIT")
    print("<3> WITHDRAW\n")

    choice = int(input("Enter Option: "))

    if choice == 1: 
        acc.show_details()
    elif choice == 2:
        amt = int(input("Enter Amount: "))
        acc.deposit(amt)
    elif choice == 3:
        amt = int(input("Enter Amount: "))
        acc.withdraw(amt)
