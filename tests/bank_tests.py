from unittest import TestCase

from abcbank.account import Account, CHECKING, MAXI_SAVINGS, SAVINGS
from abcbank.bank import Bank
from abcbank.customer import Customer

class BankTests(TestCase):

    def test_customer_summary(self):
        bank = Bank()
        john = Customer("John").openAccount(Account(CHECKING))
        bank.addCustomer(john)
        self.assertEquals(bank.customerSummary(),
                      "Customer Summary\n - John (1 account)")
    
    
    def test_checking_account(self):
        bank = Bank()
        checkingAccount = Account(CHECKING)
        bill = Customer("Bill").openAccount(checkingAccount)
        bank.addCustomer(bill)
        checkingAccount.deposit(100.0)
        self.assertEquals(bank.totalInterestPaid(), 0.1)
    
    
    def test_savings_account(self):
        bank = Bank()
        checkingAccount = Account(SAVINGS)
        bank.addCustomer(Customer("Bill").openAccount(checkingAccount))
        checkingAccount.deposit(1500.0)
        self.assertEquals(bank.totalInterestPaid(), 2.0)
    
    
    def test_maxi_savings_account(self):
        bank = Bank()
        checkingAccount = Account(MAXI_SAVINGS)
        bank.addCustomer(Customer("Bill").openAccount(checkingAccount))
        checkingAccount.deposit(3000.0)
        self.assertEquals(bank.totalInterestPaid(), 150.0)
