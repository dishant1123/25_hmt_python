import pandas as pd
# sort : 

data = {
    id :[101,102,103,104,105],
    "name":["lalit","het","amit","smit","jalay"],
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

print(df.query("marks>88"))