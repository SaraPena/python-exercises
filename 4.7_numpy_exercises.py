# Create a file named 4.7_numpy_exercises.py for this exercise.

# Use the following code for questions below:

import numpy as np
a = np.array([4, 10, 12, 23, -2, -2, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?
len(a)

(a < 0).sum()

# 2. How many positive numbers are there?

(a > 0).sum()

# 3. How many even positive numbers are there?

((a > 0) & (a % 2 ==0)).sum()

# 4. If you were to add 3 to each data point, how many positive numbers would there be?

(a+3 > 0).sum()

# 5. If you squared each number, what would the new mean and standard deviation be?

(a**2).mean()
(a**2).std()

# 6. A common statistical operation on a dataset is centering.
   # This means to adjust the data such that the center of the data is 0.
   # This is done by subtracting the mean from the each data point.
   # Center the data set.

 c = a - a.mean()
 c.mean()

# 7. Calculate the z-score for each data point. 

z_scores = (a-a.mean())/a.std()
z_scores

## More Numpy Practice

# numpy_exercises_part_1.py
# <script src="https://gist.github.com/ryanorsinger/c4cf5a64ec33c014ff2e56951bc8a42d.js"></script>

# Life w/o numpy to life with numpy

## Setup #1
a = list(range(1,11))
a

# Use python's built in functionality/operators to determine the following:

# Exercise 1 - Make a variable called sum_of_a to hold the sum of all numbers in the above list 'a'.

sum_of_a = sum(a)
sum_of_a

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list.

min_of_a = min(a)
min_of_a

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list.

max_of_a = max(a)
max_of_a

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above lise.
import math

mean_of_a = sum(a)/len(a)
mean_of_a

# Exercise  5 - Make a variable called product_of_a to hold the product of multiplying all the numbers in the above list together.

product_of_a = 1
for n in a:
    product_of_a *= n
product_of_a

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9,15, 25 ...]

squared_of_a = [n**2 for n in a]
squared_of_a

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers.

odd_in_a = [n for n in a if n % 2 == 1]
odd_in_a

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = [n for n in a if n % 2 == 0]
evens_in_a

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, product, and list of squared for this list of two lists.

b = [[3, 4, 5],[6, 7, 8]]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as variable. **Hint, you'll first need to make sure that "b" variable is a numpy array**

sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

b = np.array(b)
b.sum()

# Exercise 2 - refactor the following to use numpy.

min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])

min_of_b = b.min()

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.

max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

b.max()

# Exercise 4 - refactor the following using numpy to find the mean of b.

mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0])+len(b[1]))

b.mean()

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.

product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

product_of_b = b.prod()

# Exercise 6 - refactor the following to use numpy to find the list of squares.

squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_of_b = b**2

# Exercise 7 - refactor using numpy to determine the odds_in_b.

odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odds_in_b = b % 2 != 0 
odds_in_b = b[odds_in_b]

# Exercise 8 - refactor the following to use numpy to filter only the even numbers

evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 ==0):
            evens_in_b.append()

evens_in_b = b[b % 2 ==0]

# Exercise 9 - print out the shape of the array b.

b.shape

# Exercise 10 - transpose the array b.

b.transpose()
b.transpose().shape

# Exercise 11  - reshape the array to be a single list of 6 numbers. (1 x 6)

b.shape = (1,6)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

b.shape = (6,1)

### Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Hint, you'll first need to make sure that 'c' variable is a numpy arrary prior to using array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

c = np.array(c)

c.min()
c.max()
c.sum()
c.prod()

# Exercise 2 - Determine the standard deviation of c.

c.std()

# Exercise 3 - Determine the variance of c.

c.var()

# Exercise 4 - Print out the shape of the array c.

c.shape

# Exercise 5 - Transpose c and print out transposed result.
c_transposed = c.transpose()

print(c.transpose())

# Exercise 6 - Multiply c by the c-Transposed and print the result
c_c_transposed = c * c_transposed

print(c_c_transposed)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

c_c_transposed.sum()

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

c_c_transposed.prod()

## Setup 4

d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d.

import math

d = np.array(d)

np.sin(d)

# Exercise 2 - Find the cosine of all the numbers in d.

np.cos(d)

# Exercise 3 - Find the tangent of all the numbers in d.

np.tan(d)

# Exercise 4 - Find all the negative numbers in d

d[d < 0]

# Exercise 5 - Find all the positive numbers in d

d[d > 0]

# Exercise 6 - Return an array of only the unique numbers in d

np.unique(d)

# Exercise 7 - Determine how many unique numbers there are in d.

len(np.unique(d))

# Exercise 8 - Print out the shape of d.

print(d.shape) 

# Exercise 9 - Transpose and then print out the shape of d

transpose_d = d.transpose()

print(transpose_d.shape)

# Exercise 10 - Reshape d into an array of 9 x 2.

d.shape = (9, 2)
