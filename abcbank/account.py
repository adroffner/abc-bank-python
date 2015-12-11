from datetime import datetime, timedelta
from abcbank.transaction import Transaction, DEPOSIT, WITHDRAWL

CHECKING = 0
SAVINGS = 1
MAXI_SAVINGS = 2

ACCT_TYPE_NAME = {
    CHECKING: "Checking Account",
    SAVINGS: "Savings Account",
    MAXI_SAVINGS: "Maxi Savings Account",
}

class Account(object):
    ''' An Account belongs to a Customer.
    '''

    def __init__(self, accountType):
        '''Create an Account.

        :param int accountType: an account type, e.g. account.CHECKING
        '''
        self.accountType = accountType
        self.transactions = []

    def deposit(self, amount):
        ''' Deposit `amount` dollars into this account.
         The `amount` is a positive dollar value taken from the customer.

        :param float amount: deposit amount in USD
        '''
        if (amount <= 0):
            raise ValueError("deposit amount must be greater than zero")
        else:
            self.transactions.append(Transaction(amount))

    def withdraw(self, amount):
        ''' Withdraw `amount` dollars from this account.
         The `amount` is a positive dollar value given to the customer.

        :param float amount: withdraw amount in USD
        '''
        if (amount <= 0):
            raise ValueError("withdraw amount must be greater than zero")
        else:
            self.transactions.append(Transaction(-amount))

    def interestEarned(self):
        ''' Calculate the interest earned on all transactions.
        This computes interest on all deposits and withdrawls during the period.

        :returns: interest earned in USD
        '''
        amount = self.sumTransactions()
        if self.accountType == SAVINGS:
            if (amount <= 1000):
                return amount * 0.001
            else:
                return 1 + (amount - 1000) * 0.002
        elif self.accountType == MAXI_SAVINGS:
            # NOTE: This was the former maxi-savings plan
            """
            if (amount <= 1000):
                return amount * 0.02
            elif (amount <= 2000):
                return 20 + (amount - 1000) * 0.05
            else:
                return 70 + (amount - 2000) * 0.1
            """
            # Give a lower rate when withdrawls were made in the last 10 days.
            if self.transactionHistory(10, transType=WITHDRAWL):
                return amount * 0.001
            else:
                return amount * 0.05
        elif self.accountType == CHECKING:
            return amount * 0.001
        else:
            raise ValueError("account has an invalid account type")

    def sumTransactions(self, checkAllTransactions=True):
        ''' Computes all deposits and withdrawls during the period.

        :returns: current monies without interest in USD
        '''
        return sum([t.amount for t in self.transactions])

    def accountTypeText(self):
        ''' Give an account type description text.

        :returns: a string for the account type name
        '''
        accountType = ""
        if self.accountType in ACCT_TYPE_NAME:
            accountType = ACCT_TYPE_NAME[self.accountType]
        return accountType

    def transactionHistory(self, daysOld, transType=None):
        ''' Account Transaction history.

        :param int daysOld: find transaction that are no more than N days old
        :param transType: a Transaction type code, e.g. transaction.DEPOSIT
        '''
        transList = []
        # Filter out older older transactions.
        now = datetime.now()
        transList = [ v for v in self.transactions if (now - v.transactionDate) <= timedelta(days=daysOld) ]
        # Filter out transaction of the right type.
        if transType:
            transList = [ v for v in self.transactions if v.eventType() == transType ]
        return transList

