import csv
from datetime import datetime
import csv
import os
import random

class Customer():
    def __init__(self):
        pass

    def display_msg(self):
        print("Welcome to the Banking App")

    def new_customer(self):
        try:
            
            new_account_type = None
            new_account_first_name = None
            new_account_last_name = None
            new_account_pass = None
            random_id = random.randint(10000, 99999)
            type_responses = ["1", "2", "Q"]
            account_types = { "1": "Checking Account", "2": "Savings Account" }
            while new_account_type == None and new_account_type not in type_responses:
                new_account_type = input("What Type of Account Would You Like to Creat? (1-Checking Account 2-Saving Account): ") 
            while new_account_first_name == None:
                new_account_first_name = input("Please Enter Your First Name :")
            while new_account_last_name == None:
                new_account_last_name = input("Please Enter Your Last Name :")
            while new_account_pass == None:
                new_account_pass = input("Please Enter Your Password :")
            add_new_row(random_id=random_id, type_acct=new_account_type, first_name=new_account_first_name, last_name=new_account_last_name, password=new_account_pass)
         
        except Exception as e:
            print(e) 

    def new_acc_type(self,account_id):
        list_customers = read_csv()
        for l in list_customers:
            if l['account_id'] == account_id:
                if l['checking'] == "":
                    l['checking'] = 0
                    print("Your Checking Account Has Been Created")

                elif l['savings'] == "": 
                    l['savings'] = 0
                    print("Your Savings Account Has Been Created")
                    
                else:
                    print("You Aready Have Both Accounts")
                    break
                
            save_changes(l)

# 1.1 Seed Data to CSV
customers_info = [
    { 'account_id': '10006', 'first_name': 'Leena', 'last_name': "Alomar", 'password': "p1", 'checking': "", 'savings': ""},
    { 'account_id': '10007', 'first_name': 'Devlin', 'last_name': "Dawkins", 'password': "p2", 'checking': "", 'savings': ""},
    { 'account_id': '10008', 'first_name': 'Kristina', 'last_name': "Da-Silva", 'password': "p3", 'checking': "", 'savings': ""},
]

# 2.0 Set fieldnames once:
fieldnames = ["account_id", "first_name", "last_name", "password", "checking", "savings"]

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
def read_csv():
    try: 
        with open("banking.csv", "r") as file:
            rows = csv.DictReader(file)
            customer_list = []
            for row in rows:
                customer_list.append(row)
            return customer_list
    except csv.Error as e:
        print(e)

# 5.0 Add Individual Row => "a+" option will allow reading and APPENDING to file
def add_new_row(random_id, type_acct, first_name, last_name, password):
    acct_types = {"1": "checking", "2": "savings"}
    type_acct = acct_types[type_acct]
    print(random_id, type_acct, first_name, last_name, password)

    try:
        new_row = { 'account_id': random_id, 'first_name': first_name, 'last_name': last_name, 'password': password, 'checking': "", 'savings': ""}
        new_row[type_acct] = 0
        with open("banking.csv", "a+") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(new_row)
    except csv.Error as e:
        print(e)

