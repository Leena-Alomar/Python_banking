        
class UserError(Exception):
    pass

def init():
    curr_customer = Customer("new name")
    curr_customer.new_customer()

init()

def init():

  Banking.start_session()

init()

            fix the new custome and make a method account type to call in the transfer ,fix the csv,check if the id is uniqe if not ass user if they want to creat new acc if yes then entre pass
    def store_data(self,store_id,first_name,last_name,store_pass,store_first,store_last):
        store_id = user_id.inputs["data_store"]
        store_pass = user_pass.inputs["data_store"]
        store_first= first_name.inputs["data_store"]
        store_last= last_name.input["data_store"]
        data_store.set_ttl("temporaryToken", ttl=None)





  class user_login(customer):
     def __init__(self,account_type,user_login,login_id,login_pass,want_rest,want_creat_account,services_list,customer_login,store_id,store_pass,store_first,store_last,first_name,last_name,savings_amount,checking_amount,both_amount):
        super().__init__(account_type,login_id,user_login)
        self.login_id=login_id
        self.login_pass =login_pass
        self.want_rest =want_rest
        self.want_creat_account=want_creat_account
        self.customer_login=customer
     def login(self):
        login_id = input("now please  entre your id: ") 
        login_pass = input("now please  entre your password: ")
        if login_id == self.store_id:
            if login_pass == self.store_pass:
                services_list = input("You Successfully Login now what kind of services would you like?:1-Withdraw 2-Deposit 3-Transfer:")
            else:
                want_rest = input("did you forget your password? would you like to reset it? y/n:") 
                while (want_rest == "y" or want_rest == "Y" ):
                    new_password = input("Please Enter Your New Password:")
                    self.store_pass = new_pass
                    break
        else:
            want_creat_account = input("There is no account with the same email address, would you like to creat new account? y/n :") 
            while (want_creat_account == "y" or "Y"):
                self.customer_login.new_customer()
                break
        
     def reset_pass(self):
        new_pass = input("please entre your new password ") 
        self.store_pass = new_pass
        print("reset successfully") 

class withdraw(customer,user_login):
     def __init__(self,account_type,user_id,user_login,services_list,withdraw_amount,money_amount,store_pass,store_first,store_last,first_name,last_name,savings_amount,checking_amount,both_amount):
            super().__init__(account_type,user_id,user_login,services_list,withdraw_amount,money_amount)
            self.withdraw_amount=withdraw_amount
     def account_withdraw(self):
       if services_list == "1":
         withdraw_amount = input(f'please Entre the amount of money you wolud like to withdraw :')
         if withdraw_amount > self.money_amount:
            print("Your current amount of money is less than the withdraw amount")
         else:
            self.money_amount -= withdraw_amount
            print(f'Your current amount of money is: {money_amount}')
        
  
    
class user_login(customer):
     def __init__(self,account_type,user_login,login_id,login_pass,want_rest,want_creat_account,services_list,customer_login,store_id,store_pass,store_first,store_last,first_name,last_name,savings_amount,checking_amount,both_amount):
        super().__init__(account_type,login_id,user_login)
        self.login_id=login_id
        self.login_pass =login_pass
        self.want_rest =want_rest
        self.want_creat_account=want_creat_account
        self.customer_login=customer
     def login(self):
        login_id = input("now please  entre your id: ") 
        login_pass = input("now please  entre your password: ")
        if login_id == self.store_id:
            if login_pass == self.store_pass:
                services_list = input("You Successfully Login now what kind of services would you like?:1-Withdraw 2-Deposit 3-Transfer:")
            else:
                want_rest = input("did you forget your password? would you like to reset it? y/n:") 
                while (want_rest == "y" or want_rest == "Y" ):
                    new_password = input("Please Enter Your New Password:")
                    self.store_pass = new_pass
                    break
        else:
            want_creat_account = input("There is no account with the same email address, would you like to creat new account? y/n :") 
            while (want_creat_account == "y" or "Y"):
                self.customer_login.new_customer()
                break
        
     def reset_pass(self):
        new_pass = input("please entre your new password ") 
        self.store_pass = new_pass
        print("reset successfully") 

