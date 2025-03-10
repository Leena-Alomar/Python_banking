import csv
from datetime import datetime
import csv
import os
import random
####### CLASSES #######
class Customer():
    def __init__(self, name):
        self.name = name

    def display_msg(self):
        print("Welcome to the Banking App")    
    def new_customer(self):
        try:
            # new account information
            new_account_type = None
            new_account_first_name = None
            new_account_last_name = None
            new_account_pass = None
            random_id =random.randint(10000, 99999)
            type_responses = ["1", "2", "Q"]
            account_types = { "1": "Checking Account", "2": "Savings Account" }
            while new_account_type == None and new_account_type not in type_responses:
                new_account_type = input("What Type of Account Would You Like to Creat? (1-Checking Account 2-Saving Account): ") 
            while new_account_first_name == None:
                new_account_first_name = input("Please enter your first name")
            while new_account_last_name == None:
                new_account_last_name = input("Please enter your last name")
            while new_account_pass == None:
                new_account_pass = input("Please enter a password")
            add_new_row(random_id=random_id,type_acct=new_account_type, first_name=new_account_first_name, last_name=new_account_last_name, password=new_account_pass)
            # quit program
        except Exception as e:
            print(e) 


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
def add_new_row(random_id,type_acct, first_name, last_name, password ):
    acct_types = {"1": "checking", "2": "savings"}
    type_acct = acct_types[type_acct]
    print(random_id,type_acct, first_name, last_name, password)


    try:
        new_row = { 'account_id': random_id, 'first_name': first_name, 'last_name': last_name, 'password': password ,'checking': "", 'savings': ""}
        new_row[type_acct] = 0
        with open("banking.csv", "a+") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(new_row)
    except csv.Error as e:
        print(e)


class User_login(Customer):
    def __init__(self):
      super().__init__(self)
    def login(self):
        try:
            login_account_id = None
            login_account_pass = None
            bank_customers = read_csv()
            while login_account_id == None:
                login_account_id = input("Please Enter your ID:")
            while login_account_pass == None:
                login_account_pass = input("Please Entre your  Password:")
            for c in bank_customers:
                if login_account_id == c['account_id'] and login_account_pass == c['password']:
                    print(f'You Have Successfully login, Here are Your Account Info : ')
                    get_info = ['account_id', 'first_name', 'last_name', 'password','checking', 'savings' ]
                    info={}
                    for g in get_info:
                        if g in c:
                            info[g] = c[g]
                    print(info)
                    break
            else:
                print("Entre Valid Value")
        except Exception as e:
                    print(e) 

    def services_user_list(self):
        self.customer_login=Customer
        services_type=None
        services_respone = ["1","2","3","4", "Q"]
        offer_services = { "1": "Withdraw", "2": "Deposit", "3": "Transfer", "4": "Create New Account" }
        while services_type == None and services_type not in services_respone:
            services_type = input(f"Now What Kind of Services Would You Like to Do?  1 - {offer_services['1']}, 2 - {offer_services['2']}, 3 - {offer_services['3']}, 4 - {offer_services['4']}:")      
        match services_type:
            case "1":
                pass
            case "2":
                return 
            case "3":
                return 
            case "4":
                customer_login.new_customer()
            #type_ser = "Q"


   
# class withdraw():



# class 
       
# c= Customer('leena')
# c.display_msg()
# c.new_customer()
l=User_login()
l.login()
l.services_user_list()
