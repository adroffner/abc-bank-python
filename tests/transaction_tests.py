from unittest import TestCase

from abcbank.transaction import Transaction

class TransactionTests(TestCase):
    
    def test_type(self):
        t = Transaction(5)
        self.assertIsInstance(t, Transaction, "correct type")
