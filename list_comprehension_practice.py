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

# Exercise 3 - Answer to Submit.
number_of_vowels = fruit.count("a") + fruit.count("e") + fruit.count("i") + fruit.count("o") + fruit.count("u")
if number_of_vowels > 2:
    print("has as LEAST two vowels")
else:
    print("has LESS than two vowels")

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if fruit.count("a") + fruit.count("e") + fruit.count("i") + fruit.count("o") + fruit.count("u") > 2]
fruits_with_more_than_two_vowels

# Exercise 4 - Make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

fruits_with_only_two_vowels = [fruit for fruit in fruits if fruit.count("a") + fruit.count("e") + fruit.count("i") + fruit.count("o")+ fruit.count("u") == 2]
fruits_with_only_two_vowels

# Exercise 5 - Make a list that contains each fruit with more than 5 characters.

fruits_more_than_five_characters = [fruit for fruit in fruits if len(fruit) > 5]
fruits_more_than_five_characters

# Exercise 6 - make a list that contains fruits that have less than 5 characters.
fruits_with_less_than_five_characters = [fruit for fruit in fruits if len(fruit) < 5]
fruits_with_less_than_five_characters

# Exercise 7 - Make a list that contains fruits that have exactly 5 character.
fruits_with_exactly_five_characters = [fruit for fruit in fruits if len(fruit) == 5]
fruits_with_exactly_five_characters

# Exercise 8 - Make a list containing the number of character in each fruit. Output would be [5, 4, 10, etc...]
number_of_characters_in_fruits = [len(fruit) for fruit in fruits]
number_of_characters_in_fruits

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a".
word = "hello"
Test = word.find("e") != -1
Test

fruits_with_letter_a = [fruit for fruit in fruits if fruit.find("a") != -1 ]
fruits_with_letter_a

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers.
even_numbers = [number for number in numbers if number % 2 == 0]
even_numbers

# Exercise 11 - Make a variable named odd_numbers that hold only the odd numbers.
odd_numbers = [number for number in numbers if number % 2 == 1]
odd_numbers

# Exercise 12 - Make a variable named positive_numbers that holds only positive numbers.
positive_numbers = [number for number in numbers if number > 0]
positive_numbers

# Exercise 13 - Make a variable named negative_numbers that holds only negative numbers.
negative_numbers = [number for number in numbers if number < 0]
negative_numbers

# Exercise 14 - Use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or numerals.
two_or_more_numerals = [number for number in numbers if abs(number) > 10 ]
two_or_more_numerals

# Exercise 15 - Make a variable named numbers_squared that contains the numbers with each element squared. Output is [4, 6, 9, 16, etc...]
numbers_squared = [number ** 2 for number in numbers]
numbers_squared

# Exercise 16 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five.
numbers_plus_5 = [number + 5 for number in numbers]
numbers_plus_5

# Exercise 17 - Make a variable named odd_negative_numbers that contains only the number that are both odd and negative.
odd_negative_numbers = [number for number in numbers if number < 0 and number % 2 == 1]
odd_negative_numbers


# BONUS Make a variable named "primes" that is a list containing prime numbers in the numbers list. *Hint* you may want to make or find a helper function to determine if a given number is prime or not.
primes = [number for number in numbers if number > 1]
primes

x = 4

def divisable(x):
    for n in range(2,x):
        if x % n !=0:
            return False
        else:
            return True
            break

primes = [number for number in numbers if divisable(number) == False and number > 1]
primes




        