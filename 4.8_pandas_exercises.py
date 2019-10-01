#!/usr/bin/env python
# coding: utf-8

# # pandas_exercises

# Create a notebook or python script named `pandas_exercises` to do your work for this exercise.
# 
# For the following exercises, you'll need to load several datasets using the `pydataset` library. (If you get an error when trying to run the import below use `pip` to install the `pydataset` package.)

# In[238]:


from pydataset import data


# When the instructions say to load a dataset, you can pass the name of the dataset as string to the `data` function to load the dataset. You can also view the documentation for the data set by passing the `show_doc` keyword agrument.

# In[239]:


mpg = data('mpg') #load the dataset and store it in a variable 
data('mpg',show_doc=True) #view the documentation for the dataset.


# Use pandas to convert the following list to a numeric series:

# In[2]:


import pandas as pd


# In[30]:


money = pd.DataFrame({'amount': ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']})
money['amount']= money['amount'].str.replace('$','').str.replace(',','').astype(float)
money.info()


# 1. Load the `mpg` dataset. Read the documentation for it, and use the data to answer these questions.
#     * On average, which manufacturer has the best miles per gallon?

# In[240]:


import math
import pandas as pd
import numpy as np
import matplotlib as plt
mpg = data('mpg')


# In[241]:


# mpg['average_mileage'] = (mpg.hwy+mpg.cty)/2
# mpg['average_mileage']
# mpg[['manufacturer','average_mileage']]

avg_city_mileage = mpg.groupby('manufacturer').cty.mean()
avg_highway_mileage = mpg.groupby('manufacturer').hwy.mean()

((avg_city_mileage + avg_highway_mileage)/2).sort_values(ascending = False).head(1)




# * How many different manufacturers are there?

# In[242]:


mpg['manufacturer'].nunique()


# * How many different models are there?

# In[243]:


mpg['model'].nunique()


# - Do automatic or manual cars have better miles per gallon?

# In[244]:


mpg['transmission'] = mpg['trans'].str.split("(").str[0]
mpg['average_mileage'] = (mpg['hwy'] + mpg['cty'])/2

mpg[['transmission','average_mileage']].groupby('transmission').mean().sort_values('average_mileage', ascending = False)


# #### 2. Joining and Merging
# 
# Copy `users` and `roles` dataframes. What to you think a `right` join would look like? An `outer` join? What happens if you drop the foreign keys from the dataframes and try to merge them?

# In[245]:


users = pd.DataFrame({
        'id' : [1, 2, 3, 4, 5, 6],
        'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
        'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
roles = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'name': ['admin', 'author', 'reviewer', 'commenter']
})


# In[246]:


users


# In[247]:


roles


# In[248]:


pd.merge(users, roles, left_on = 'role_id', right_on = 'id', how = 'right')


# In[249]:


pd.merge(users, roles, left_on = 'role_id', right_on = 'id', how = 'outer')


# In[250]:


pd.merge(users, roles, how = 'right')


# In[251]:


pd.merge(users, roles, how = 'outer')


# In[252]:


pd.merge(users, roles, how = 'left')


# 3. Getting data from SQL databases
# 
#     a. Create a function named `get_db_url`. It should accept a username, hostname, password, and database name and return a url formated like in the examples in this lesson.

# In[253]:


from env import host, user, password
def get_db_url(user, host, password, database_name):
    url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
    return url


#    b. Use your function to obtain a connection to the `employees` database.

# In[254]:


employees_database_connection = get_db_url(user, host, password, 'employees')


# c. Once you successfully run a query:
# - Intentionally make a typo in the database url. What kind of error message do you see?

# In[255]:


# url = get_db_url(user, host, password, 'test')
url = get_db_url(user, host, password, 'employees')


# In[256]:


pd.read_sql('SELECT * FROM employees LIMIT 5', url)


# - Intentionally make an error in your sql query. What does the error message look like?

# In[257]:


pd.read_sql('SELECT * FROM test LIMIT 5', url)


# d. Read the `employees ` and `titles` tables into two separate dataframes.

# In[258]:


employees_table = pd.read_sql('SELECT * FROM employees', url)
employees_table


# In[259]:


title_table = pd.read_sql('SELECT * FROM titles', url)
title_table


# ### e. Visualize the number of employees with each title

# In[260]:


title_table_count = pd.read_sql('SELECT title, count(*) as amount FROM titles GROUP BY title', url)
title_table_count.plot.bar(x = 'title')


# ### f. Join the employees and titles dataframes together.

# In[261]:


employees_titles = pd.merge(employees_table, title_table, left_on = 'emp_no', right_on = 'emp_no', how = 'left')


# ### g. Visualize how frequently employees change titles.

# In[262]:


employees_titles.head(3)


# In[263]:


employees_titles.describe()


# In[281]:


employees_titles.groupby(['emp_no']).title.count().sort_values(ascending=False)


# In[264]:


employees_titles.groupby('emp_no').title.count().plot.hist()


# ### h. for each title, find the hire date of the employee that was hired most recently with that title

# In[290]:


# employees_titles[['title','from_date']]
employees_titles.info()


# In[361]:


# s = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000'] * 1000)
# s.head()
# pd.to_datetime(s,infer_datetime_format=True)
employees_titles['hire_date'] = pd.to_datetime(employees_titles['hire_date'],infer_datetime_format=True)
#employees_titles[employees_titles['hire_date'] == employees_titles['hire_date'].max()]
#title_hire_date = employees_titles.groupby(['title','hire_date']).hire_date.max()

employees_titles.groupby('title').hire_date.max()


# ### i. Write the code necessary to create a cross tabulation of the number of titles by department. (Hint: this will involve a combination of SQL and python/pandas code)

# In[365]:


url = get_db_url(user, host, password, 'employees')
employees_titles_departments = pd.read_sql("SELECT * FROM titles LEFT JOIN dept_emp using (emp_no) LEFT JOIN departments using (dept_no) WHERE dept_emp.to_date = '9999-01-01' and titles.to_date = '9999-01-01'", url)
# employees_titles_departments.head()


# In[370]:


employees_titles_departments.head()
pd.crosstab(employees_titles_departments.dept_name, employees_titles_departments.title, margins = True)


# ## 4. Use your get_db_url function to help you explore the data from the `chipotle` database. Use the data to answer the following questions:

# In[265]:


url = get_db_url(user, host, password, 'chipotle')


# In[266]:


chipotle = pd.read_sql('SELECT * FROM orders', url)
chipotle


# ###  What is the total price for each order?

# In[267]:


type(chipotle)


# In[268]:


chipotle['item_price'] = chipotle['item_price'].str.replace('$', '')
# chipotle['item_price'].describe()
# chipotle['item_price'] = chipotle['item_price'].astype(float)
# chipotle.describe


# In[269]:


# chipotle['item_price'].describe()
chipotle['item_price'] = chipotle['item_price'].astype(float)
# chipotle.describe


# In[270]:


chipotle.dtypes


# In[271]:


chipotle.info()


# In[272]:


chipotle.groupby('order_id').item_price.sum()


# In[273]:


chipotle.head()


# In[274]:


(chipotle.groupby('item_name').quantity.sum().sort_values(ascending = False)).head(3)


# - Which item has produced the most revenue?

# In[275]:


chipotle['revenue'] = chipotle['quantity'] * chipotle['item_price']


# In[276]:


chipotle.head()


# In[282]:


chipotle.groupby('item_name').revenue.sum().sort_values(ascending=False).head()


# In[ ]:




