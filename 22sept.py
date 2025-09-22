import pandas as pd 

"""
df1=pd.DataFrame([
    ["guru",20,900000],
    ["yash",19,800000],
    ["het",18,800000],
    ["ved",17,1000000],
    ["mayuri",19,300000]],columns=["name","age","salary"])"""
# print(df1) 

"""df2=df1.rename(columns={
    "name":"first_name",
    "salary":"stipend"
},axis=1,inplace=True)
print(df2)
"""
"""t2=pd.DataFrame({
    "name" :["mayuri","yash","het","ved","guru"],
    "age":[19,19,18,17,20],
    "salary":[300000,800000,800000,1000000,900000]
})
print(t2)
"""
# print(t2)
# print(t2.columns)
# print(t2.keys())

"""t2=t2.rename(columns={
    "name":"first_name",
    "salary":"stipend"
})
print(t2)
"""
# drop  : 

"""
x =t2.drop("age",axis=1)
x = t2.drop(["age","salary"],axis=1)
x=t2.drop(columns=["name","salary"],axis=1)
print(x)
"""
#add new col in   data frame :

"""t2["gender"]=["Female","Male","Male","Male","Male"]
print(t2)
"""
# mckinsey .csv : 

df = pd.read_csv("mckinsey.csv")
print(df)