"""
Do your work for this exercise in a file named 4.3_control_structures_exercises.py.

   1. Conditional Basics
   a. prompt the user for day of the week, print out whether the day is Monday or not.
"""

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

"""
 c. create variables and make up values for: 
      - the number of hours worked in one week 
      - the hourly rate
      - how much the week's paycheck will be
     write the python code that calculates the weekly paycheck. you get paid time and a half if you work more than 40 hours. 
"""

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
    
"""
2. Loop Basics
   a. While
       - Create an integer variable i with value of 5.
       - Create a while loop that runs so long as i is less than or equal to 15.
       - Each loop iteration, output the current value of i then increment i by one.
 You out put should look like this:
 5
 6
 7
 8
 9
 10
 11
 12
 13
 14
 15
"""

i = 5
i
while i <= 15:
    print(i)
    i +=1

#   - Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0

while i <= 100:
    print(i)
    i += 1

#   - Alter your loop to count backwards by 5;s from 100 to -10

i = 100

while i >= -10:
    print(i)
    i -= 5

#   - Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.

i = 2

while i**2 < 1_000_000:
    print(i)
    i **=2

#   - Write a loop that uses print to create the output shown below:

i = 100

while i >= 5:
    print(i)
    i -= 5

"""
 b. For Loops
   i. Write some code that prompts the user foa number, then shoes a multiplication table up through 10 for that number.
        # For example, if the user enters 7, your program should output:
            # 7 x 1 = 7 
            # 7 x 2 = 14
            # 7 x 3 = 21
            # 7 x 4 = 28
            # 7 x 5 = 35
            # 7 x 6 = 42
            # 7 x 7 = 49
            # 7 x 8 = 56
            # 7 x 9 = 63
            # 7 x 10 = 70
"""

user_number = float(input("Please type a number "))

for i in range(1,11):
    print(f'{user_number} x {i} = {user_number * i}')

#   ii. Create a for loop that uses print to create the output shown below.

for i in range(1,10):
    print(str(i)*i)

""" 
c. break and continue
   i. Prompt the user for an odd number between 1 and 50.
     # Use a loop and a break statement to continue prompting the user if they enter invalid input. 
     # (Hint: use the isdigit method on strings to determine this).
     # Use a loop and the continue statement to ouput all the odd numbers between 1 and 50, except for the number the user entered.
"""

user_number  = "7"

user_number = input("Type an odd number between 1 and 50: ")

while True:
    if user_number.isdigit() and int(user_number) % 2 == 1 and (int(user_number) in list(range(1,51))):
       break
    user_number = input("Try Again. Type an odd number between 1 and 50: ") 

print(f'Number to skip is: {user_number}')

for n in range(1,51,2):
    if n == int(user_number):
        print (f'Yikes! Skipping number: {user_number}')
        continue
    print (f'Here is an odd number: {n}')

"""
 d. The input function can be used to prompt for input and use that input in your python code.
    Prompt the user to enter a positive number and write a loop that counts from 0 to that number.
    Hints: first make sure that the value the user entered is a valid number, also note that the input function  returns a string, so you'll need to convert this to a numeric type.
"""

user_number = input("Type an integer greater than 0: ")

while True:
    if user_number.isdigit() and int(user_number) > 0:
        break
    user_number = input("Try again. Type an integer greater than 0: ")

print('Your number is: '+ user_number)

for n in range(0,int(user_number)+1):
    print(n)


""" 
    e. Write a program that prompts the user for a positive integer.
       Next write a loop that prints out the numbers from the numbers from the number the user entered down to one.
"""

user_number = input("Type an integer greater than 1: ")

while True:
    if user_number.isdigit() and int(user_number) > 1:
        break
    user_number = input("Try Again. Type an integer greater than 1: ")

print("The number you choose was " + user_number)

for n in range(int(user_number),0, -1):
    print(n)

""" 
3.    Fizz Buzz
       One of the most common interview questions for entry-level programmers is the Fizzbuzz test.
       Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
           - Write a prorgam that prints the numbers from 1 to 100.
           - For multiples of three print "Fizz" instead of the number.
           - For multiples of five print "Buzz".
           - For numbers which are multiples of both three and five print "FizzBuzz". 
"""

