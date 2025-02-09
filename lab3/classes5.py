#Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
#class Account:
#    pass

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = int(balance)

    def deposit(self, sum):
        self.balance = self.balance + sum
        print("Current balance:", self.balance)

    def withdraw(self, sum):
        if self.balance < sum:
            print("Insufficient funds")
        else:
            self.balance = self.balance - sum
        
        print("Current balance:", self.balance)


ownerName = input("Enter an owner name: ")
initialBalance = input("Enter an initial balance: ")

account1 = Account(ownerName, initialBalance)
command = input("Enter command deposit/withdraw: ")
if command == "deposit":
    sum = int((input("Enter the sum: ")))
    account1.deposit(sum)
elif command == "withdraw":
    sum = int((input("Enter the sum: ")))
    account1.withdraw(sum)
else:
    print("Incorrect request, try again.")