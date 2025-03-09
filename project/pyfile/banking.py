import csv
from datetime import datetime
import csv
import os
# 1.1 Seed Data to CSV
customers_info = [
    { 'account_id': '10006', 'first_name': 'Yazeed', 'last_name': "Booth", 'password': "b8wf5" ,'checking': "", 'savings': ""},
    { 'account_id': '10007', 'first_name': 'Devlin', 'last_name': "Dawkins", 'password': "bdfghdf8wf5" ,'checking': "", 'savings': ""},
    { 'account_id': '10008', 'first_name': 'Kristina', 'last_name': "Da-Silva", 'password': "b8wdff5" ,'checking': "", 'savings': ""},
]

# 2.0 Set fieldnames once:
fieldnames = ["account_id", "first_name", "last_name" , "password" ,"checking" , "savings"]

# 3.0 Check CSV File Exists (otherwise error thrown!)
# 3.1 Set Headers in the CSVFile 
# 3.2 SEED DATA TO CSV
# 3.3 EXAMPLE: writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
# 3.4 "w" option will allow writing, but NOT appending...
if not os.path.exists("./banking.csv"):
    with open("./banking.csv", 'w', newline='') as csvfile:
        try:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in customers_info:
                writer.writerow(row)
        except csv.Error as e:
            print(e)

# 4.0 If Exists - ReadFile / Rows:
try: 
    with open("banking.csv", "r") as file:
        contents = csv.DictReader(file)
        for row in contents:
            print(row) #will print: {'Name': 'The First Doctor', 'Actor': 'William Hartnell', 'Number of Episodes': '134'}
            for prop in fieldnames:
                print(row[prop]) # will print the value of each individual property
except csv.Error as e:
    print(e)


# 5.0 Add Individual Row => "a+" option will allow reading and APPENDING to file
try:
    new_row = {'Name': 'The Sixth Doctor', 'Actor': 'Harrison Ford', 'Number of Episodes': 1 }
    with open("banking.csv", "a+") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(new_row)
except csv.Error as e:
    print(e)

class UserError(Exception):
    pass

class customer():
    def __init__(self,user_id,user_pass,store_id,store_pass,store_first,store_last,first_name,last_name,savings_amount,checking_amount,both_amount,checking_account,savings_account):
        self.user_id= user_id
        self.user_pass=user_pass
        self.store_id=store_id
        self.store_pass=store_pass
        self.first_name=first_name
        self.last_name=last_name
        self.savings_amount=savings_amount
        self.checking_amount=checking_amount
        self.both_amount=both_amount
        self.checking_account = checking_account
        self.savings_account=savings_account

    def new_customer():
        try:
            # new account information
            new_account_type = None
            new_account_first_name = None
            new_account_last_name = None
            new_account_pass = None

            type_responses = ["1", "2", "Q"]
            account_types = { "1": "Checking Account", "2": "Savings Account" }
            while new_account_type == None and account_type not in type_responses:
                new_account_type = input("welcome to our banking app what type of account would you like to creat? (1-checking account 2-saving account): ") 
            while new_account_first_name == None:
                new_account_first_name = input("Please enter your first name")
            while new_account_last_name == None:
                new_account_last_name = input("Please enter your last name")
            while new_account_pass == None:
                new_account_pass = input("Please enter a password")
            
        except Exception as e:
            print(e) 

            # fix the new custome and make a method account type to call in the transfer ,fix the csv,check if the id is uniqe if not ass user if they want to creat new acc if yes then entre pass
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
        


# class Deposit(customer,user_login):
#      def __init__(self):
#         super().__init__(self,account_type,user_id,user_login,services_list,money_amount,money_input,savings_amount,checking_amount,both_amount,deposit_type)
#         self.money_input=money_input
#         self.deposit_type =deposit_type
#      def deposit_money(self,account_type,user_id,user_login,services_list,money_input,savings_amount,checking_amount,both_amount,deposit_type):
#         if services_list =="2":
#             money_input = input("How much would you like to add?:") 
#             deposit_type = input("what type of account would you like to deposit? (1-checking account 2-saving account 3-both): ")
#             if deposit_type == "1":
#                 savings_amount += money_input
#                 print (f'Your current amount of money is: {savings_amount}')
#             elif deposit_type == "2":
#                 checking_amount += money_input
#                 print (f'Your current amount of money is: {checking_amount}') 
#             elif deposit_type == "3":
#                 both_amount -= money_input
#                 print(f'Your current amount of money is: {both_amount}')
      
