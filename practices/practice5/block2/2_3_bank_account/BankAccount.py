class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"{amount} средств успешно зачислены на счет {self.account_number}"

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError('Недостаточно средств.')
        self.balance -= amount
        return f"{amount} средств успешно сняты с счета {self.account_number}"

    def check_balance(self):
        return f"Баланс счета {self.account_number}: {self.balance}"
