from unittest import TestCase

from abcbank.transaction import Transaction
from abcbank.account import Account, CHECKING, SAVINGS, MAXI_SAVINGS


class AccountTests(TestCase):
    
    def test_deposit(self):
        amount = 5
        a = Account(CHECKING)
        a.deposit(amount)
        self.assertGreaterEqual(amount, 0)
        self.assertIsInstance(a.transactions[0], Transaction, "correct type")
    
    def test_deposit_error(self):
        amount = -5
        a = Account(CHECKING)
        with self.assertRaisesRegexp(ValueError, r'deposit amount must be greater than zero'):
            a.deposit(amount)

    def test_withdraw(self):
        amount = 2
        a = Account(CHECKING)
        a.withdraw(amount)
        self.assertLessEqual(amount, 0)
        self.assertIsInstance(a.transactions[0], Transaction, "correct type")
    
    def test_withdraw_error(self):
        amount = -2
        a = Account(CHECKING)
        with self.assertRaisesRegexp(ValueError, r'withdraw amount must be greater than zero'):
            a.withdraw(amount)