# class Transfer(customer,user_login):
#      def __init__(self,account_type,user_id,user_login,services_list,account_wanted,transfer_amount,transfer_acoount):
#         super().__init__(account_type,user_id,user_login,services_list,transfer_acoount)
#         self.account_wanted=account_wanted
#         self.transfer_amount=transfer_amount
#         self.transfer_acoount=transfer_acoount
#         self.transfer_to_type =transfer_to_type 
#      def transfer_money(self):
#         try:
#             if services_list =="3":
#                 account_wanted = input("please entre account id:")
#                 if account_wanted == user_id:
#                     transfer_acoount = input("what type of account would you like to transfer from? (1-checking account 2-saving account 3-both): ")
#                     if transfer_account == "1":
#                         savings_amount -= money_input
#                         print (f'Your current amount of money is: {savings_amount}')
#                     elif deposit_type == "2":
#                         checking_amount -= money_input
#                         print (f'Your current amount of money is: {checking_amount}') 
#                     elif deposit_type == "3":
#                         both_amount -= money_input
#                         print(f'Your current amount of money is: {botth_amount}')
#                     transfer_to_type = input("please entre type of account you would like to tranfer to:")
#                     if transfer_to_type  == "1":
#                         savings_amount += money_input
#                         print (f'Your current amount of money has been transferd')
#                     elif transfer_to_type  == "2":
#                         checking_amount += money_input
#                         print (f'Your current amount of moneyhas been transferd') 
#                     elif transfer_to_type  == "3":
#                         both_amount += money_input
#                         print(f'Your current amount of money has been transferd')
                  
#                 else:
#                     raise UserError("please entre a valid account number")
#         except ValueError: 
#             raise UserError('please enter valid number') 

# class overdraft(Customer,user_login):
#      def __init__(self,account_type,user_id,user_login,services_list,overdraft,count,money):
#       super().__init__(account_type,user_id,user_login,services_list)
#       self.overdraft=overdraft

#      def overdraft_money(self):
#         count =0
#         if money_amount < 0 :
#              overdraft = money_amount -35 
#              count += 1
#              print("You are chared with fee of 35$")
#              for c in count:
#                 if c>2:
#                     print("Your account have been deactivate") 
#                     if self.money_amount == 0:
#                         print("Your account have been activated") 

# class Bouns():
#      def __init__():
#         super().__init__()



# c = Customer(111111, "password123", 111111, "storepassword", "Leena", "Mansour", 1000, 2000, 3000)
# print("User ID:", c.user_id)  # Output: 111111
# print("First Name:", c.first_name)  # Output: Leena
# print("Last Name:", c.last_name)  # Output: Mansour
# user1 = UserLogin("checking", 111111, "password123", 111111, "storepassword")
# user1.login() 





# c = Customer(111111, "password123", 111111, "storepassword", "Leena", "Mansour", 1000, 2000, 3000)
# print("User ID:", c.user_id)  # Output: 111111
# print("First Name:", c.first_name)  # Output: Leena
# print("Last Name:", c.last_name)  # Output: Mansour
# user1 = UserLogin("checking", 111111, "password123", 111111, "storepassword")
# user1.login() 






# """

#     - **BONUS**
#       - Display Transaction Data (You need to create another file to store the transaction history, required login)
#       list .push()
#       dir list

#       - index all transactions for a customer account

#       - show one transaction **details**
#       - show historical data of transactions (date and time of transaction, type of transaction, resulting balance, etc.)



# """









# """

# user after login they have amount of money in the acc then the user can send the reqiured amount of money to the account 
# they want ,first i will check if the amount of money is out of budget or not then i will check type of account they want
# to send the money to then send the money after and decrease that amount of money from the account and increase it to the 
# other 

# user can add money in both of the two account and increase the amount of money evey time they do


# user maybe have more than 1 accout if he want to transfer money from one acc to another then he first need to login then
# he need to choose the account he want to transfer to (i might add smth like each user have diff transfer num and when user 
# want to transfer money it will appear in thier account ... maybe something like acc num [amount].push ????? 
# also i need each user to have uniqe acc num )

# """