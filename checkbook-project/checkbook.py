#Open balance.txt to find the most recent balance that will be on the last line - bl[-1]

print("~~~~~ Welcome to your terminal checkbook!~~~~~")

choice_box = "\nWhat would you like to do?\n\n1) view current balance\n2) record a debit(withdraw)\n3) record a credit (deposit)\n4) exit\n\nYour choice? "

user_input = input(choice_box)

while True:
    if user_input == '1':
        with open("balance.txt", "r+") as b:
            b.seek(0)
            bl = b.readlines()
            current_balance = float(bl[-1].split()[2])
            print(f'\nYour current balance is : ${current_balance:.2f}')
            user_input = input(choice_box)


    if user_input == '2':
        with open("withdraw.txt", "a+") as w:
            withdraw_amount = input("\nhow much would you like to withdraw? ")
            w.write(withdraw_amount+"\n")
            withdraw_amount = float(withdraw_amount)
            print(f'\nYou are withdrawing ${withdraw_amount:.2f}')
        
        with open("balance.txt","a+") as b:    
            b.seek(0)
            bl = b.readlines()
            current_balance = float(bl[-1].split()[2])
            new_balance = current_balance - withdraw_amount
            b.write(f'balance : {new_balance:.2f}\n')
            print(f'\nYour new balance is ${new_balance:.2f}')
            user_input = input(choice_box)


    if user_input == '3':
        with open("deposit.txt", "a+") as d:
            deposit_amount = input("\nhow much would you like to deposit? ")
            d.write(deposit_amount+"\n")
            deposit_amount = float(deposit_amount)
            print(f'\nYou are depositing ${deposit_amount:.2f}')
        
        with open("balance.txt","a+") as b:    
            b.seek(0)
            bl = b.readlines()
            current_balance = float(bl[-1].split()[2])
            new_balance = current_balance + deposit_amount
            b.write(f'balance : {new_balance:.2f}\n')
            print(f'\nYour new balance is ${new_balance:.2f}')
            user_input = input(choice_box)

    if user_input == '4':
        print('Thanks for banking with ABC Telco :)')
        break

    if user_input.isdigit() != True or int(user_input) > 4:
        user_input = input(f'\nERROR: Please enter only a number from the menu to select a action.\n{choice_box}')
