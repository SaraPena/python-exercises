# Create a file named 4.5_import_exercises.py to do your work in.

"""
1.  Import and test 3 function from your functions exercise file.
    
    Your functions exercises are not currently in a file with a name that can be easily imported.
    Copy your functions exercises file and name the copy functions_exercises.py.
    To do this from the command line, from python exercises folder: cp 4.4_function_exercises.py functions_exercises.py
"""

# Import each function in a different way:

# Import the module and refer to the function with the .syntax.


#import functions_exercises #uncomment to run

#discount_amount = functions_exercises.apply_discount(100,.2) #uncomment to run

#print(f'The amount you will pay for the sale item is ${discount_amount}0') #uncomment to run

#from functions_exercises import remove_vowels #uncomment to run

#sentence_with_vowels = "My cat's name is Charlie" #uncomment to run

#print(f'Remove vowels function with sentence: My cat\'s name is Charlie.\nRemove vowels: {sentence_with_vowels}') #uncomment to run


# use from and give the function a different name.

#from functions_exercises import apply_discount as sale #uncomment to run

#price = sale(100,.2) #uncomment to run
#print(f'The amount you will pay for the sale item is ${price}0.') #uncomment to run


"""
For the following exercises, read about and use the intertools module from the standard library to help you solve the problem.
"""
#   1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

import itertools as i

len(list(i.permutations('ABC123',6)))

len(list(i.combinations('abcd',2)))

import json as j

with open("profiles.json", "r") as profiles:
    data = j.load(profiles)


def total_number_of_users(x):
    return len(x)

total_number_of_users(data)


def active_users(x):
    s = []
    for i in data:
        if i['isActive']:
            s.append(True)
    return len(s)

active_users(data)

def inactive_users(x):
    s = []
    for i in data:
        if i['isActive'] != True:
            s.append(False)
    return len(s)

inactive_users(data)

def grand_total_of_balances(x):
    s = []
    t = 0
    for i in data:
        s.append(i['balance'])
    return s 

l = grand_total_of_balances(data) # list of balances from dictionaries in data.
s = [] #new empty list to append balance without '$'

for b in l:
    b = b.replace('$',"").replace(',',"")
    s.append(b)
s


assert True == False
assert True == True