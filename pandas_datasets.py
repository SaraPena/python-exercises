"""
For serveral of the following exercises, you'll need to
load several datasets using the pydataset library.
If you get an error when trying to run the import below,
use pip to install the pydataset package
"""

from pydataset import data

"""
When the instructions say to load a dataset,
you can pass the name of the dataset as a string 
to the data function to load the dataset. You can
also view the documentation for the data set by passing
the show_doc keyword argument.
"""
# data('mpg', show_doc = True) # view the documentation for the dataset
mpg = data('mpg') # load the dataset and store it in a variable

"""
All the datasets loaded from the pydataset library
will be pandas dataframes.
"""

# 1. Copy the code from the lsson to create a dataframe full of student grades.

import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas', 'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']
# randomly generate scores for each student for each subject.

math_grades = np.random.randint(low = 60, high = 100, size = len(students))
english_grades = np.random.randint(low = 60, high = 100, size = len(students))
reading_grades = np.random.randint(low = 60, high = 100, size = len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

#   a. Create a column named passing_english that indicates whether each student has a passing grade in english.

df['passing_english'] = df.english > 70
df

#   b. Sort the english grades by the passing english column. How are the duplicated handled? 

df.sort_values(by = 'passing_english')
    # Duplicates are handlies by the next highest grade, if all grades are equal they are sorted by Alpha name.

"""
    c.  Sort the english grades first by passing_english and then by student name.
        All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically.
        The same should be true for the students passing english. (HINT: you can pass a list to the .sort_values method) 
"""
df.sort_values(by = ['passing_english', 'name'])

#   d. Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did the last step.

df.sort_values(by = ['passing_english', 'english'])

#   e. Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.

df['overall_grade'] = (math_grades + english_grades + reading_grades)/3
df