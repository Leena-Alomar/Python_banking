import csv
from datetime import datetime
import csv
import os
import random

class Customer():
    def __init__(self):
        pass

    def display_msg(self):
        print("______________________________________")
        print("     ") 
        print("Welcome to the Banking App \U0001F3E6 \U00002728")

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
                new_account_type = input("What Type of Account Would You Like to Creat? (\U0001F538 1-Checking Account \U0001F538 2-Saving Account): ") 
            while new_account_first_name == None:
                new_account_first_name = input("\U0001F7E3 Please Enter Your First Name :")
            while new_account_last_name == None:
                new_account_last_name = input(" \U0001F7E3 Please Enter Your Last Name :")
            while new_account_pass == None:
                new_account_pass = input(" \U0001F7E3 Please Enter Your Password :")
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

customers_info = [
    { 'account_id': '10006', 'first_name': 'Leena', 'last_name': "Alomar", 'password': "p1", 'checking': "", 'savings': ""},
    { 'account_id': '10007', 'first_name': 'Devlin', 'last_name': "Dawkins", 'password': "p2", 'checking': "", 'savings': ""},
    { 'account_id': '10008', 'first_name': 'Kristina', 'last_name': "Da-Silva", 'password': "p3", 'checking': "", 'savings': ""},
]


fieldnames = ["account_id", "first_name", "last_name", "password", "checking", "savings"]


