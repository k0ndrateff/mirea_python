import pytest
from BankAccount import BankAccount


def test_initial_balance():
    account = BankAccount(1)
    assert account.balance == 0


def test_deposit():
    account = BankAccount(2)
    account.deposit(100)
    assert account.balance == 100


def test_withdraw_sufficient_funds():
    account = BankAccount(3)
    account.deposit(100)
    account.withdraw(50)
    assert account.balance == 50


def test_withdraw_insufficient_funds():
    account = BankAccount(4)
    account.deposit(100)
    with pytest.raises(ValueError):
        account.withdraw(200)


def test_check_balance():
    account = BankAccount(5)
    account.deposit(10000)
    assert account.check_balance() == "Баланс счета 5: 10000"


# coverage run -m pytest test_bank_account.py
# coverage report -m
# coverage report -m --include=BankAccount.py
# coverage html
