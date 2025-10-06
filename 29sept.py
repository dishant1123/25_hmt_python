import pandas as pd
import numpy as np

"""
loc : explict index 
iloc : implicit index
"""
df =pd.read_csv("mckinsey.csv")
print(df)

cont =df["country"]
# print(cont)

# print(cont.loc[0])
# print(cont.loc[2 :5])  # loc : start  end  both included 
# print(cont.iloc[12 :17])   # end   ==> excluded 

# print(df.loc[2:5])
# print(df.loc[2:5,1:3])   #  not  poss  ==> slicing  in  row only 
# print(df.iloc[2:5,1:3])   #  last row  excluded ==> you can slicing row and  col  both 

# print(df.loc[2:5,"year":"continent"])
# print(df.loc[1:6,["year","continent","gdp_cap"]])

# print(df.loc[-1])
# print(df.iloc[-1])   # u  y  p  pri   vi  my  nis  

# add new col in  data frame :  using loc 
"""df.loc[2]=["india",2015,15000000,"asia",36,24.789]
print(df)
"""
# using  iloc : 
"""df.iloc[1705]=["india",2015,15000000,"asia",36,24.789]
print(df)
"""
#==========

