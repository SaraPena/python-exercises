# Write some Python code, that is, variables and operators,
# to describe the following scenarios. Do not worry about
# the real operations to get the values, the goal of these
# exercises is to understand how real world conditions
# can be represented with code

# You have rented some movies for your kids:
# The Little Mermaid (for 3 days),
# Brother Bear (for 5 days, they love it),
# Hercules (for 1 day, you don't know if they're going to like it).
# If price for a movie is 3 dollars, how much will you have
# to pay?

rental_price_per_day = 3.00
little_mermaid_days = 3
brother_bear_days = 5
hercules_days = 1
pay = 0
pay += little_mermaid_days * rental_price_per_day
pay += brother_bear_days * rental_price_per_day
pay += hercules_days * rental_price_per_day

# Suppose you're' working as a contractor for 3 companies: Google,
# Amazon and Facebook, they pay you a different rate per hour.
# Google pays 400 dollars per hour, Amazon 380 and Facebook 350.
# How much will you recieve in payment for this week? You worked 10
# hours for Facebook, 6 hours for Google and 4 hours for Amazon.

Amazon = [380, 4]
Google = [400, 6]
Facebook = [350, 10]
pay = Amazon[0] * Amazon[1] + Google[0]*Google[1] + Facebook[0]*Facebook[1]
print (pay)

# A student can be enrolled to a class only if the class is not full
# and the class schedule does not conflict with her current schedule
class_full = True
schdeule_conflict = False

class_full and schdeule_conflict

# A product can be applied only if people buy more than 2 items,
# and the offer has not expired. Premium members do not need to buy
# a specific amount of products.

Premium_Member = True
Product_amount = 1

Premium_Member = False
Product_amount = 2

# Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'

# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters

length_5 = len(password) >= 5
length_5

# the username must be no more than 20 characters.

username_20 = len(username) <= 20
username_20

# the password must not be the same as the username.
not_same = password != username
not_same

# BONUS neither the username or password can start or end with whitespace.
no_white_space = (username[0] != " " and username[-1] != " ") and (password[0] != " " and password[-1] != " ")
no_white_space

