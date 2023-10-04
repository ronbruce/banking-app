# I imported this JSON file to parse user data (key-value pairs)
# without dealing with extra information from users-account-info.txt.
# JSON was chosen for its simplicity and suitability for this task.
import json

#FUNCTION 1: Open the user-accounts file to parse it in JSON. 

with open('users-accounts.json', 'r') as f:
    bank_data = json.load(f)
input_username = input("Admin use: Enter a user's name: ")

for account in bank_data["accounts"]:

    if input_username.lower() == account["username"].lower():

        input_password = input("Admin use: Enter a user's password: ")
        user_password = account["password"]
   
    # Handle the case where the stored password is an integer.
        if isinstance(user_password, int):
            try:
    # this try catch tries to convert my stored password to an integer
                input_password = int(input_password)
    # Attempt to convert the user's input to an integer.
            except ValueError:
    # If the conversion fails, print an error message and exit.
                print("Incorrect password.")
                break

        if input_password == user_password:
            print("Correct password")
        else: 
            print("Incorrect password.")
        break
else:
        print("Username not found")

# FUNCTION 2: Get all users information.

def bank_account_dictionary(user_accounts):
    bank_files = open(user_accounts, "r").readlines()

    # Dictionary to store user information
    bank_accounts = {}

    for files in bank_files:
        split_file_list = files.strip().split(",")

        account_name = split_file_list[0]
        account_password = split_file_list[1]
        full_name = split_file_list[2]
        account_balance = split_file_list[3]


        bank_accounts[account_name] = {
            "password": str(account_password),
            "fullname": full_name,
            "balance": float(account_balance)
        }
    return bank_accounts

# Print all user information.

def print_all_users_info(accounts_dict):
    for username, info in accounts_dict.items():
        print(f"Username: {username}")
        print(f"Password: {info['password']}")
        print(f"Full Name: {info['fullname']}")
        print(f"Blance: {info['balance']}" )
        print()

# Get the bank accounts dictionary 
bank_account_dict = bank_account_dictionary("users-account-info.txt")

user_choice = input("Do you want to print all the user information? (yes/no)").strip().lower()

if user_choice == "yes":

    print_all_users_info(bank_account_dict)
else:
    print("No user information will be printed")

# FUNCTION 3: Login In to get user information.

user_data = {
    "aman": {
        "username": "aman",
        "password": 1234,
        "fullname": "Andy Allman",
        "balance": 1000
    },

    "betho": {
        "username": "betho",
        "password": "pa$$word",
        "fullname": "Beth Beto",
        "balance": 2000
    },

    "camcam": {
        "username": "camcam",
        "password": "default",
        "fullname": "Cameron Clay",
        "balance": 3000
    },
}

print("User Log In Menu: ")
# Personal note: username and password are parameters in my login function,
# They are later called as arguments when I invoke my login() function. 
def login(username, password):
    if username in user_data:
# Retrieve user information from the user_data dictionary. 
        user = user_data[username]
        stored_password = user["password"]
# Check if the stored password is an integer and convert is to a string if needed.
        if isinstance(stored_password, int):
            stored_password = str(stored_password)
        if password == stored_password:
            return user["fullname"], user["balance"]
        else:
            return None
    else:
        return None

#Prompt the user for their name and password.
user_input = input("Enter your name: ")
password_input = input("Enter your password: ")

#Attempt to log in using the provided credentials. 
result = login(user_input, password_input)

if result:
# If login is successful, extract and print user information.
    fullname, balance = result
    print("Login a success!")
    print("User:", fullname)
    print("Balance:", balance)
else:
    print("Bummer! Log in failed.")

###################################################################################

# Pseudocode:
# Create an empty dictionary to store user information
# user_information_dict = {}

# Function login(username, password)
#   PROMPT for username input
#   INPUT username
#   PROMPT for password input
#   INPUT password

#   IF username exists in user_information_dict AND password matches the stored password
#       RETURN user_information_dict[username]["fullname"] and user_information_dict[username]["balance"]
#   ELSE
#       RETURN None

# Prompt the user for their username and password
# user_input = INPUT "Enter your username: "
# password_input = INPUT "Enter your password: "

# Call the login function with user_input and password_input as arguments
# result = login(user_input, password_input)

# IF result is not None
#   PRINT "Login successful!"
#   PRINT "User:", result[0]  # Fullname
#   PRINT "Balance:", result[1]  # Balance
# ELSE
#   PRINT "Bummer! Login failed."