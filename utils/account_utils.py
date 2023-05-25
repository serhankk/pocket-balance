#!/usr/bin/env python3

class Account:
    def __init__(self, account_name: str) -> None:
        self.account_name = account_name
        self.password = str(123)
        self.balance = 0.0

    def get_balance(self) -> float:
        return self.balance

    def set_balance(self, amount: float) -> float:
        self.balance += amount
        return self.balance
    
    def create_spending(self, name: str, category: str, amount: float) -> dict:
        data = {"name": name,
                "category": category,
                "amount": amount}
        self.set_balance(-abs(amount))
        return data
    
    def create_incoming(self, name: str, category: str, amount: float) -> dict:
        data = {"name": name,
                "category": category,
                "amount": amount}
        self.set_balance(abs(amount))
        return data

    


my_acc = Account("Foo")
balance = my_acc.get_balance()
print(balance)

my_acc.set_balance(500)
balance = my_acc.get_balance()
print(balance)

"""
my_acc.create_spending("smart robot", "home", -1000)
balance = my_acc.get_balance()
print(balance)

my_acc.create_incoming("rent", "passive", 7500)
balance = my_acc.get_balance()
print(balance)
"""