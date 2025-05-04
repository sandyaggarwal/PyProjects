import random
from datetime import datetime


class Account:
    def __init__(self):
        self.account_number = random.randint(100000, 999999)
        # self.account_owner
        self.balance: float = self.balance
        self.creation_date = datetime.now()

    def deposit():
        ...

    def withdraw():
        ...

    def get_balance():
        ...

    def get_transaction_history():
        ...