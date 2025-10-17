import pandas as pd 
# join  : 
"""
sql  : 

1. inner join  ==> 2 table 1 col  common 
2. left join   ==> left side 
3. right join  ==> right side  join 
4. cross join  ==> all  row  
"""

users = pd.DataFrame({"userid":[1,2,3],"name":["yash","unnati","ram"]})
# print(users)

msgs =pd.DataFrame({"userid":[1,2,3],"msg":["hi","hello","jay shree ram"],"age":[20,38,55]})
# print(msgs)

# a =pd.concat([users,msgs])
# a =pd.concat([users,msgs],axis=1)

a= users.merge(msgs)  # inner  join  
print(a)