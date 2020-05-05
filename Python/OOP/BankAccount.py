class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate= int_rate
        self.balance=0
    def withdraw(self, amount):
        self.balance-=amount
        if self.balance<0:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance-=5
        return self
    def deposit(self, amount):
        self.balance+=amount
        return self
    def display_account_info(self):
        print("Balance: ", self.balance)
        return self
    def yield_interest(self):
        self.balance+=(self.balance*self.int_rate)
        return self

# baller=BankAccount(.1, 1000)
# broke=BankAccount(.01, 3)
# baller.deposit(2000).deposit(5000).deposit(10000).withdraw(7000).yield_interest().display_account_info()
# broke.deposit(7).deposit(20).withdraw(1).withdraw(5).withdraw(20).withdraw(10).yield_interest().display_account_info()
