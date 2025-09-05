# shape ndim size  itemsize : 

import numpy as np  

x=np.random.randint(low =-30,high=50,size=12).reshape(3,4)
print(x)
# print(x.shape)
# print(x.ndim)
# print(x.size)
# print(x.itemsize)

# print(x.T)

"""
axis =0 do the  computation column wise 
axis =1 do the computation row wise
"""

# print(x.sum())
# print(x.sum(axis=0))
# print(x.sum(axis=1))

print(x+10)
# print(x*2)
# print(x/3)
# print(x%5)

