# Create a file named 4.4_function_exercises.py for this exercise.
# After creating each function specified below, write the necessary code in order to test your function.

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string, False otherwise.


def is_two(x):
    """ 
    Take a one input and return True if the passed input is either the number or string 2, False otherwise.
    """
    if x == 2 or (str(x)).lower()== 'two':
        return True
    else:
        return False


is_two(2)
is_two("two")
is_two(4)
is_two("asjfofds")

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(x):
    """ 
    return True if the passed string is a vowel, False otherwise. 
    """
    if x.lower() in ["a","e","i","o","u"]:
        print(f'{x} is a vowel')
        return True
    elif len(x) > 1 or type(x) == int:
        print("please enter a single letter")
        return False
    else:
        print(f'{x} is not a vowel. {x} is a consonant')


# 3. Define a function named is_constant. It should return True if the passed string is a consonant, False otherwise. Use you is_vowel function to accomplish this.

def is_consonant(x):
    """ 
    return True if the passed string is a consonant, False otherwise. Use you is_vowel function to accomplish this.
    """
    if is_vowel(x) == True:
        return False
    elif len(x) > 1 or type(x) == int:
        return False


# 4. cap_if_consonant(word)

def cap_if_consonant(word):
    if is_consonant(word[0]):
        return word.capitalize()
    return word


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
 

def calculate_tip(tip,bill):
    if tip > 1 or tip < 0:
        print("Please select a tip amount between 0 and 1")
        pass
    elif type(tip) == str:
        print("Please select a tip amount between 0 and 1")
        pass
    elif bill <= 0:
        print("Please enter a bill amount greater than 0")
        pass
    else:
        tip_amount = bill*tip
        print("Tip Amount: $" +str(tip_amount))
        return tip_amount

user_bill = input("How much was the bill? $")
user_tip = input("How much would you like to tip between 0 and 1? ")

# 6. Define a function named apply_discount. 
#    It should accept a original price, and discount percentage, return the price after the discount is applied.

def apply_discount(price,discount_percentage):
    if discount_percentage > 1:
        discount_percentage = discount_percentage/100
        discount_amount = discount_percentage * price
        discount_price_of_item = price - discount_amount
        return discount_price_of_item
    elif discount_percentage < 0:
        return False
    else:
        discount_amount = discount_percentage * price
        discount_price_of_item = price - discount_amount
        return discount_price_of_item


# 7. Define a function named handle_commas. 
#    It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(x):
    """ Accept a string that is a number that contains commas in it as input, and return as number as output.
        1. if - want to check that input is string type, if false print "Please enter a string" return boolean False value
        2. else - reassign x to a copy with replace method to change commas to underscores. This will allow python to read the string as a number. Wrap the replace with int() to assign x to an int type. """
    if type(x) != str:
        print ("Please enter a string")
        return False
    else:
        x = float(x.replace(",",""))
        return x


# 8. Define a function named get_letter_grade. 
#    It should accept a number and return the letter grade associated with the number (A-F).
def get_letter_grade(x):
    if x >= 90:
        return "A"
    elif x < 90 and x >= 80:
        return "B"
    elif x < 80 and x >=70:
        return "C"
    elif x < 70:
        return "F"


# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(x):
    rv = "" # assign a new variable (rv - removed vowels) to an empty string ""
    for l in x:
        if l.lower() not in ["e", "a", "i", "o", "u"]:
            rv += l
    return rv
            
# 10. Define a function named normalize_name.
#     It should accept a string and return a valid python identifier, that is:
#       anything that is not a valid python identifier should be removed.
#       leading and trailing whitespace should be removed.
#       spaces should be replaced with underscores
#       for example:
#           Name will become name
#           First Name will become first_name
#           % Completed will become completed



