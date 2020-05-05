class User:
    def __init__(self, name, email):
        self.name= name
        self.email= email
        self.account=BankAccount(int_rate=0.02, balance=0)
    def make_withdrawal(self, amount):
        self.account.balance-=amount
        return self
    def make_deposit(self, amount):
        self.account.balance+=amount
        return self
    def display_user_balance(self):
        print(self.account.balance)
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

rich = User("Richard", "lee@gmail.com")
joe = User("Joe", "choe@gmail.com")
jesse = User("Jesse", "allen@gmail.com")
rich.make_deposit(100).make_deposit(50).make_deposit(25)
rich.make_withdrawal(125)
rich.display_user_balance()
joe.make_deposit(200).make_deposit(400)
joe.make_withdrawal(100).make_withdrawal(200)
joe.display_user_balance()
jesse.make_deposit(500)
jesse.make_withdrawal(100).make_withdrawal(200).make_withdrawal(50)
jesse.display_user_balance()