from unittest import TestCase, skip

from abcbank.account import Account, CHECKING, SAVINGS
from abcbank.customer import Customer

class StatementTests(TestCase):
    
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
