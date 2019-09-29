# Make a file named pandas_series.py or pandas_series.ipynb for the following exercises.

import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

# 1. Use pandas to create a series from the following data:

fruits = [
    "kiwi", 
    "mango", 
    "strawberry", 
    "pineapple", 
    "gala apple", 
    "honeycrisp apple",
    "tomato",
    "watermelon",
    "honeydew",
    "kiwi",
    "kiwi",
    "kiwi",
    "mango",
    "blueberry",
    "blackberry",
    "gooseberry",
    "papaya" 
    ]

# a. Name a variable that holds the series fruits.

fruits = pd.Series(fruits)

# b. Run .describe() on the series to see what describe return for a series of strings.

fruits.describe() 

"""
    describe let's us know: 

    fruits.describe()...
    count       17
    unique      13
    top       kiwi
    freq         4
    dtype: object
"""
# c. Run the code necessary to produce only the unique fruit names.

fruits.unique()

# d. Determine how many times each value occurs in the series.

fruits.value_counts()

# e. Determine the most frequently occuring fruit name from the series.

count_fruits = fruits.value_counts()

count_fruits[count_fruits == count_fruits.max()]

#  f. Determine the least frequently occuring fruit name from the series.

count_fruits = fruits.value_counts()

count_fruits[count_fruits == count_fruits.min()]

# g. Write the code to get the longest string from the fruits series.

max_string = fruits.str.len().max()
string_length = fruits.str.len()

fruits[string_length == max_string]

min_string = fruits.str.len().min()

fruits[string_length == min_string]

# h. Find the fruit(s) with 5 or more letter in the name.

fruits[string_length >= 5]

# i. Capitalize all the fruit strings in the series.

fruits.str.upper()

# j. Count the letter "a" in all the fruits (use string vectorization)


a_count = fruits.apply(lambda word : word.count("a"))
a_count = fruits.str.count("a")
pd.DataFrame(list(zip(fruits, a_count)),columns = ['fruits','a_count'])

# k. Output the number of vowels in each and every fruit.

vowels = list("aeiou")

def count_vowels(word):
    count = 0
    for letter in word:
        if letter in list("aeiou"):
            count += 1
    return count

count_vowels("aeiou")

vowel_count = fruits.str.count('[aeiou]')

pd.DataFrame(list(zip(fruits,vowel_count)), columns = ['fruits','vowel_count'])


# l. use the .apply method and a lamba function to find the fruit(s) containing two or more "o" letters in the name.
o_greater_or_equal_to_two =fruits[fruits.apply(lambda word : word.count("o")>=2)]
o_greater_or_equal_to_two

# m. Write the code to get only the fruits containing "berry" in the name

berry = fruits.str.findall('berry', flags = re.IGNORECASE)

## match object research
"""
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
    print(match.group())  ## 'b@google'
match = re.search(r'\d\d\d', 'p123g')
match.group()

"""
fruits[fruits.str.find("berry") > -1]

# n. Write the code to get only the fruits containing "apple" in the name.

fruits[fruits.str.find("apple") > -1]

# o. Which fruit has the highest amount of vowels?

fruits[vowel_count == max(vowel_count)]

# 2. Use pandas to create a Series from the following data:

money = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
money = pd.Series(money)

# What is the data type of the series money? Money is dtype: Object (Pandas Datatype), It is a string datatype in Python.

# What is the maximum value of money?

money_float = money.str.replace('$',"").str.replace(',',"").astype(float)

max(money_float)

# What is the minimum value of money?

min(money_float)

# Bin the data into 4 equally sized intervals and show how many values fall into each bin.
index = pd.Index(money_float)
index.value_counts()

bins_four = money_float.value_counts(bins = 4)

# Plot a histogram of the data. Be sure to include a title and axis labels.

plt.hist(money_float)

# 3. Use pandas to create a Series from the following exam scores: 
exam_scores = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]

exam_scores = pd.Series(exam_scores)

# What is the minimum exam score? The max, mean, and median?
exam_scores.describe()

# Convert each of the numbers above into a letter grade. For example, 86 should be a B and 95 should be an 'A'

def letter_grade(grade):
        if grade >= 90.0:
            return "A"
        elif grade >=80.0:
            return "B"
        elif grade >=70.0:
            return "C"
        else:
            return "F"

exam_letters = exam_scores.apply(letter_grade)

# Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.

curve = 100 - exam_scores.max()
curved_scores = curve + exam_scores

# Use pandas to create a Series from the following string

letters = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'

letters = pd.Series(list(letters))

# What is the most frequently occuring letter?

letters.value_counts()[letters.value_counts() == letters.value_counts().max()]
letters.value_counts()[letters.value_counts() == letters.value_counts().max()]

# How many vowels are in the list?

letters.apply(count_vowels).sum()

# How many consonants are in the list?

len(letters) - letters.apply(count_vowels).sum()

# Create a series that has all of the same letters, but uppercased

letters.str.upper()

# Create a bar plot of the frequencies of the most 6 most frequently occuring letters.

top_seven_letters = letters.value_counts().head(7).sort_index()

top_seven_letters.plot.bar(rot=0)
