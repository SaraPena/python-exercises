#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

# Use the following code for the questions below:

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[2]:


# 1. How many negative numbers are there?

# I used shape property to answer this
a[a<0].shape


# In[3]:


#2. How many positive numbers are there?

# I used shape property to answer this
a[a>0].shape


# In[4]:


# 3. How many even positive numbers are there?

# I used shape property to answer this
a[(a % 2 == 0) & (a > 0)].shape


# In[ ]:


# 4. If you were to add 3 to each data point, how many positive numbers would there be?

# I assigned the new value to a different varible so that the adjustment would not effect remaining exercises
b = a + 3
b[a % 2 == 0].shape


# In[ ]:


# 5. If you squared each number, what would the new mean and standard deviation be?

# I assigned the new value to a different varible so that the adjustment would not effect remaining exercises
c = a ** 2
c.mean()
c.std()


# In[ ]:


# 6. A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the center of the data is at 0. 
# This is done by subtracting the mean from each data point. Center the data set.

# First I used the mean function to find the current mean of a
a.mean()

# Then created a new varible to hold the adjusted centered mean
centered = a - a.mean()
centered.mean()


# In[ ]:


# 7. Calculate the z-score for each data point. Recall that the z-score is given by: z = x - mu / stddev

# used the mean and standard deviation functions to calculate the z score
z_score = (a - a.mean())/a.std()


# In[ ]:


# 8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and 
# add your solutions.


# In[1]:


import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:


# In[ ]:


# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

# assign variable
sum_of_a = sum(a)


# In[ ]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

# assign variable
min_of_a = min(a)


# In[ ]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

# assign variable
max_of_a = max(a)


# In[ ]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

# assign variable
mean_of_a = sum(a)/len(a)


# In[ ]:


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers
# in the above list together

# assign variable to start at 1 because starting at 0 will make product 0
product_of_a = 1
# use a loop to muliply each number by the next number in the list
for n in a:
    product_of_a = product_of_a * n


# In[ ]:


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared 
# like [1, 4, 9, 16, 25...]

# use a list comprehension to square each number in the list
squares_of_a = [n**2 for n in a]


# In[ ]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

# use a list comprehension to find numbers where the remainder when dividing by 2 equals 1 in the list
odds_in_a = [n for n in a if n % 2 == 1]


# In[ ]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

# use a list comprehension to find numbers where the remainder when dividing by 2 equals 0 in the list
evens_in_a = [n for n in a if n % 2 == 0]


# In[ ]:


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of
# squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]
# note: the answers to what it would take to find the sum, min, max, average, product, and list of squares are given below


# In[ ]:


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

# create a new variable for the array of b
npb = np.array(b)
# use numpy function sum
npb.sum()


# In[ ]:


# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1]) 

# use numpy function min
npb.min()


# In[ ]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

# use numpy function max
npb.max()


# In[ ]:


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

# use numpy function mean
npb.mean()


# In[ ]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

# use numpy function prod
npb.prod()


# In[ ]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

# assign new varible to hold squares to not effect data set
squares_npb = [npb ** 2]


# In[ ]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

# use comparison opperators to index into the array
npb[npb % 2 == 1]


# In[ ]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

# use comparison opperators to index into the array
npb[npb % 2 == 0]


# In[ ]:


# Exercise 9 - print out the shape of the array b.

# use shape property, shows 2 rows by 3 columns
npb.shape


# In[ ]:


# Exercise 10 - transpose the array b.

# exobrain https://www.w3resource.com/numpy/manipulation/transpose.php
# use numpy function transpose
npb.transpose()


# In[ ]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

# assign to new variable, use reshape function
# exobrain https://www.geeksforgeeks.org/python-flatten-a-2d-numpy-array-into-1d-array/
reshape_npb = npb.reshape([1, 6])


# In[ ]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

# use reshape function
reshape2_npb = npb.reshape([6, 1])


# In[2]:


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

# convert "c" to array
c = np.array(c)

# min, max, sum, and prod functions
c.min()
c.max()
c.sum()
c.prod()


# In[ ]:


# Exercise 2 - Determine the standard deviation of c.

# use std dev function
c.std()


# In[ ]:


# Exercise 3 - Determine the variance of c.

# exobrain https://numpy.org/doc/stable/reference/generated/numpy.var.html
# use var function
c.var()


# In[3]:


# Exercise 4 - Print out the shape of the array c

# use print with shape property
print(c.shape)


# In[ ]:


# Exercise 5 - Transpose c and print out transposed result.

# use transpose function and print
print(c.transpose())


# In[7]:


# Exercise 6 - Get the dot product of the array c with c. 

# exobrain https://www.tutorialspoint.com/numpy/numpy_dot.htm
# assign new variable, use dot function

dotc = np.dot(c, c)


# In[3]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# assign c transposed to variable
ctrans = c.transpose()
# find result of c times c transposed and assign result to new variable
multc = np.multiply(ctrans, c)
# sum result with sum function
multc.sum()
multc


# In[8]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed.

# Answer should be 131681894400.
ctrans = c.transpose()
# get product of c times c transposed
multc2 = np.prod(c * ctrans)


# In[8]:


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]


# In[10]:


# Exercise 1 - Find the sine of all the numbers in d

# use sin function
np.sin(d)


# In[11]:


# Exercise 2 - Find the cosine of all the numbers in d

# use cos function
np.cos(d)


# In[12]:


# Exercise 3 - Find the tangent of all the numbers in d

# use tan function
np.tan(d)


# In[16]:


# Exercise 4 - Find all the negative numbers in d

# convert "d" to array
d = np.array(d)
# use comparison opperator in index into array
d[d < 0]


# In[17]:


# Exercise 5 - Find all the positive numbers in d

# use comparison opperator in index into array
d[d > 0]


# In[24]:


# Exercise 6 - Return an array of only the unique numbers in d.

# use unique function 
setd = np.unique([d])


# In[25]:


# Exercise 7 - Determine how many unique numbers there are in d.

# use shape property to find how many unique numbers are in the set
setd.shape


# In[26]:


# Exercise 8 - Print out the shape of d.

# use print with shape property
print(setd.shape)


# In[27]:


# Exercise 9 - Transpose and then print out the shape of d.

transd = c.transpose()
print(transd.shape)


# In[30]:


# Exercise 10 - Reshape d into an array of 9 x 2

# reshape function
reshape_d = d.reshape([9, 2])


# In[ ]:


# 9. For even more practice, clone https://github.com/rougier/numpy-100, make your own repo called numpy-100, 
# and then commit and push your solutions to your own repo.

