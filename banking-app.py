import json

#open my user-accounts file so I can parse to json

with open('users-accounts.json', 'r') as f:
    bank_data = json.load(f)
input_username = input("Enter your username: ")

for account in bank_data["accounts"]:

    if input_username.lower() == account["username"].lower():

        input_password = input("Enter your password: ")
        if input_password == account["password"]:
            print("Correct Password!")
        else:
            print("Incorrect password.")
        break
else:
    print("Username not found")

  


# Print all

def bank_account_dictionary(user_accounts):
    bank_files = open(user_accounts, "r").readlines()

    #dictionary 
    bank_accounts = {}

    for files in bank_files:
        split_file_list = files.strip().split(",")

        account_name = split_file_list[0]
        account_password = split_file_list[1]
        full_name = split_file_list[2]
        account_balance = split_file_list[3]


        bank_accounts[account_name] = str(account_password)
        bank_accounts[full_name] = str(account_balance)
    return bank_accounts

# print(bank_account_dictionary("users-account-info.txt"))
    

# Storing my user-account-info in a user_accounts.

# user_accounts = 'users-account-info.txt'

# read_user_accounts = open(user_accounts, 'r')

# #read.lines() will create a list where each 
# #element iws a line from the user-account-info

# lines = read_user_accounts.readlines()


# #Dictionary for my account users

# bank_accounts = {}

# for line in lines:
#     # Strip puts on new line
#     stripped_line = line.strip()
#     # split use delimiter to format
#     split_line = stripped_line.split(',')

#     #access key and value from split line.
#     key = split_line[0]
#     value = split_line[1]

#     # add to bank_accounts dictionary 
#     bank_accounts[key] = value
   

# print(bank_accounts)