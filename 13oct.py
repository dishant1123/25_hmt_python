import pandas as pd
# sort : 

data = {
    "id" :[101,102,103,104,105],
    "name":["aryaman","het","amit","smit","jalay"],
    "age":[20,21,23,24,19],
    "marks":[90,91,88,86,99],
    "city":["chennai","delhi","mumbai","bangalore","kolkata"]
}

df = pd.DataFrame(data)
# print(df)
# sort marks  ==> desc to asc 
# print(df.sort_values(["marks"],ascending=False))


# 2 col  sort : 
"""
print(df.sort_values(["marks","age"],ascending=[True,True]))
"""
# using filter  : 
# print(df[df["marks"]>88])

# print(df.query("marks>88"))

# print(df.sample(3))  # random 3 row print  

# sql  :  top  3 by  marks 
"""a= df.nlargest(3,"marks")
print(a)
"""
# bottom  3 : 
"""b =df.nsmallest(3,"marks")
print(b)
"""

# give me  row  like name  start  with "a"  : 


# a=df[df["name"].str.startswith("a")]
# print(a)

b =df.query("marks > 88 and age >15" )
print(b)