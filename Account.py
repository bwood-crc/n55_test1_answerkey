from abc import ABC, abstractmethod
from decimal import Decimal


class Account(ABC):
    last_id = 0

    @staticmethod
    def get_next_id():
        Account.last_id += 1
        return Account.last_id

    def __init__(self, name: str):
        self.balance = Decimal(0)
        self.fees = Decimal(0)
        self.name = name
        self.account_number = Account.get_next_id()

    @abstractmethod
    def withdraw(self, amount: Decimal):
        self.balance -= amount

    @abstractmethod
    def deposit(self, amount: Decimal):
        self.balance += amount

    def __str__(self):
        return (f"Account Number: {self.account_number}, name: {self.name}, balance: ${self.balance:.2f}, "
                f"current fees: ${self.fees:.2f}.")
