import pandas as pd 
# join  : 
"""
sql  : 

1. inner join  ==> 2 table 1 col  common 
2. left join   ==> left side 
3. right join  ==> right side  join 
4. cross join  ==> all  row  
"""

"""users = pd.DataFrame({"userid":[1,2,3],"name":["yash","unnati","ram"]})
print(users)

msgs =pd.DataFrame({"userid":[1,2,3],"msg":["hi","hello","jay shree ram"],"age":[20,38,55]})
print(msgs)
"""
# a =pd.concat([users,msgs])
# a =pd.concat([users,msgs],axis=1)

"""
a= users.merge(msgs)  # inner  join  
print(a)
"""

"""
emp =pd.DataFrame({"empid":[1,2,3,4,5],"name":["ram","yash","unnati","jay","shree"],"dept_id":[10,10,20,40,50]})
# print(emp)

dept =pd.DataFrame({"dept_id":[10,20,50],"dept_name":["IT","HR","Finance"]})
# print(dept)

result_join = emp.merge(dept,how="left",on="dept_id")
print(result_join)

"""

emp =pd.DataFrame({"empid":[1,2,3,4,5],
                   "name":["ram","yash","unnati","jay","shree"],
                   "dept_id":[10,10,20,40,50],
                   "salary":[1000,2000,3000,4000,5000]})

dept =pd.DataFrame({"dept_id":[10,20,50],
                    "dept_name":["IT","HR","Finance"]})


combine =pd.merge(emp,dept,how="left",on="dept_id")
# print(combine)

# avg salary by dept : 

avg_salary =combine.groupby("dept_name")['salary'].mean()
# print(avg_salary)

# total  salary +emp count per dept  : 

salary_count =combine.groupby("dept_name").agg(total_salary=("salary","sum"),count_emp=("empid","count"),avg_salary=("salary","mean"))

print(salary_count)