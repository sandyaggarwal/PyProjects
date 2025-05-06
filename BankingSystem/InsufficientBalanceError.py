class InsufficientBalanceError(Exception):
    def __init__(self):
        super().__init__("Account have low balance!")
        