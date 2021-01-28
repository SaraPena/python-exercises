# This is latest version of checkbook app with comments
# I have a previouse file checkbook.py that stores balances, deposits, and withdrawals in seperate text files.
# Going to work with json so we can format the data in dictionaries, and lists.
import json
import datetime as dt

# Welcome user to terminal checkbook.
print("\n~~~~~ Welcome to your terminal checkbook!~~~~~")

# create a string variable choice_box to use throughout the program to prompt the user to select an action.
choice_box = "\nWhat would you like to do?\n1) Check current balance\n2) Make a withdrawal?\n3) Make a deposit\n4) exit\n\nYour choice: "

# Start by asking the user for input and what they woud like to do.
user_input = input(choice_box)

# Using a while loop to keep asking the user they action they would like to take, until they choose to exit.
while True:

    # if user_input == '1' (user_input variable will be a string type) they chose to "view their balance". This if statement will print the user's current balance.
    if user_input == '1':

        # The balance for the user is going to come from a json file that stores the running balance of the account.
        # balance_data will be assigned the list of dictionaries of balances that are stored in json_balance.json. balance_data will be a list type.
        # current_balance will be assigned the last index balance_data[-1]. To grab the value from the index the variable will point to the value for the 'balance' key.
        # to handle cents in money I assigned the current_balance variable as float type.
        with open('json_balance.json','r') as jb:
            balance_data = json.load(jb)
            current_balance = float(balance_data[-1]['balance'])
            
            # If the current_balance value is equal to 0. A Caution message will be sent to the user about overdraft fees. 
            # For a future version we could limit the actions that are available to them if their balance is 0, such as only depositing or viewing balance.
            if current_balance == 0:
                print ("\nCAUTION: Your balance is now $0.00, if you overdraft you will incur fees. ")

            # If the current_balance value is less than 0. A different caution message will be sent to the user about overdraft fees.
            if current_balance < 0:
                print ("\nCAUTION: Your balance is below $0.00, if you overdraft you will incur fees. ")
            
            # Because the user selected option '1' print the user's current balance from the current_balance variable
            print(f'\nYour current balance is : ${current_balance:.2f}')

            # Continue the while loop by asking the user for another action.
            user_input = input(choice_box)

    # if user_input == '2' (user_input variable will be a string type) they chose to "make a withdrawal".
    # This if statement will update the json_withdrawal file with the amount withdrawn
    # The json_balance will be with the running balance of the account.
    if user_input == '2':

        # The json_withdraw.json file will hold the withdrawal amounts made my the user as a list of dictionaries.
        with open("json_withdraw.json", "r") as jw:
            with open("json_balance.json","r") as jb: 
                # withdraw_data will be assigned the list of dictionaries of withdrawals that are stored in json_withdraw.json. 
                # withdraw_data will be a list type.
                withdraw_data = json.load(jw)   
                
                # balance_data will be assigned the list of dictionaries of balances that are stored in json_balance.json. 
                # balance_data will be a list type.
                balance_data = json.load(jb)

                # current_balance will be assigned the last index balance_data[-1]. 
                # To grab the value from the index the variable will point to the value for the 'balance' key.
                current_balance = float(balance_data[-1]['balance'])

                # If the current_balance value is equal to 0. 
                # A Caution message will be sent to the user about overdraft fees.     
                if current_balance == 0:
                    print ("\nCAUTION: Your balance is now $0.00, if you overdraft you will incur fees. ")
                    
                # If the current_balance value is less than 0. 
                # A different caution message will be sent to the user about overdraft fees.
                if current_balance < 0:
                    print ("\nCAUTION: Your balance is below $0.00, if you overdraft you will incur fees. ")
                
                    
                # withdraw_amount will ask the user how much money they would like to take. 
                # This input variable will be stored as a string type.
                withdraw_amount = float(input("\nHow much would you like to withdraw? $"))
                

                # Calculate new_balance variable by subtracting the withdraw_amount from the current_balance

                new_balance = current_balance - withdraw_amount

                time = "{}".format(dt.datetime.now().strftime("%H:%M:%S"))
        
                #withdraw_amount = 12.00 (test for python interactive)

                # Ask user what type of withdrawal they would like to make. 
                # This input variable will be stored as a string type

                withdraw_category = input("\nWhat type of withdrawal are you making? Example: Food \n\nYour type of withdrawal: ")

                # append the withdraw_data list with the new input from withdraw_amount input variable.
                # for future versions with date time stamp we could search for withdrawals by certain dates.
                # for future version we can filter by categorys of withdrawals.

                withdraw_data.append({"withdraw" : withdraw_amount, "withdraw_category": withdraw_category, "timestamp": time}) 



                # append the balance_data list with a new balance dictionary.
                balance_data.append({"balance" : float(new_balance)})

                # update json_files with appeneded lists balance data & withdraw data using dump()
                with open('json_balance.json', 'w') as jb:
                    json.dump(balance_data,jb)
                with open('json_withdraw.json', 'w') as jw:
                    json.dump(withdraw_data,jw)

                # Because the user selected option '2' print the amount the user withdrew.
                print(f'\nYou are withdrawing ${withdraw_amount:.2f}')

                # print the user's current balance from the current_balance variable
                print(f'\nYour new balance is ${new_balance:.2f}')

                # Continue the while loop by asking the user for another action.
                user_input = input(choice_box)


    # if user_input == '2' (user_input variable will be a string type) they chose to "make a deposit".
    # This if statement will update the json_deposit file with the amount deposited.
    # The json_balance will be updated with the running balance of the account.

    if user_input == '3':

        # deposits by the user will be stored in json_deposit.json.
        with open("json_deposit.json", "r") as jd:

            # deposit_data will be assigned the list of dictionaries of deposits that are stored in json_balance.json. deposit_data will be a list type.
            deposit_data = json.load(jd)

            # The user will input how much they want to deposit and the input will be stored as deposit_amount. 
            # I assigned the variable to a float type to handle cents.
            deposit_amount = float(input("\nhow much would you like to deposit? $"))

            # I updated the deposit_data list with the new deposit stored as dictionary with a time-stamp.
            # for future versions we could find deposits and filter based off of timestamps.
            deposit_data.append({"deposit" : deposit_amount})
            print(f'\nYou are depositing ${deposit_amount:.2f}')
        
        # update json_files with appeneded deposit_data list using dump()
        with open("json_deposit.json","w") as jd:
            json.dump(deposit_data,jd)

        # Open json_balance file
        with open("json_balance.json","r") as jb:

            # Store data in json_balance file as a list with .load() method    
            balance_data = json.load(jb)

            # current_balance will be assigned the last index balance_data[-1]. 
            # To grab the value from the index the variable will point to the value for the 'balance' key.
            current_balance = float(balance_data[-1]["balance"])

            # Calculate new_balance variable by adding the deposit_amount to the current_balance
            new_balance = current_balance + deposit_amount

            # append the balance_data list with a new balance dictionary
            balance_data.append({"balance" : new_balance})

        # update json_files with appeneded balance data list using dump()
        with open("json_balance.json","w") as jb:
            json.dump(balance_data,jb)

        # print new balance update to user
        print(f'\nYour new balance is ${new_balance:.2f}')
        user_input = input(choice_box)

    # if user_input == '2' (user_input variable will be a string type) they chose to "exit".
    # This if statement will print an exit message and leave the loop with "break"
    if user_input == '4':
        print('Thanks for banking with ABC Telco $$:)$$')
        break

    # if the user_input is not a digit or greater than 4 then the 
    if user_input.isdigit() != True or int(user_input) > 4:
        user_input = input(f'\nERROR: Please enter only a number from the menu to select a action.\n{choice_box}')
