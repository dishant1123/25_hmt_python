import pandas as pd
import numpy as np


df =pd.read_csv("mckinsey.csv")
# print(df)

temp =df.set_index("country")
# print(temp)

india =temp.loc["India"]
# print(india)

# prit only  specific  year  : 

yr = df.loc[df["year"]==2007]
# print(yr)

# drop  :  delete  table row  or  col 

# a= df.drop(2,axis=0)
# a=df.drop("year",axis=1)
a=df.drop(["year","population"],axis=1)
print(a)

# print  first 20  row  == >  2,3,4,6,8,10   ==>  row  delete  

b =df.drop([2,3,4,6,8,10]).head(20)
print(b)

# print last 20  row ==> 1701  1702  1703  1699  ==>  row  delete 

