# Make a file named pandas_series.py or pandas_series.ipynb for the following exercises.

import pandas as pd
import numpy as np

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

fruits[fruits.apply(lambda word : word.count("a"))]


# k. Output the number of vowels in each and every fruit.

vowels = list("aeiou")

def count_vowels(word):
    count = 0
    for letter in word:
        if letter in list("aeiou"):
            count += 1
    return count

count_vowels("aeiou")

fruits.str.count('[aeiou]')

fruits[fruits.apply(count_vowels) > 0]
fruits[fruits.str.count('[aeiou]')>=0]



# l. use the .apply method and a lamba function to find the fruit(s) containing two or more "o" letters in the name.
fruits[fruits.apply(lambda word : word.count("o")) >= 2]

