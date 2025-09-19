# deep copy vs shallow copy : 

# shallow copy : 
"""l1 = [1,2,3,4]

l2=l1 
l1[3]="pragati"

print(l2)
print(l1)
"""

# deep copy : 
"""l1=[1,2,3,4]
l2 =l1.copy() 

l1[2]="unnati"

print("l2 : ",l2)
print("l1 :",l1)
# u ==> 1 unnati 3 4  p ==>1 2 3 4 l2= 1 u 3 4    
#   l ==> l1 = 1 2 u 4  l2 = 1 2 3 4
# y  ==> 1 2  u 4  l2 = 1 2 3 4 
"""

import numpy as np 

# shallow copy :
"""
arr =np.array([1,2,3,4,5])

shallow =arr 
shallow[2]=99

print(shallow)
print(arr)
"""

# deep  copy  : 

"""
arr =np.array([1,2,3,4,5])
l2 =arr.copy()

arr[2]=990
print("l2 = ",l2)   
print("arr = ",arr)
"""

"""import matplotlib.pyplot as plt

virat= plt.imread("virat_rohit_picture.jpg") 
print(virat)

b = plt.imsave("virat_rohit_picture.jpg",virat)
print(b)

# a =plt.imshow(virat)
# print(a)

virat_inverted = virat[::-1, :, :]
print(virat_inverted)

plt.imshow(virat_inverted)

"""
