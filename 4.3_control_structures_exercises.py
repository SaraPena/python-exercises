# Do your work for this exercise in a file named 4.3_control_structures_exercises.py.

# 1. Conditional Basics
#   a. prompt the user for day of the week, print out whether the day is Monday or not.

user_day_of_the_week = input("What day of the week is today? ")

if user_day_of_the_week.lower() == "monday":
    print ('Today is {}'.format(user_day_of_the_week))
else:
    print ("Today is NOT Monday")

#   b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend.

if user_day_of_the_week.lower() in ["saturday","sunday"]:
    print ("It's the weekend!")
else:
    print("It's a weekday, you are at Codeup :)!")

# c. create variables and make up values for: 
#      - the number of hours worked in one week 
#      - the hourly rate
#      - how much the week's paycheck will be
#     write the python code that calculates the weekly paycheck. you get paid time and a half if you work more than 40 hours. 

user_number_of_hours_worked_one_week = input("How many hours did you work this week? ")
user_hourly_rate = input("How much do you get paid per hour? ")

print("Number of hours worked: " + str(user_number_of_hours_worked_one_week))
print("Hourly Rate: "+ str(user_hourly_rate))


if int(user_number_of_hours_worked_one_week) <= 40:
    paycheck = int(user_number_of_hours_worked_one_week) * int(user_hourly_rate)
    print("Paycheck $$$$$ : $" + str(paycheck))
else:
    paycheck = (int(user_number_of_hours_worked_one_week) - 40) * (1.5 * int(user_hourly_rate)) + (40 * int(user_hourly_rate))
    print("You work too much! You make time and a half for hours over 40! Paycheck $$$$$ : $" + str(paycheck))
    
 