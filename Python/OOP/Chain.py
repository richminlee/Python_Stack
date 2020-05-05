class User:
    def __init__(self, name, email):
        self.name= name
        self.email= email
        self.balance=0
    def make_withdrawal(self, amount):
        self.balance-=amount
        return self
    def make_deposit(self, amount):
        self.balance+=amount
        return self
    def display_user_balance(self):
        print(self.balance)

rich = User("Richard", "lee@gmail.com")
joe = User("Joe", "choe@gmail.com")
jesse = User("Jesse", "allen@gmail.com")
rich.make_deposit(100).make_deposit(50).make_deposit(25).make_withdrawal(125).display_user_balance()
joe.make_deposit(200).make_deposit(400).make_withdrawal(100).make_withdrawal(200).display_user_balance()
jesse.make_deposit(500).make_withdrawal(100).make_withdrawal(200).make_withdrawal(50).display_user_balance()