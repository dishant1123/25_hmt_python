# list  :  mutable  sequence 
"""l1= [1,2,3,4,5,6,7,"harshit",90,12.67,7j,True]
print(l1)
print(type(l1))
"""

# l1=[10,20,30,40,50,60]
# index start : 0    ==> l  to r 
# negative index : -1 -2 -3  ==> r to  l 

"""l1.append("patel")
print(l1)

l1.insert(2,"harshit")
print(l1)
"""

# slicing  : 

"""print(l1[4])
l1[2] ="tithi"
print(l1)
"""

# adv list  : 
"""
l1=[[1,2,3],    
    [4,5,6],
    [7,8,9]]
"""
"""
matrix components : 

(0,0) ==>1  (0,1) ==>2 (0,2)==>3 
(1,0) ==>4  (1,1) ==>5 (1,2)==>6
(2,0) ==>7  (2,1) ==>8 (2,2)==>9
"""
"""print(l1)
for i in l1 : 
    print(i)
"""

"""print(l1[0])
#        r  c
print(l1[0][2])
print(l1[1][-1])
print(l1[2][1:3])
print(l1[2][0:3 :2])  # start stop  step  
print(l1[1] [ : : -2])
"""
# print(l1[ : : -1])

"""
l1=[[1,2,3],    
    [4,5,6],
    [7,8,9]]

"""
# import  numpy as np 

import numpy as np 

"""a=np.array([1,2,3,4,5,6,7,8,90])
print(a)

b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(b)

c=np.array([[[1,2,3]],
            [[4,5,6]],
            [[7,8,9]]])
print(c)

"""

"""a =np.array([1,2,3,4,5,6,7,8,90],dtype="int16") # ==> 2 bytes store 
print(a)

b =np.array([1,2,3,4,5,6,7,8,90],dtype="float") # ==> 8 bytes store 
print(b)
"""

# array  : 
# 4 *7 : 
a=np.array([
    [1,2,3,4,5,34,55],
    [6,7,8,9,10,11,12],
    [13,14,15,16,17,18,19],
    [21,22,23,24,25,26,27]
    ])

print(a)
print(a[0,4])
print(a[1,2:6])
print(a[2,: : 2])
print(a[0,: : -1])

print(a[1:3,2:6])
print(a[2:3,1:-5])
print(a[1:3:2,0:6 :2])




