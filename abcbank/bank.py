class Bank(object):
    ''' A Bank branch has one or more Customers.
    '''

    def __init__(self):
        ''' Create a bank branch.
        '''
        self.customers = []

    def addCustomer(self, customer):
        ''' Add a new customer to the branch.

        :param Customer customer: add a new Customer object
        '''
        self.customers.append(customer)

    def customerSummary(self):
        ''' List a summary of customers who have accounts at this branch.

        :returns: a customer summary string
        '''
        summary = "Customer Summary\n - "
        return summary + "\n - ".join([ str(customer) for customer in self.customers ])

    def totalInterestPaid(self):
        ''' Calculate the total interest paid by the bank during this period.

        :returns: total interest in USD
        :rtype: float
        '''
        total = 0
        for c in self.customers:
            total += c.totalInterestEarned()
        return total

    # def getFirstCustomer(self): There is no use for this method, and it was buggy!
