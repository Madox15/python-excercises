from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value) -> None:
        if value < 0:
            raise ValueError("Balance has to be positive")
        self._balance = value

    def deposit(self, value) -> None:
        if value <= 0:
            raise ValueError("Deposit has to be positive")
        self.balance += value

    def withdraw(self, value) -> bool:
        if value <= 0:
            raise ValueError("Withdraw has to be positive")
        if value > self.balance:
            return False
        self.balance -= value
        return True

    @abstractmethod
    def monthly_fee(self):
        pass

    def apply_monthly_fee(self):
        return self.withdraw(self.monthly_fee())

    def __str__(self):
        return f"{self.owner}: {self.balance:.2f} PLN"


class CheckingAccount(Account):

    def monthly_fee(self):
        if self.balance >= 1000:
            return 0
        else:
            return 10


if __name__ == "__main__":
    acc = CheckingAccount("Anna", 500)
    print(acc)  # Anna: 500.00 PLN
    acc.deposit(600)
    print(acc.monthly_fee())  # 0
    print(acc.apply_monthly_fee())  # True
    acc.withdraw(700)
    print(acc.monthly_fee())  # 10
    print(acc.apply_monthly_fee())  # True
    print(acc)  # Anna: 390.00 PLN
    print(acc.withdraw(1000))  # False
    print(acc.balance)  # 390

    try:
        acc.balance = -5
    except ValueError:
        print("OK")  # OK

    try:
        Account("x", 1)
    except TypeError:
        print("abstract OK")  # abstract OK
