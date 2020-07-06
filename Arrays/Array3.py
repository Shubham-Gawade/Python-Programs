# Types to create array
# 1)array()
# 2)linspace()
# 3)logspace()
# 4)arange()
# 5)zeros()
# 6)ones()

from numpy import *

arr = array([1,2,3,4,5,6],int)
arr1 = array([1,2,3,4,5,6],float)

print(arr)
print(arr1)
print("-------------------------------------------------------------")

arr2=linspace(0,15,15)
#(start,end,divide into how many parts)
print(arr2)

print("-------------------------------------------------------------")

arr3=logspace(1,40,5)

print(arr3)

print("-------------------------------------------------------------")

arr4=arange(1,15,2)
#skip by how many number
print(arr4)

print("-------------------------------------------------------------")

arr5=ones(5,int)

print(arr5)

print("-------------------------------------------------------------")

arr6=zeros(5)

print(arr6)