#  missing value  : 

import pandas as pd

data = {
    "name" :["lalit","het","amit","smit","jalay","priya",None,"jalay"],
    "age" :[25,30,20,None,35,45,23,35],
    "city":["chennai","delhi","mumbai","bangalore",None,"kolkata","gandhinagar",None],
    
}

df =pd.DataFrame(data)
# print(df)

# check missing  in your  data :  

# isnull()  :  it will return boolean value True/False 
"""print("find missing value in your data",df.isnull())
print("totlal missing  value in your data :\n",df.isnull().sum())
"""

# dropna()  :  it will drop the missing value row. 

"""
print("drop  missing value  of row  :\n",df.dropna()) 

"""

# fillna():  it will fill the missing value with some value. 

# print(df)
"""
print("fill the missing value with some value :\n",df.fillna({
    "name":"unknown","age":0,"city":"unknown"}))
"""

# remove duplicate : 

# print("remove duplicate value :\n",df.drop_duplicates())