def save_changes(n):
    accounts_info = []
    with open('banking.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            accounts_info.append(row)
    
    with open('banking.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for account in accounts_info:
            if account['account_id'] == n['account_id']:
                account = n
            writer.writerow(account)

class User_login(Customer):
    def __init__(self):
        super().__init__()
        self.user_id=None

    def login(self):
        try:
            login_account_id = None
            login_account_pass = None
            bank_customers = read_csv()
            while login_account_id == None:
                login_account_id = input("Please Enter your ID :")
            while login_account_pass == None:
                login_account_pass = input("Please Entre your  Password :")
            for c in bank_customers:
                if login_account_id == c['account_id'] and login_account_pass == c['password']:
                    print(f'You Have Successfully login, Here are Your Account Info : ')
                    get_info = ['account_id', 'first_name', 'last_name', 'password', 'checking', 'savings']
                    info = {}
                    for g in get_info:
                        if g in c:
                            info[g] = c[g]
                    print(info)
                    self.user_id = login_account_id
                    self.services_user_list()
                    break
            else:
                print("Entre Valid Value")
        except Exception as e:
            print(e) 

    def services_user_list(self):
        self.customer_login = Customer
        services_type = None
        services_respone = ["1", "2", "3", "4","5", "Q"]
        offer_services = { "1": "Withdraw", "2": "Deposit", "3": "Transfer", "4": "Create New Account", "5": "Check Overdraft" }
        while services_type == None and services_type not in services_respone:
            services_type = input(f"Now What Kind of Services Would You Like to Do?  1 - {offer_services['1']}, 2 - {offer_services['2']}, 3 - {offer_services['3']}, 4 - {offer_services['4']}, 5 - {offer_services['5']} :")      
        match services_type:
            case "1":
                return Withdraw.user_withdraw(self,self.user_id) 
            case "2":
                return Deposit.user_deposit(self,self.user_id) 
            case "3":
                return Transfer.user_Transfer(self,self.user_id)
            case "4":
                return Customer.new_acc_type(self,self.user_id)
            case "5":
                return Overdraft.user_overdraft(self,self.user_id)  

class Withdraw():
    def __init__(self):
        pass
    def user_withdraw(self, account_id): 
        lists = read_csv()
        try: 
            wi_type={
                "1": "checking",
                "2": "savings",
            }
            withdraw_input = input("Please Enter The Amount of Money You Would Like To Withdraw :")
            withdraw_from=input("What Type of Account Would You Like to Withdraw To? : 1-Checking 2-Savings :")
            while withdraw_from is not None and withdraw_from in wi_type:
                wi_from = wi_type[withdraw_from]
                for s in lists:
                    if int(withdraw_input) <= 100:
                        if s['account_id'] == account_id and s[wi_from] != "":
                            s[wi_from]= int(s[wi_from]) - int(withdraw_input)
                            print("Your Account Has Been Updated , This is Your Current Balance :")
                            print(s[wi_from])
                            save_changes(s)
                            if int(s[wi_from]) < 0:
                                Overdraft.user_overdraft(self,account_id)
                                save_changes(s)
                                if int(s[wi_from]) <= -100:
                                    print("Your Account Is Less Than -100")   
                                break
                    else:
                        print("Please Entre a Valid Input")
                        break
                            
                # else:
                #     print("Please Entre a Valid Input")
                break 
            save_changes(s) 
                    
        except Exception as e:
            print(e)
            

class Deposit():
    def __init__(self):
        pass  
    def user_deposit(self, account_id): 
        lists = read_csv()
        try: 
            de_type={
                "1": "checking",
                "2": "savings",
            }
            deposit_input = input("Please Enter The Amount of Money You Would Like To Deposit :")
            deposit_from=input("What Type of Account Would You Like to Deposit To? : 1-Checking 2-Savings :")
            while deposit_from is not None and deposit_from in de_type:
                de_from = de_type[deposit_from]
                for s in lists:
                    if s['account_id'] == account_id and s[de_from] != "":
                        s[de_from]= int(s[de_from]) + int(deposit_input)
                        print("Your Account Has Been Updated , This is Your Current Balance :")
                        print(s[de_from])      
                        break
                else:
                    print("Please Entre a Valid Input")
                break 
            save_changes(s) 
                    
        except Exception as e:
            print(e)


class Transfer():
    def __init__(self):
        pass  

    def user_Transfer(self, account_id): 
        lists = read_csv()
        try:
            tr_type={
                "1": "checking",
                "2": "savings",
            }
            tr_input = input("Please Enter The Amount of Money You Would Like To Transfer :")
            tr_from=input("What Type of Account Would You Like to Transfer Money From ? : 1-Checking 2-Savings :")
            while tr_from is not None and tr_from in tr_type:
                    transfer_from = tr_type[tr_from]
                    for s in lists:
                        if s['account_id'] == account_id and int(s[transfer_from]) >= int(tr_input):
                            s[transfer_from]= int(s[transfer_from]) - int(tr_input)
                            print("Your Account Has Been Updated , This is Your Current Balance :")
                            print(s[transfer_from])   
                            save_changes(s)  
                            break
                    else:
                        print("Please Entre a Valid Input")
                        break   
                        
                    tr_id= input("Entre The User ID :")
                    tr_to=input("What Type of Account Would You Like to Transfer Money From ? : 1-Checking 2-Savings :")
                    while tr_to is not None and tr_to in tr_type:
                        tranfer_to=  tr_type[tr_to]
                        for s1 in lists:
                            if s1['account_id'] == tr_id and s1[transfer_from] != "":
                                s1[transfer_from]= int(s1[transfer_from]) + int(tr_input) 
                                print("The Amount Of Money Is Transferd :") 
                                save_changes(s1)
                                break
                            
                        else:
                            print("Please Entre a Valid Input")
                            break
                                
                        break 
            save_changes(s) 
                    
        except Exception as e:
            print(e)





#         # lists = read_csv()
#         # try:
#         #     withdraw = Withdraw()
#         #     withdraw.user_withdraw(account_id)
#         #     deposit = Deposit()
#         #     tr= input("Entre The User ID You Want To Tranfer Money To : ")
#         #     deposit.user_deposit(tr)

#         #     save_changes(s)       
#         # except Exception as e:
#         #     print(e)


class Overdraft():
    def __init__(self):
        pass  
    def user_overdraft(self, account_id): 
        lists = read_csv()
        count = 0
        try: 
            o_type={
                "1": "checking",
                "2": "savings",
            }
            
            overdraft_check=input("What Type of Account Would You Like to Check the Overdraft? : 1-Checking 2-Savings :")
            while overdraft_check is not None and overdraft_check in o_type:
                over = o_type[overdraft_check]
                for s in lists:
                    if s['account_id'] == account_id and s[over] != "":
                        if int(s[over]) < 0:
                            s[over]= int(s[over]) - 35      
                            print("You are chared with fee of 35$")
                            if int(s[over]) < -70:
                                print("Your Account Status : Deactivate")
                                save_changes(s) 
                                break
                        else:
                            print("Your Account Status : Activated")
                            save_changes(s)
                            break 
                    # else:
                    #     print("Entre a Valid Input")  
                break
        except Exception as e:
            print(e)
# class 
# def init():
#   Customer.start_session()

# init()

# c=Customer()
# c.display_msg()
# c.new_customer()
l=User_login()
l.login()

