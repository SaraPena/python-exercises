import pandas as pd
from env import host, user, password

url = f'mysql+pymysql://{user}:{password}@{host}/employees'
df = pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50',url)

a = [1, 2, 3]
b = ['d', 'e', 'f']

c = list(zip(a,b))

pd.Series(c)

from pydataset import data

mpg = data('mpg')
mpg

example = pd.DataFrame({'fruits': ['kiwi', 'banana', 'mango']})
example

