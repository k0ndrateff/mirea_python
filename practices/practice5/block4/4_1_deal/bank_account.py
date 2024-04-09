import deal


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    @deal.pre(lambda amount: amount > 0)
    def deposit(self, amount):
        self.balance += amount
        return f"{amount} средств успешно зачислены на счет {self.account_number}"

    @deal.raises(ValueError)
    def withdraw(self, amount):
        if amount < self.balance:
            raise ValueError('Недостаточно средств')

        self.balance -= amount
        return f"{amount} средств успешно сняты с счета {self.account_number}"

    @deal.post(lambda x: x >= 0)
    def get_balance(self):
        return self.balance

    @deal.has('stdout')
    def check_balance(self):
        return f"Баланс счета {self.account_number}: {self.balance}"


if __name__ == '__main__':
    test_bank = deal.cases(BankAccount)
