import deal


@deal.inv(lambda account: account.balance >= 0)
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    @deal.pre(lambda amount: amount > 0)
    @deal.has('stdout')
    def deposit(self, amount):
        self.balance += amount
        return f"{amount} средств успешно зачислены на счет {self.account_number}"

    @deal.raises(ValueError)
    @deal.pre(lambda amount: amount > 0)
    @deal.has('stdout')
    def withdraw(self, amount):
        if amount < self.balance:
            raise ValueError('Недостаточно средств')

        self.balance -= amount
        return f"{amount} средств успешно сняты с счета {self.account_number}"

    @deal.has('stdout')
    def check_balance(self):
        return f"Баланс счета {self.account_number}: {self.balance}"
