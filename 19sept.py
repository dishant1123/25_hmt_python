# sql  : 
"""

emp_id  name  salary 
 
1       guru   900000
2       yash   800000 
3       het    80000
4       ved    1000000 
5       lalit  50000

fetch : first  3 rows only  
offset : last 2 row only  
"""

# pandas :  pip install  pandas 
"""
Introduction
Think pandas as an extension of numpy

In numpy we could just have a single type of data in an array. Pandas solve that problem. How? We will see it once we open our today's first file.

Pandas can do everything what we used to do in SQL but, in an easier way. Hence, many prefers to use pandas over SQL plus, pandas has its own performance benefit which we will see later.

While working with offline editors like vs code or pycharm, we need to install pandas first using pip install pandas command however, it comes pre-installed in google colab so we just need to import it. Usually we import it like: import pandas as pd


dataframes : df 

"""

import pandas as pd

df = pd.read_csv("mckinsey.csv")
# print(df)

"""a=df.head()   # first  5 row display 
print(a)
"""
"""b=df.head(15)   # first  25  row  display 
print(b)
"""

"""c=df.tail()   # last 5 row  display ()
print(c)"""

"""
d =df.tail(10)   # last 10  row  display 
print(d)
"""

"""df.shape 
row,col = df.shape
print(row)
print(col)
"""

# create dataframe :   

df1=pd.DataFrame([
    ["guru",20,900000],
    ["yash",19,800000],
    ["het",18,800000],
    ["ved",17,1000000],
    ["mayuri",19,300000]],columns=["name","age","salary"])
print(df1)