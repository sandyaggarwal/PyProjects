import random
from InsufficientBalanceError import InsufficientBalanceError

class Account:
    def __init__(self, account_name: str, initial_balance: float):
        self.account_number = random.randint(100000, 999999)
        self.account_name: str = account_name
        self.balance: float = initial_balance
 
    def get_balance(self):
        print(f"Balance for the A/C {self.account_name} is {self.balance:.2f}")
        return f"{self.balance:.2f}"

    def deposit(self, amount: float) -> float:
        self.balance += amount
        print(f"\nRs{amount} credited to A/C {self.account_number}")
        return self.get_balance()
    
    def is_valid_balance(self, amount: float):
        if self.balance < amount:
            raise InsufficientBalanceError
        else:
            return True
        
    def withdraw(self, amount: float):
        try:
            if self.is_valid_balance(amount):
                self.balance -= amount
                print(f"\n {amount} Rs amount withdrawn")
                return self.get_balance()
        except InsufficientBalanceError:
            print(f"\nLow Balance!!! {self.get_balance()}"
                  f"\nRs{amount} can't be withdrawn")
        
    def __str__(self):
        return f"\n ********Account Details******** \nName: {self.account_name}\nAcctNumber:"\
               f"{self.account_number} \nBalance: {self.balance:.2f}"
