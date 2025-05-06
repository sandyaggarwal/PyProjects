import random


class Account:
    def __init__(self, account_name: str, initial_balance: float):
        self.account_number = random.randint(100000, 999999)
        self.account_name: str = account_name
        self.balance: float = initial_balance
 
    def get_balance(self):
        return f"{self.balance:.2f}"

    def deposit(self, amount: float) -> float:
        self.balance += amount
        print(f"\n{amount} Rs credited to A/C {self.account_number}")
        return self.get_balance()
        
    def __str__(self):
        return f"\n ********Account Details******** \nName: {self.account_name}\nAcctNumber:"\
               f"{self.account_number} \nBalance: {self.balance:.2f}"
