import numpy as np    
"""a=np.array([
    [1,2,3,4,5,34,55],
    [6,7,8,9,10,11,12],
    [13,14,15,16,17,18,19],
    [21,22,23,24,25,26,27]
    ])
"""
# print(a[1:3:2,1:7:3])

# lalit  :6 ,9 12  
# pragti : 6 ,8 10 
# jalay  : 6,8 10 

# d= np.full(a.shape,13)
# print(d)

"""f =np.full_like(a,100)
print(f)
"""
"""
f=f.reshape(7,4)  # 4,7
print(f)
"""

"""b= np.arange(1,29).reshape(7,4)
print(b)
"""

import random as r 

# print(r.random())  # 0-1 
# print(r.randrange(1,10,2))  # last value  excluded : 
# print(r.randint(1,10))  # both  point included 
# print(r.choice([1,2,3,4,5,"guru",100 ]))
# print(r.choices([1,2,3,4,5,"guru",100 ],k=2))

"""
d =np.random.random(12).reshape(3,4)
print(d)
"""
"""e=np.random.randint(low=1,high=10,size=9)
print(e)

g=np.random.randint(low=1,high=100,size=(3,4))
print(g)
"""

"""j=np.random.randint(low=1,high=100,size=9).reshape(3,3)
print(j)
"""

"""k=np.random.sample((5,5))
print(k)
"""

"""l=np.arange(0,10,0.5)
print(l)
"""

"""t=np.ones((3,4))
print(t)
"""
"""r= np.zeros((3,4))
print(r)
"""
q =np.linspace(0,9.5,20)
print(q)

# formula  : 
"""
each step size =stop -start / num-1

start = 0  stop =9.5  num =20
"""
"""
       [[1, 1, 1, 1, 1],
       [1, 0, 0, 0, 1],
       [1, 0, 9, 0, 1],
       [1, 0, 0, 0, 1],
       [1, 1, 1, 1, 1]]

"""

a =np.arange(1,31).reshape(6,5)
print(a)

# task :1print()  11,12 
        #          16,17

# task  2 :  2 8 14 20 

# task 3 : 
"""
[[4 5],
[24 25],
[29 ,30]]
"""

# task  :4 
#[1 ][7] [13][19] [25]
