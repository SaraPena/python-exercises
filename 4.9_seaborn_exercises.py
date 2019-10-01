# Create a file named 4.9_seaborn_exercises.py for this exercise

# Use the iris database to answer the following questions:

import numpy as np
import pandas as  pd
import matplotlib.pyplot as plt 

import seaborn as sns 

iris = sns.load_dataset('iris')
type(iris)

# 1. What does the distribution of petal lengths look like?
sns.distplot(iris.petal_length)

# 2. Is there a correlation between petal length and petal width?
iris.corr()
r = iris.corr().loc['petal_length', 'petal_width']

sns.relplot(data = iris, x = 'petal_length', y = 'petal_width')

plt.text(1.5, 2, f'r = {r:.2}')
# Would it be reasonable to predict speces based on sepal width and sepal length?

sns.relplot(data = iris, x = 'sepal_width', y = 'sepal_length', hue = 'species')

# Which features would be best used to predict species?

sns.relplot(data = iris, x = 'petal_length', y = 'petal_width')

sns.pairplot(data=iris,hue = 'species')

# 1. Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set. Use pandas to group the data by dataset column, and calculate summary statistics for each dataset.
    # What do you notice?
    # Plot the x and y values in the anscombe data. Each dataset should be a separate column.

anscombe = sns.load_dataset('anscombe')
anscombe.groupby('dataset').mean()
anscombe.groupby('dataset').count()
anscombe.groupby('dataset').median()
anscombe.groupby('dataset').std()
anscombe.groupby('dataset').describe()

sns.relplot(data = anscombe, x = 'x', y = 'y', col = 'dataset')

# 2. Load the InsectSprays dataset and read it's documentation. Create visualizations to answer the following questions:

from pydataset import data

data('InsectSprays', show_doc= True)

InsectSprays = data('InsectSprays')

sns.boxplot(data = InsectSprays, y = 'count', x = 'spray', hue = 'spray' )
sns.boxplot(data = InsectSprays, y = 'count', x = 'spray')

plt.legend(loc = 'upper right', bbox_to_anchor = (.8,1))

# 3. Load the swiss dataset and read it's documentation. Create visualization to answer the following questions:

data('swiss', show_doc = True)

swiss = data('swiss')

# Create an attribute named is_catholic that holds a boolean value of whether or not the province is Catholic. (Choose a cutoff point for what constitutes Catholic.)
sns.distplot(swiss.Catholic)

swiss['is_catholic'] = swiss['Catholic'] > 50 
swiss.Catholic.apply(lambda n: 'Catholic' if n > 50 else 'Not Catholic')

sns.boxplot(data = swiss, y = 'Fertility', x = 'is_catholic')

swiss.corr()

sns.relplot(data = swiss, x = 'is_catholic', y = 'Fertility', hue = 'is_catholic')

group_is_catholic = swiss.groupby('is_catholic').count()['Fertility']

group_is_catholic.plot.bar(x = 'is_catholic')

# What measure corretlates most strongly with fertility?

swiss.corr().Fertility

sns.relplot(data = swiss, x = 'Education', y = 'Fertility', hue = 'is_catholic')

# Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 most popular items and the revenue produced by each.
from env import host, user, password

def get_url(host, user, password, database):
    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    return url

url = get_url(host, user, password, 'chipotle')

chipotle = pd.read_sql('SELECT * FROM orders', url)
chipotle.head()
chipotle.info()

chipotle['item_price'] = chipotle['item_price'].str.replace('$',"").astype(float)
chipotle.info() #check that the item_price is a float type

chipotle.groupby('item_name').sum()

(chipotle.groupby('item_name')
 .item_price.sum()
 .sort_values(ascending = False)
 .head(4)
 .plot.bar(rot=0))

top_four_items = (chipotle.groupby('item_name')
 .sum()
 .sort_values(by = 'quantity', ascending = False)
 .drop(columns = ['id','order_id'])
 .head(4)
 .reset_index()
)

sns.barplot(data = top_four_items, y = 'item_price', x = 'item_name')

plt.ylabel('revenue')

# 5. Load the sleepstudy dataset and read it's documentation.
#    Use Seaborn to create a line chart of all the individual subject's reaction times and a more prominent line showing the average change in reaction time.


sleepstudy = data('sleepstudy')
sleepstudy.info()

sleepstudy.Subject  = 'subject_' + sleepstudy.Subject.astype(str)


plt.figure(figsize = (12,12))
sns.lineplot(data = sleepstudy, x = 'Days', y = 'Reaction', hue = 'Subject',alpha = .3, palette = 'vlag')
sns.lineplot(data = sleepstudy, y = 'Reaction', x = 'Days', color = 'white')


sum_reactions_by_days = sleepstudy.groupby('Days').Reaction.sum()
number_of_subjects = sleepstudy['Subject'].nunique()

average_change = sum_reactions_by_days/number_of_subjects

sns.lineplot(data=sleepstudy, x = 'Days', y = 'Reaction', hue = 'Subject', color = 'Blues')
sns.lineplot(data = average_change, color = 'Red')

# sns.lineplot(data=sleepstudy[['Reaction', 'Subject']]

# #Make a data frame
# df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21), 'y4': np.random.randn(10)+range(6,16), 'y5': np.random.randn(10)+range(4,14)+(0,0,0,0,0,0,0,-3,-8,-6), 'y6': np.random.randn(10)+range(2,12), 'y7': np.random.randn(10)+range(5,15), 'y8': np.random.randn(10)+range(4,14), 'y9': np.random.randn(10)+range(4,14), 'y10': np.random.randn(10)+range(2,12) })
 
# # style
# plt.style.use('seaborn-darkgrid')
 
# # create a color palette
# palette = plt.get_cmap('Set1')
 
# # multiple line plot
# num=0
# for column in df.drop('x', axis=1):
#     num+=1
#     plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=1, alpha=0.9, label=column)
 
# # Add legend
# plt.legend(loc=2, ncol=2)
 
# # Add titles
# plt.title("A (bad) Spaghetti plot", loc='left', fontsize=12, fontweight=0, color='orange')
# plt.xlabel("Time")
# plt.ylabel("Score")