class withdraw(customer,user_login):
     def __init__(self,account_type,user_id,user_login,services_list,withdraw_amount,money_amount,store_pass,store_first,store_last,first_name,last_name,savings_amount,checking_amount,both_amount):
            super().__init__(account_type,user_id,user_login,services_list,withdraw_amount,money_amount)
            self.withdraw_amount=withdraw_amount
     def account_withdraw(self):
       if services_list == "1":
         withdraw_amount = input(f'please Entre the amount of money you wolud like to withdraw :')
         if withdraw_amount > self.money_amount:
            print("Your current amount of money is less than the withdraw amount")
         else:
            self.money_amount -= withdraw_amount
            print(f'Your current amount of money is: {money_amount}')
        


class Deposit(customer,user_login):
     def __init__(self):
        super().__init__(self,account_type,user_id,user_login,services_list,money_amount,money_input,savings_amount,checking_amount,both_amount,deposit_type)
        self.money_input=money_input
        self.deposit_type =deposit_type
     def deposit_money(self,account_type,user_id,user_login,services_list,money_input,savings_amount,checking_amount,both_amount,deposit_type):
        if services_list =="2":
            money_input = input("How much would you like to add?:") 
            deposit_type = input( "what type of account would you like to deposit? (1-checking account 2-saving account 3-both): ")
            if deposit_type == "1":
                savings_amount += money_input
                print (f'Your current amount of money is: {savings_amount}')
            elif deposit_type == "2":
                checking_amount += money_input
                print (f'Your current amount of money is: {checking_amount}') 
            elif deposit_type == "3":
                both_amount -= money_input
                print(f'Your current amount of money is: {both_amount}')
      
class Transfer(customer,user_login):
     def __init__(self,account_type,user_id,user_login,services_list,account_wanted,transfer_amount,transfer_acoount):
        super().__init__(account_type,user_id,user_login,services_list,transfer_acoount)
        self.account_wanted=account_wanted
        self.transfer_amount=transfer_amount
        self.transfer_acoount=transfer_acoount
        self.transfer_to_type =transfer_to_type 
     def transfer_money(self):
        try:
            if services_list =="3":
                account_wanted = input("please entre account id:")
                if account_wanted == user_id:
                    transfer_acoount = input("what type of account would you like to transfer from? (1-checking account 2-saving account 3-both): ")
                    if transfer_account == "1":
                        savings_amount -= money_input
                        print (f'Your current amount of money is: {savings_amount}')
                    elif deposit_type == "2":
                        checking_amount -= money_input
                        print (f'Your current amount of money is: {checking_amount}') 
                    elif deposit_type == "3":
                        both_amount -= money_input
                        print(f'Your current amount of money is: {botth_amount}')
                    transfer_to_type = input("please entre type of account you would like to tranfer to:")
                    if transfer_to_type  == "1":
                        savings_amount += money_input
                        print (f'Your current amount of money has been transferd')
                    elif transfer_to_type  == "2":
                        checking_amount += money_input
                        print (f'Your current amount of moneyhas been transferd') 
                    elif transfer_to_type  == "3":
                        both_amount += money_input
                        print(f'Your current amount of money has been transferd')
                  
                else:
                    raise UserError("please entre a valid account number")
        except ValueError: 
            raise UserError('please enter valid number') 

class overdraft(Customer,user_login):
     def __init__(self,account_type,user_id,user_login,services_list,overdraft,count,money):
      super().__init__(account_type,user_id,user_login,services_list)
      self.overdraft=overdraft

     def overdraft_money(self):
        count =0
        if money_amount < 0 :
             overdraft = money_amount -35 
             count += 1
             print("You are chared with fee of 35$")
             for c in count:
                if c>2:
                    print("Your account have been deactivate") 
                    if self.money_amount == 0:
                        print("Your account have been activated") 

class Bouns():
     def __init__():
        super().__init__()



c = Customer(111111, "password123", 111111, "storepassword", "Leena", "Mansour", 1000, 2000, 3000)
print("User ID:", c.user_id)  # Output: 111111
print("First Name:", c.first_name)  # Output: Leena
print("Last Name:", c.last_name)  # Output: Mansour
user1 = UserLogin("checking", 111111, "password123", 111111, "storepassword")
user1.login() 





