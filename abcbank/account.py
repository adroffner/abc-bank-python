from abcbank.transaction import Transaction

CHECKING = 0
SAVINGS = 1
MAXI_SAVINGS = 2


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
            if (amount <= 1000):
                return amount * 0.02
            elif (amount <= 2000):
                return 20 + (amount - 1000) * 0.05
            else:
                return 70 + (amount - 2000) * 0.1
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

        if self.accountType == CHECKING:
            accountType = "Checking Account"
        if self.accountType == SAVINGS:
            accountType = "Savings Account"
        if self.accountType == MAXI_SAVINGS:
            accountType = "Maxi Savings Account"

        return accountType

