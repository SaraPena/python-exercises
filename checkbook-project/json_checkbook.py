#This is latest version of checkbook app.

import json
import datetime as dt

print("\n~~~~~ Welcome to your terminal checkbook!~~~~~")

choice_box = "\nWhat would you like to do?\n1) Check current balance\n2) Make a withdrawal?\n3) Make a deposit\n4) exit\n\nYour choice: "

user_input = input(choice_box)

while True:

    if user_input == '1':
       
        with open('json_balance.json','r') as jb:
            balance_data = json.load(jb)
            current_balance = float(balance_data[-1]['balance'])
            
            if current_balance == 0:
                print ("\nCAUTION: Your balance is now $0.00, if you overdraft you will incur fees. ")

            if current_balance < 0:
                print ("\nCAUTION: Your balance is below $0.00, if you overdraft you will incur fees. ")
            
            print(f'\nYour current balance is : ${current_balance:.2f}')

            user_input = input(choice_box)

    if user_input == '2':
        with open("json_withdraw.json", "r") as jw:
            with open("json_balance.json","r") as jb: 
                
                withdraw_data = json.load(jw)   
                
                balance_data = json.load(jb)

                current_balance = float(balance_data[-1]['balance'])

                if current_balance == 0:
                    print ("\nCAUTION: Your balance is now $0.00, if you overdraft you will incur fees. ")
                    
                if current_balance < 0:
                    print ("\nCAUTION: Your balance is below $0.00, if you overdraft you will incur fees. ")
                
                withdraw_amount = float(input("\nHow much would you like to withdraw? $"))
                
                new_balance = current_balance - withdraw_amount

                time = "{}".format(dt.datetime.now().strftime("%H:%M:%S"))
        
                withdraw_category = input("\nWhat type of withdrawal are you making? Example: Food \n\nYour type of withdrawal: ")

                withdraw_data.append({"withdraw" : withdraw_amount, "withdraw_category": withdraw_category, "timestamp": time}) 

                balance_data.append({"balance" : float(new_balance)})

                with open('json_balance.json', 'w') as jb:
                    json.dump(balance_data,jb)

                with open('json_withdraw.json', 'w') as jw:
                    json.dump(withdraw_data,jw)

                print(f'\nYou are withdrawing ${withdraw_amount:.2f}')

                print(f'\nYour new balance is ${new_balance:.2f}')

                user_input = input(choice_box)

    if user_input == '3':

        with open("json_deposit.json", "r") as jd:

            deposit_data = json.load(jd)

            deposit_amount = float(input("\nhow much would you like to deposit? $"))

            deposit_data.append({"deposit" : deposit_amount})
            print(f'\nYou are depositing ${deposit_amount:.2f}')
        
        with open("json_deposit.json","w") as jd:
            json.dump(deposit_data,jd)

        with open("json_balance.json","r") as jb:

            balance_data = json.load(jb)

            current_balance = float(balance_data[-1]["balance"])

            new_balance = current_balance + deposit_amount

            balance_data.append({"balance" : new_balance})

        with open("json_balance.json","w") as jb:
            json.dump(balance_data,jb)

        print(f'\nYour new balance is ${new_balance:.2f}')
        user_input = input(choice_box)

    if user_input == '4':
        print('Thanks for banking with ABC Telco $$:)$$\n')
        break

    if user_input.isdigit() != True or int(user_input) > 4:
        user_input = input(f'\nERROR: Please enter only a number from the menu to select a action.\n{choice_box}')
