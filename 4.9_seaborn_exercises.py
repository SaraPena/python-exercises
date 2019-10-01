# Create a file named 4.9_seaborn_exercises.py for this exercise

# Use the iris database to answer the following questions:

import numpy as np
import pandas as import import pd
import matplotlib.pyplot as plt 

import seaborn as sns 

iris = sns.load_dataset('iris')
type(iris)

# 1. What does the distribution of petal lengths look like?
sns.distplot(iris.petal_length)

# 2. Is there a correlation between petal length and petal width?
iris.corr()

sns.relplot(data = iris, x = 'petal_length', y = 'petal_width')

# Would it be reasonable to predict speces based on sepal width and sepal length?

sns.relplot(data = iris, x = 'sepal_length', y = 'sepal_width')

# Which features would be best used to predict species?

sns.relplot(data = iris, x = 'petal_length', y = 'petal_width')

# 1. Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set. Use pandas to group the data by dataset column, and calculate summary statistics for each dataset.
    # What do you notice?
    # Plot the x and y values in the anscombe data. Each dataset should be a separate column.

anscombe = sns.load_dataset('anscombe', show_doc = True)
anscombe.groupby('dataset').mean().describe()
anscombe.groupby('dataset').count()
anscombe.groupby('dataset').median()
anscombe.groupby('dataset').std()

sns.relplot(data = anscombe, x = 'x', y = 'y', col = 'dataset')

# 2. Load the InsectSprays dataset and read it's documentation. Create visualizations to answer the following questions:

from pydataset import data

data('InsectSprays', show_doc= True)

InsectSprays = data('InsectSprays')

sns.boxplot(data = InsectSprays, y = 'count', x = 'spray', hue = 'spray' )
plt.legend(loc = 'upper right', bbox_to_anchor = (.8,1))

# 3. Load the swiss dataset and read it's documentation. Create visualization to answer the following questions:

data('swiss', show_doc = True)

swiss = data('swiss')

# Create an attribute named is_catholic that holds a boolean value of whether or not the province is Catholic. (Choose a cutoff point for what constitutes Catholic.)

swiss['is_catholic'] = swiss['Catholic'] > 60 

swiss.corr()

sns.relplot(data = swiss, x = 'is_catholic', y = 'Fertility', hue = 'is_catholic')

group_is_catholic = swiss.groupby('is_catholic').count()['Fertility']

group_is_catholic.plot.bar(x = 'is_catholic')

# What measure corretlates most strongly with fertility?

swiss.corr()

sns.relplot(data = swiss, x = 'Education', y = 'Fertility', hue = 'is_catholic')

# Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 most popular items and the revenue produced by each.