for n in range(1,101):
    if n % 3 == 0 and n % 5 ==0:
        print("FizzBuzz")
        continue
    elif n % 5 == 0:
        print("Buzz")
        continue
    elif n % 3 == 0:
        print("Fizz")
        continue
    print(n)

""" 
4. Display a table of powers
    - prompt the user to enter an integer.
    - Display a table of squares and cubes from 1 to the valued entered.
    - Ask if the user wants to continue.
"""

user_number = input("\nWhat integer between 1 and 100 would you like to go up to? ")

while True:
    if user_number.isdigit() and int(user_number) >= 1 and int(user_number) <= 100:
        break
    else:
        user_number = input("Try Again. Type an integer between 1 and 100: ")

header = ('{:7}'.format('number') + "|" + '{:^9}'.format('squared') + "|" + '{:>6}'.format('cubed') )
border = ('{:7}'.format('------') + "|" + '{:^9}'.format('-------') + "|" + '{:>6}'.format('-----') )

def table_of_powers(user_number):
    print("\nHere is your table!\n")
    print(header)
    print(border)
    for n in range(1,int(user_number)+1):
        if n < 4:
            print('{:d}'.format(n) + '{:>8}'.format("| ") + '{:d}'.format(n ** 2) + '{:>9}'.format(" | ") + '{:d}'.format(n **3 ))
        elif n < 10 and n > 3:
            print('{:d}'.format(n) + '{:>8}'.format("| ") + '{:d}'.format(n ** 2) + '{:>8}'.format(" | ") + '{:d}'.format(n ** 3))
        elif n >= 10 and n < 32:
            print('{:d}'.format(n) + '{:>7}'.format("| ") + '{:d}'.format(n ** 2) + '{:>7}'.format(" | ") + '{:d}'.format(n ** 3))
        elif n >= 32 and n < 100:
            print('{:d}'.format(n) + '{:>7}'.format("| ") + '{:d}'.format(n ** 2) + '{:>6}'.format(" | ") + '{:d}'.format(n ** 3))
        elif n >= 100:
            print('{:d}'.format(n) + '{:>6}'.format("| ") + '{:d}'.format(n ** 2) + '{:>5}'.format(" | ") + '{:d}'.format(n ** 3))

table_of_powers(user_number)

"""
5. Convert given number grades into letter grades.
    - prompt the user for a numerical grade from 0 to 100
    - Display the corresponding letter grade.
    - Prompt the user to continue.
    - Assume that the user will enter valid integers for the grades.
    - The application should only continue if the user agrees to.
    - Grade Ranges:
        A: 100 - 88
        B: 87 - 80
        C: 79 - 67
        D: 66 - 60
        F: 59 - 0
"""

while True:
    user_grade = input("Please enter a grade between 0 and 100: ")
    user_grade = int(user_grade)
    if user_grade >= 88:
        grade = "A"
        print(f'Grade: {grade}')
    elif user_grade >= 80:
        grade = "B"
        print(f'Grade: {grade}')
    elif user_grade >= 67:
        grade = "C"
        print(f'Grade: {grade}')
    elif user_grade >= 60:
        grade = "D"
        print(f'Grade: {grade}')
    elif user_grade >= 0:
        grade = "F"
        print(f'Grade: {grade}')
    more_grades = input("Would you like to continue? Y/N ")
    if more_grades == 'N':
        break

""" 
6. Create a list of dictionaries where each dictionary represents a book that you have read.
Each dictionary in the list should have the keys title, austhor, and genre.
Loop through the list and print out information about each book.
"""
books = [{'title': 'Where the Crawdads Sing', 'author': 'Delia Owens', 'genre': 'fiction'}, 
         {'title': 'Sharp Objects', 'author': 'Gillian Flynn', 'genre': 'True Crime'},
         {'title': 'Order of the Phoenix', 'author': 'J.K Rowling','genre': 'fiction'}]

user_genre = input("Select a genre: ")

for book in books:
    if book['genre'] == user_genre:
        print(book['title'])




