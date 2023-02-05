class Bank_account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        print("Pleas, enter the sum you want to put in deposit:")
        money = float(input())
        self.balance += money
        return Bank_account(self.owner, self.balance)

    def withdraw(self):
        print("Please, enter the sum you want to take:")
        taken = float(input())
        while taken > self.balance:
            print("Please, enter the sum you want to take:")
            taken = float(input())
        self.balance -= taken
        return Bank_account(self.owner, self.balance)

    def __str__(self):
        return f"{self.owner} have {self.balance} money in his deposit."


account = Bank_account(input(), float(input()))
account = Bank_account.deposit(account)
account = Bank_account.withdraw(account)
print(account)