if not os.path.exists("./banking.csv"):
    with open("./banking.csv", 'w', newline='') as csvfile:
        try:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in customers_info:
                writer.writerow(row)
        except csv.Error as e:
            print(e)


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
                print("______________________________________")
                print("     ") 
                login_account_id = input("\U0001F7E3 Please Enter your ID :")
            while login_account_pass == None:
                login_account_pass = input("\U0001F7E3 Please Entre your Password :")
            for c in bank_customers:
                if login_account_id == c['account_id'] and login_account_pass == c['password']:
                    print("______________________________________")
                    print("     ") 
                    print(f'You Have Successfully login \U00002705 Here are Your Account Info : ')
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
        services_respone = ["1", "2", "3", "4", "Q"]
        offer_services = { "1": "Withdraw", "2": "Deposit", "3": "Transfer", "4": "Create New Account" }
        while services_type == None and services_type not in services_respone:
            print("______________________________________")
            print("     ") 
            services_type = input(f"Now What Kind of Services Would You Like to Do?  \U0001F538 1 - {offer_services['1']}, \U0001F538 2 - {offer_services['2']}, \U0001F538 3 - {offer_services['3']},  \U0001F538 4 - {offer_services['4']}  :")      
        match services_type:
            case "1":
                return Withdraw.user_withdraw(self,self.user_id) 
            case "2":
                return Deposit.user_deposit(self,self.user_id) 
            case "3":
                return Transfer.user_Transfer(self,self.user_id)
            case "4":
                return Customer.new_acc_type(self,self.user_id)

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
            print("______________________________________")
            print("     ") 
            withdraw_input = input("\U0001F7E3 Please Enter The Amount of Money You Would Like To Withdraw :")
            withdraw_from=input("What Type of Account Would You Like to Withdraw To? :  \U0001F538 1-Checking  \U0001F538 2-Savings :")
            while withdraw_from is not None and withdraw_from in wi_type:
                wi_from = wi_type[withdraw_from]
                for s in lists:
                    if int(withdraw_input) <= 100:
                        if s['account_id'] == account_id and s[wi_from] != "":
                            s[wi_from]= int(s[wi_from]) - int(withdraw_input)
                            print("Your Account Has Been Updated \U00002705 This is Your Current Balance :")
                            print(s[wi_from])
                            save_changes(s)
                            if int(s[wi_from]) < 0:
                                Overdraft.user_overdraft(self,account_id, withdraw_from)
                                # save_changes(s)
                                if int(s[wi_from]) <= -100:
                                    print("Your Account Is Less Than -100  \U0000274C")   
                                break
                    else:
                        print("Please Entre a Valid Input  \U0000274C")
                        break
                            
                
                break 
            
                    
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
            print("______________________________________")
            print("     ") 
            deposit_input = input("Please Enter The Amount of Money You Would Like To Deposit :")
            deposit_from=input("What Type of Account Would You Like to Deposit To? :  \U0001F538 1-Checking   \U0001F538 2-Savings :")
            while deposit_from is not None and deposit_from in de_type:
                de_from = de_type[deposit_from]
                for s in lists:
                    if s['account_id'] == account_id and s[de_from] != "":
                        s[de_from]= int(s[de_from]) + int(deposit_input)
                        print("Your Account Has Been Updated \U00002705 This is Your Current Balance :")
                        print(s[de_from])      
                        break
                else:
                    print("Please Entre a Valid Input  \U0000274C")
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
            print("______________________________________")
            print("     ") 
            tr_input = input("Please Enter The Amount of Money You Would Like To Transfer :")
            tr_from=input("What Type of Account Would You Like to Transfer Money From ? :  \U0001F538 1-Checking  \U0001F538 2-Savings :")
            s1_account_match = False
            while tr_from is not None and tr_from in tr_type:
                transfer_from = tr_type[tr_from]
                for s in lists:
                    if s['account_id'] == account_id and int(s[transfer_from]) >= int(tr_input):
                        s[transfer_from]= int(s[transfer_from]) - int(tr_input)
                        print("Your Account Has Been Updated \U00002705 This is Your Current Balance :")
                        print(s[transfer_from])   
                        save_changes(s)  
                        break
 
                break
            tr_to=input("What Type of Account Would You Like to Transfer Money To ? :  \U0001F5381-Checking  \U0001F538 2-Savings :")
            tr_id= input("Entre The User ID :")
            while tr_to is not None and tr_to in tr_type:
                transfer_to = tr_type[tr_to]
                for s1 in lists:
                    if s1['account_id'] == tr_id and s1[transfer_to] != "":
                        s1_account_match = True
                        s1[transfer_to]= int(s1[transfer_to]) + int(tr_input)
                        print("The Amount Of Money Is Transferd \U00002705:") 
                        print(tr_input)
                        save_changes(s1)
                        return
                if s1_account_match == False:
                    transfer_from = tr_type[tr_from]
                    for s in lists:
                        if s['account_id'] == account_id:
                            s[transfer_from]= int(s[transfer_from]) + int(tr_input)
                    print("Please Entre a Valid Input  \U0000274C")
                break
            if tr_to != tr_type['1'] or tr_to != tr_type['2']:
                for s in lists:
                    if s['account_id'] == account_id:
                        s[transfer_from]= int(s[transfer_from]) + int(tr_input)
                print("Please Entre a Valid Input  \U0000274C")        
            save_changes(s) 



        except Exception as e:
            print(e)

    


class Overdraft():
    def __init__(self):
        pass  
    def user_overdraft(self, account_id, account_from): 
        lists = read_csv()
        count = 0
        try: 
            o_type={
                "1": "checking",
                "2": "savings",
            }
            print("______________________________________")
            print("     ") 
            overdraft_check=account_from
            while overdraft_check is not None and overdraft_check in o_type:
                over = o_type[overdraft_check]
                for s in lists:
                    if s['account_id'] == account_id and s[over] != "":
                        if int(s[over]) < 0:
                            result = s[over]= int(s[over]) - 35
                            print('result', result)
                            print('account status', s[over])
                            save_changes(s) 
                            print("You are chared with fee of 35$")
                            if int(s[over]) < -70:
                                print("Your Account Status : Deactivate  \U0000274C")
                                save_changes(s)
                            break
                        else:
                            print("Your Account Status : Activated \U00002705")
                            save_changes(s)
                            break 
                  
                break
        except Exception as e:
            print(e)


# c=Customer()
# c.display_msg()
# c.new_customer()
l=User_login()
l.login()

