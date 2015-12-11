from datetime import datetime


class Transaction(object):
    ''' A single Transaction on an account.

    This expects the real numeric amount in USD.
    A deposit is positive.
    A withdrawl is negative.
    '''

    def __init__(self, amount):
        ''' Create a new transaction for the amount.

        :param float amount: amount deposited or withdrawn in USD
        '''
        self.amount = amount
        self.transactionDate = datetime.now()

    def eventText(self):
        ''' Transaction event text describes what happened.

        :returns: event description string
        '''
        if self.amount < 0:
            return "withdrawal"
        elif self.amount > 0:
            return "deposit"
        else:
            return "N/A"


