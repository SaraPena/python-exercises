# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())


# Exercise 1 - Rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [fruit.upper() for fruit in fruits]
uppercased_fruits

# Exercise 2 - Create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
capitalized_fruits

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

## Learning through trial and error --below-- ##
help(pass)
vowels = ["a","e","i","o","u"]
output = ""
fruit = "apple"
for letter in fruit:
    if letter in vowels:
        output += letter.upper()
    else:
        output += letter
fruit
   
output

# Exercise 3 - Answer to submit
fruits_with_more_than_two_vowels = []
for fruit in fruits:
    c = 0
    for letter in fruit:
        for vowel in vowels:
            if letter == vowel:
                c += 1
    if c > 2:
        fruits_with_more_than_two_vowels.append(fruit)

fruits_with_more_than_two_vowels
        



        