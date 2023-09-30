from Account import *


class SavingsAccount(Account):

    def __init__(self, name: str):
        super().__init__(name)

    def withdraw(self, amount: Decimal):
        self.fees += Decimal(1.00)
        super().withdraw(amount)

    def deposit(self, amount: Decimal):
        super().deposit(amount)