c = Customer(111111, "password123", 111111, "storepassword", "Leena", "Mansour", 1000, 2000, 3000)
print("User ID:", c.user_id)  # Output: 111111
print("First Name:", c.first_name)  # Output: Leena
print("Last Name:", c.last_name)  # Output: Mansour
user1 = UserLogin("checking", 111111, "password123", 111111, "storepassword")
user1.login() 



   # def user_deposit(self, account_id): 
    #     customers_list = read_csv()
    #     try: 
    #         account_type = input("What Type of Account Would You Like to Deposit To? : 1-Checking 2-Savings :")
            
    #         for i in customers_list:
    #             if account_type == "1":
    #                 if i['account_id'] == account_id and i['checking'] != "":
    #                     money_input = input("Please Enter The Amount of Money You Would Like To Deposit :")
    #                     i['checking'] = int(i['checking']) + int(money_input)
    #                     print("Your Checking Account Has Been Updated , This is Your Current Balance :")
    #                     print(i['checking'])       
    #                     break
    #             elif account_type == "2":
    #                 if i['account_id'] == account_id and i['savings'] != "":
    #                     money_input = input("Please Enter The Amount of Money You Would Like To Deposit :")
    #                     i['savings'] =  int(i['savings']) + int(money_input)


"""

    - **BONUS**
      - Display Transaction Data (You need to create another file to store the transaction history, required login)
      list .push()
      dir list

      - index all transactions for a customer account

      - show one transaction **details**
      - show historical data of transactions (date and time of transaction, type of transaction, resulting balance, etc.)



"""



 # transfer_from = input("What Type of Account Would You Like to Transfer To? : 1-Checking 2-Savings :")
            
            # for s in lists:
            #     if transfer_from == "1":
            #         if s['account_id'] == account_id and s['checking'] != "":
            #             transfer_input = input("Please Enter The Amount of Money You Would Like To Transfer :")
            #             s['checking'] = int(s['checking']) - int(transfer_input)
            #             transfer_to = input("What Type of Account Would You Like to Transfer To? : 1-Checking 2-Savings :")
            #             if transfer_to =="1"
            #                 if s['account_id'] == account_id and s['checking'] != "":
            #                     s['checking'] = int(s['checking']) + int(tranfer_input)
            #                     print("The Amount of Money is Transferd")
            #             elif transfer_from == "2":
            #                 if s['account_id'] == account_id and s['savings'] != "":
            #                     s['savings'] =  int(s['savings']) + int(tranfer_input)
            #                     print("The Amount of Money is Transferd")
            #             else:
            #                 print("Please Entre a Valid Input")
                                
                                
                                
            #             break
            #     elif transfer_from == "2":
            #         if s['account_id'] == account_id and s['savings'] != "":
            #             tranfer_input = input("Please Enter The Amount of Money You Would Like To Transfer :")
            #             s['savings'] =  int(s['savings']) - int(tranfer_input)
            #                  transfer_to = input("What Type of Account Would You Like to Transfer To? : 1-Checking 2-Savings :")
            #             if transfer_to =="1"
            #                 if s['account_id'] == account_id and s['checking'] != "":
            #                     s['checking'] = int(s['checking']) + int(tranfer_input)
            #                     print("The Amount of Money is Transferd")
            #             elif transfer_from == "2":
            #                 if s['account_id'] == account_id and s['savings'] != "":
            #                     s['savings'] =  int(s['savings']) + int(tranfer_input)
            #                     print("The Amount of Money is Transferd")
            #             else:
            #                 print("Please Entre a Valid Input")
            #     else:
            #         print("Please Entre a Valid Input")





"""

user after login they have amount of money in the acc then the user can send the reqiured amount of money to the account 
they want ,first i will check if the amount of money is out of budget or not then i will check type of account they want
to send the money to then send the money after and decrease that amount of money from the account and increase it to the 
other 

user can add money in both of the two account and increase the amount of money evey time they do


user maybe have more than 1 accout if he want to transfer money from one acc to another then he first need to login then
he need to choose the account he want to transfer to (i might add smth like each user have diff transfer num and when user 
want to transfer money it will appear in thier account ... maybe something like acc num [amount].push ????? 
also i need each user to have uniqe acc num )

"""