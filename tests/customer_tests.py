from unittest import TestCase, skip

from abcbank.account import Account, CHECKING, SAVINGS
from abcbank.customer import Customer

class AccountTests(TestCase):
    
    def test_statement(self):
        checkingAccount = Account(CHECKING)
        savingsAccount = Account(SAVINGS)
        henry = Customer("Henry").openAccount(checkingAccount).openAccount(savingsAccount)
        checkingAccount.deposit(100.0)
        savingsAccount.deposit(4000.0)
        savingsAccount.withdraw(200.0)
        self.assertEquals(henry.getStatement(),
                      "Statement for Henry" +
                      "\n\nChecking Account\n  deposit $100.00\nTotal $100.00" +
                      "\n\nSavings Account\n  deposit $4000.00\n  withdrawal $200.00\nTotal $3800.00" +
                      "\n\nTotal In All Accounts $3900.00")
    
    
    def test_oneAccount(self):
        oscar = Customer("Oscar").openAccount(Account(SAVINGS))
        self.assertEquals(oscar.numAccs(), 1)
    
    
    def test_twoAccounts(self):
        oscar = Customer("Oscar").openAccount(Account(SAVINGS))
        oscar.openAccount(Account(CHECKING))
        self.assertEquals(oscar.numAccs(), 2)
    
    
    @skip
    def test_threeAccounts(self):
        oscar = Customer("Oscar").openAccount(Account(SAVINGS))
        oscar.openAccount(Account(CHECKING))
        self.assertEquals(oscar.numAccs(), 3)

    def test_ownsAccount_True(self):
        oscar = Customer("Oscar").openAccount(Account(SAVINGS))
        checkingAcct = Account(CHECKING)
        oscar.openAccount(checkingAcct)
        self.assertTrue(oscar.ownsAccount(checkingAcct))

    def test_ownsAccount_False(self):
        oscar = Customer("Oscar").openAccount(Account(SAVINGS))
        oscar.openAccount(Account(CHECKING))
        checkingAcct = Account(CHECKING)
        self.assertFalse(oscar.ownsAccount(checkingAcct))

    def test_transfer(self):
        savingsAcct = Account(SAVINGS)
        checkingAcct = Account(CHECKING)
        oscar = Customer("Oscar").openAccount(savingsAcct)
        oscar.openAccount(checkingAcct)
        # Start with $500 in savings and $0 in checking.
        savingsAcct.deposit(500.00)
        self.assertTrue(oscar.ownsAccount(savingsAcct))
        self.assertTrue(oscar.ownsAccount(checkingAcct))
        # Transfer half of savings to checking to have $250 each.
        oscar.transfer(savingsAcct, checkingAcct, 250.00)
        self.assertEquals(savingsAcct.sumTransactions(), 250.0)
        self.assertEquals(checkingAcct.sumTransactions(), 250.0)

