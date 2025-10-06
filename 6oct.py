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
print(yr)