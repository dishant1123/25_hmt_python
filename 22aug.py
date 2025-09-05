"""
1. numpy  ==> array manupulation   
2. pandas ==> data analysis ==> sql 
3. matplotlib ==> plotting , graph ==> bar chart ,col , line chart 
4. seaborn ==> plotting , graph ==> regression  line  

"""
# list : mutable sequence  ==> changes in list . 

"""
l1 =[1,2,3,4,5,6,7,"harshit",90,12.67,7j,True]

print(l1)
print(type(l1))
"""
# list element access though index : 

# l1 =[10,20,30,40,50,60,70,"harshit",90,12.67,7j,True]

# index number  : 0 ,1,2,3 ...  ==>  l to  r 
# negative :-1 -2    ==> r to l 

"""
print(l1[4])
l1[5] ="tithi"
print(l1)
"""
# slicing  : 
"""print(l1[2:4])  # start index : 2  end index :4 
print(l1[4 :-4])
print(l1[-4 :4])
print(l1[-4 :-2])
"""

"""print(l1[2:5:2])  # 2 starting index 5 end index 2 step size
print(l1[0:8:3])  # 0 starting index 8 end index 3 step size

print(l1[ : : -2])
print(l1[ : : -1])
"""

# built  in function  : len  min max sorted sum  .. 
# l1 =[100,20,30,40,50,60,70,90,12.67]

"""print(len(l1))
print(sum(l1))
print(sorted(l1))

"""

"""l2= sorted(l1)
print(l2)
l3 =l2[ : :-1]
print(l3)
"""

"""l1.append(900)
print(l1)

l1[6]="harshit"
print(l1)

l1.insert(4,"lalit")
print(l1)
"""

l1=[[1,2,3,10] , 
    [4,5,6,11] , 
    [7,8,9,100]]
"""
(0,0) ==>1  (0,1)==>2 
(1,0) ==>3  (1,1) ==>4 
(2,0) ==>5  (2,1)==>6
[1,2,3]   ==> row  0 ==>  0 ==> index 1 0 index ==>2  1   3 index ==>2
"""
# print(l1,end="")
"""
for i in l1 :
    print(i)
"""
#        r  c
print(l1[0][0])
print(l1[2][1])
print(l1[0][0:2])
print(l1[1][1:2])
print(l1[2][:-1])
print(l1[2][0 :3 :2])
print(l1[1][0 :-1 :3])

