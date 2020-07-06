from numpy import *

arr1=array([1,2,3,4,5])

arr2=arr1 #only one array is created in memory

print("Array2: ",arr2)

print(id(arr1)) #id to show address
print(id(arr2))

arr3=arr1.view()

arr1[1]=7  #shallow copy -> change for one automatically change to other

print("Array3: ",arr3)

print(id(arr3))

arr4=arr1.copy()

arr1[1]=8

print("Array4: ",arr4)
print("Array1: ",arr1)