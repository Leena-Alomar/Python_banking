import unittest
from banking import customer, 

class TestCustomer(unittest.TestCase):
     def test_new_customer(self):
        c=customer()
        result = c.new_customer("" )
        self.assertEqual(result)

     def test_store_data(self):
        c=customer()
        result = c.store_data("" )
        self.assertEqual(result)

      def test_login(self):
        c=customer()
        result = c.login("" )
        self.assertEqual(result)
    
     def test_reset_pass(self):
        c=customer()
        result = c.reset_pass("" )
        self.assertEqual(result)

     def test_account_withdraw(self):
        c=customer()
        result = c.account_withdraw("" )
        self.assertEqual(result)

    
     def test_deposit_money(self):
        c=customer()
        result = c.deposit_money("" )
        self.assertEqual(result)

    
     def test_transfer_money(self):
        c=customer()
        result = c.transfer_money("" )
        self.assertEqual(result)
    
     def test_overdraft_money(self):
        c=customer()
        result = c.overdraft_money("" )
        self.assertEqual(result)
    
    

if __name__ == '__main__':
    unittest.main()





