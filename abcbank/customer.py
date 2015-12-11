from abcbank.account import CHECKING, SAVINGS, MAXI_SAVINGS


class Customer(object):
    ''' A Customer of the bank.
    '''

    def __init__(self, name):
        ''' Create a new customer who has one or more accounts.
        '''
        self.name = name
        self.accounts = []

    def __str__(self):
        return "{} ({} account{})".format(self.name, self.numAccs(),
            ('s' if self.numAccs() != 1 else ''))

    def openAccount(self, account):
        ''' Open a new account for this customer.
        The method returns this object rather than NoneType, like sorted() vs. sort().

        :param account: a new Account object
        :returns: this Customer object
        '''
        self.accounts.append(account)
        return self

    def numAccs(self):
        ''' Show the number of accounts this customer has.

        :returns: number of accounts
        :rtype: int
        '''
        return len(self.accounts)

    def totalInterestEarned(self):
        ''' Compute the total interest earned by this customer across all accounts.

        :returns: total interest in USD
        :rtype: float
        '''
        return sum([a.interestEarned() for a in self.accounts])

    def getStatement(self):
        ''' Get a bank statement for this customer.

        :returns: a bank statement string
        '''
        # DELETE: These lines do nothing and 1988 is before Python ever existed!
        # JIRA-123 Change by Joe Bloggs 29/7/1988 start
        ## statement = None  # reset statement to null here
        # JIRA-123 Change by Joe Bloggs 29/7/1988 end

        totalAcrossAllAccounts = sum([a.sumTransactions() for a in self.accounts])
        accountStatements = [ self.statementForAccount(account) for account in self.accounts ]

        statement = ("Statement for {}".format(self.name) + ''.join(accountStatements)
            + "\n\nTotal In All Accounts " + _toDollars(totalAcrossAllAccounts))
        return statement

    def statementForAccount(self, account):
        ''' Prepare a statement for a single account belonging to this customer.

        :param Account account: pass the Account object
        :returns: a statement string for the account
        '''
        transactionSummary = [t.eventText() + " " + _toDollars(abs(t.amount))
                              for t in account.transactions]
        transactionSummary = "  " + "\n  ".join(transactionSummary) + "\n"
        totalSummary = "Total " + _toDollars(sum([t.amount for t in account.transactions]))
        return "\n\n{}\n".format(account.accountTypeText()) + transactionSummary + totalSummary

    def ownsAccount(self, account):
        '''Does this customer own the `account`?

        :parameter Account account: the account to check
        :returns:  True when this Customer owns the Account
        '''
        # Use the "is" operator to match the exact Account object.
        # TODO: Replace this with a clear Account.id
        return any([ account is v for v in self.accounts ])

    def transfer(self, fromAccount, toAccount, amount):
        ''' Transfer money from one account to another belonging to this customer.
        The `amount` should be a postive value in USD.

        :param fromAccount: transfer from this Account
        :param toAccount: transfer to this Account
        :param float amount: transfer this amount in USD
        '''
        if not (self.ownsAccount(fromAccount) and self.ownsAccount(toAccount)):
            raise ValueError("Customer cannot transfer between those accounts")

        fromAccount.withdraw(amount)
        toAccount.deposit(amount)


def _toDollars(number):
    ''' Format an amount in USD to a printed USD string, e.g. 12.01 to "$12.01".

    :param float number: amount in USD
    :returns: a USD string to print
    '''
    return "${:1.2f}".format(number)
