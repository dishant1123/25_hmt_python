import numpy as np

"""a=np.random.randint(low=1,high=10,size=9).reshape(3,3)
b=np.random.randint(low=1,high=10,size=9).reshape(3,3)

print("a=",a)
print("b=",b)
"""
"""
c=np.matmul(a,b)
print(c)
"""
"""
a= 
[[4 7 3]     4 7 3     9  2 1  = 36 +14 + 3  = 53  
 [9 7 2]       
 [2 2 5]]
b= 
[[9 3 8]
 [2 4 3]
 [1 1 2]]   4 7 3 3 4 1 = 12 + 28 + 3 =43  
"""  
"""
a=np.random.randint(low=1,high=10,size=9).reshape(3,3)
print(a)
c =np.sqrt(a)
print(c)
"""

"""a=np.random.randint(low=1,high=10,size=9).reshape(3,3)

print(a)
c =np.where(a>5)
print(c)
"""

"""
a=np.arange(1,10).reshape(3,3)
b= np.arange(11,20).reshape(3,3)
"""
# print(a)
# print(b)

"""c =np.vstack((a,b))
print(c)
"""
"""c =np.hstack((a,b))
print(c)
"""

# statistical function  : 

# a=np.arange(1,10).reshape(3,3)
a = np.array([[10, 7, 4], [3, 2, 1]])
# sort : 1 2 3 4 7 10 11
c=np.mean(a)
d=np.median(a)
print(c)
print(d)