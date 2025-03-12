

![gif](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3J5YWN4Y2hyeHBrZjVjbGN5bGZ6eWsyN3k1c2d4NTRpdmFrbTAwayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YYW0hHizzIOrlhimPG/giphy.gif)

# Python Banking Project

This is a banking application that allows users to perform basic banking services such as creating new accounts, checking balances, depositing money, withdrawing money, transferring money between accounts and checking overdrafts
It uses a CSV file to store customer data such as account information, names, and balances for simplicity. 

## Functionality
  
1. Account Creation	: Users can create a new account by providing their first and last names, and setting up a password. They can also select the type of account (checking or savings).
2. User Login	Users can log in using their account ID and password. If the login is successful, they are shown their account details.
3. Withdraw Money :	After logging in, users can withdraw money from their checking or savings account. The app checks if the user has sufficient balance for withdrawal.
4. Deposit Money :	Users can deposit money into their checking or savings account. The balance is updated accordingly.
5. Transfer Money :	Users can transfer money between their checking and savings accounts or even to another user's account.
6. Create New Account :	Users can create a new type of account (checking or savings) if they don’t already have both types.
7. Check Overdraft :	Users can check for overdrafts in their account. If their balance goes below $0, an overdraft fee may be applied, and the account may be deactivated if the balance goes below -$70.


## Technologies used
1. CSV (Comma Separated Values):
Used to store customer account information, including account IDs, first names, last names, passwords, and balances for checking and savings accounts. The csv module allows reading from and writing to CSV files, providing a simple way to handle user data.

2. Random:
This module is used to generate random account IDs for new customers, ensuring that each user gets a unique identifier when creating an account.


## Icebox Features

1. Account Notifications:
Users will receive SMS or email notifications whenever a transaction is made or when their balance drops below a set amount.

2. Multi-Factor Authentication (MFA):
Add an extra layer of security during login by verifying users through SMS or email.

3. Bank Loan Application:
Allow users to apply for loans, check their loan balance, and make repayments directly within the app.

4. Graphical User Interface (GUI):
Create a user-friendly interface where users can interact with the app using buttons, text fields, and other visual elements.

5. Currency Exchange:
Integrate an API to get real-time currency exchange rates, so users can convert their money between different currencies easily.


## Challenges

1. File Handling:
Managing data in CSV files becomes challenging when users try to modify the file to update their information, as it may lead to data inconsistencies or errors.

2. Error Handling:
The app struggles with handling errors, such as invalid inputs or issues during file reading and writing. Improved error handling is needed to prevent crashes and provide users with clear, helpful feedback.

3. Infinite Loops:
The app occasionally gets stuck in infinite loops when users enter incorrect information. Implementing better input validation and exit conditions can prevent this from happening. :money_with_wings:

4. Saving Data to CSV:
Writing data to the CSV file can result in problems like overwriting or creating duplicate entries. A more efficient method for saving and updating data would help maintain file integrity
   