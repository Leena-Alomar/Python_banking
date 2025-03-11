import unittest
from banking import Customer,User_login,Withdraw,Deposit,Transfer

class CustomerTest(unittest.TestCase):
    def __init__(self):

    def test_display_msg(self):
   

    def test_new_customer(self):
       

    def test_new_acc_type(self,account_id):
     
def test_read_csv():
 
def test_add_new_row(random_id, type_acct, first_name, last_name, password):
    


class Test_User_login(unittest.TestCase):
    def __init__(self):
        super().__init__()
     

    def test_login(self):
        

    def test_services_user_list(self):
      

class Test_Withdraw(unittest.TestCase):
    def __init__(self):
     
    def test_user_withdraw(self, account_id): 
 
      
            

class Test_Deposit(unittest.TestCase):
    def __init__(self):
          
    def test_user_deposit(self, account_id): 
      

class Test_Transfer(unittest.TestCase):
    def __init__(self):
 

    def test_user_Transfer(self, account_id): 
          
if __name__ == '__main__':
    unittest.main()





