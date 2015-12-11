from unittest import TestCase

from datetime import datetime, timedelta
from abcbank.transaction import Transaction, DEPOSIT, WITHDRAWL
from abcbank.account import Account, CHECKING, SAVINGS, MAXI_SAVINGS, ACCT_TYPE_NAME


class AccountTests(TestCase):
    
    def test_deposit(self):
        amount = 5.0
        a = Account(CHECKING)
        a.deposit(amount)
        self.assertGreaterEqual(amount, 0)
        self.assertIsInstance(a.transactions[0], Transaction, "correct type")
    
    def test_deposit_error(self):
        amount = -5.0
        a = Account(CHECKING)
        with self.assertRaisesRegexp(ValueError, r'deposit amount must be greater than zero'):
            a.deposit(amount)

    def test_withdraw(self):
        amount = 2.0
        a = Account(CHECKING)
        a.withdraw(amount)
        self.assertGreaterEqual(amount, 0)
        self.assertIsInstance(a.transactions[0], Transaction, "correct type")
    
    def test_withdraw_error(self):
        amount = -2.0
        a = Account(CHECKING)
        with self.assertRaisesRegexp(ValueError, r'withdraw amount must be greater than zero'):
            a.withdraw(amount)

    def test_interest_checking(self):
        amount = 200.00
        interest = amount * 0.001
        a = Account(CHECKING)
        a.deposit(amount)
        iy = a.interestEarned()
        self.assertEqual(iy, interest)

    def test_interest_savings_low(self):
        amount = 370.00
        interest = amount * 0.001
        a = Account(SAVINGS)
        a.deposit(amount)
        iy = a.interestEarned()
        self.assertEqual(iy, interest)

    def test_interest_savings_high(self):
        amount = 1250.00
        interest = (amount - 1000.0) * 0.002 + 1.0
        a = Account(SAVINGS)
        a.deposit(amount)
        iy = a.interestEarned()
        self.assertEqual(iy, interest)

    def test_interest_maxi_savings_low(self):
        amount = 370.00
        interest = amount * 0.02
        a = Account(MAXI_SAVINGS)
        a.deposit(amount)
        iy = a.interestEarned()
        self.assertEqual(iy, interest)

    def test_interest_maxi_savings_high(self):
        amount = 1250.00
        interest = (amount - 1000) * 0.05 + 20.0
        a = Account(MAXI_SAVINGS)
        a.deposit(amount)
        iy = a.interestEarned()
        self.assertEqual(iy, interest)

    def test_interest_maxi_savings_max(self):
        amount = 2350.00
        interest = (amount - 2000) * 0.1 + 70.0
        a = Account(MAXI_SAVINGS)
        a.deposit(amount)
        iy = a.interestEarned()
        self.assertEqual(iy, interest)

    def test_accountTypeText(self):
        for k,v in ACCT_TYPE_NAME.items():
            a = Account(k)
            self.assertEquals(a.accountTypeText(), v)

    def test_transactionHistory_age_ok(self):
        amount = 250.00
        a = Account(MAXI_SAVINGS)
        a.deposit(amount)
        a.transactions[0].transactionDate = datetime.now() - timedelta(days=0)
        result = a.transactionHistory(5)
        self.assertEquals(len(result), 1)

    def test_transactionHistory_age_older(self):
        amount = 250.00
        a = Account(MAXI_SAVINGS)
        a.deposit(amount)
        a.transactions[0].transactionDate = datetime.now() - timedelta(days=8)
        result = a.transactionHistory(5)
        self.assertEquals(len(result), 0)

    def test_transactionHistory_type_ok(self):
        amount = 250.00
        a = Account(MAXI_SAVINGS)
        a.deposit(amount)
        a.withdraw(amount)
        a.deposit(amount)
        result = a.transactionHistory(5, transType=DEPOSIT)
        self.assertEquals(len(result), 2)

