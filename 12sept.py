import numpy as np 
# txt == > read   load.txt , genfrom .txt 

a = np.array([[10, 7, 4], [3, 2, 1]])
# sort : 1 2 3 4 7 10 11

"""c=np.mean(a)
d=np.median(a)
e=np.std(a)   # std dev 
t=np.var(a)   # var 
print(c)
print(d)
print(e)
print(t)
"""

"""a = np.array([[10, 7, 4], [3, 2, 1]])
print(a)
min_a=np.min(a)
print(min_a)

max_a =np.max(a)
print(max_a)

# max_a= np.max(a,axis=0)  #  axis  =0  ===>  row  max 
# max_a= np.max(a,axis=1)   # axis =1  ==> col  max 
# arg_max=np.argmax(a)  # it given index number  of max value 
# arg_max=np.argmax(a,axis=0)  #
# arg_max=np.argmax(a,axis=1)  #

print(arg_max)
"""

# load.txt , genfrom.txt  : 
"""
load.txt ==> clean , uniform 
genfrom.txt ==> clean , uniform ,missing value  ,header ,delimiter 
"""
"""a=np.loadtxt("1.txt",dtype=int,delimiter=" ")
print(a)
print(a.shape)
"""

# genfromtxt :

"""
a=np.genfromtxt("2.txt",dtype=None,delimiter=",",names=True)
print(a)
print("names : ",a.dtype.names)
"""

"""fit =np.genfromtxt("fitbit_user.txt",dtype="str",delimiter=",",skip_header=1)
print(fit)
"""
# len : 
"""len_of_fit =len(fit)
print(len_of_fit)
"""
# shape : 
"""print(fit.ndim)  # number of axis  =2 
print(fit.shape)  # array  (96,6)

print(fit[0])
print(fit[0 :5]) 
"""
"""
task  :1 

Print number of days user was sedantary (< 5000 steps), low active (5000 to 7499 steps), somewhat active (7500 to 9999 steps) and active (10k to 12499 steps).
"""

"""
steps =fit[ :,1]
steps =steps.astype(int)
print(steps)

sedantary =len(steps[steps<5000])
lowactive = len(steps[steps<7500]) -sedantary
somewhateactive = len(steps[steps<10000]) -lowactive -sedantary
active = len(steps[steps<12500]) -somewhateactive -lowactive -sedantary
print(sedantary)
print(lowactive)
print(somewhateactive)
print(active)
"""