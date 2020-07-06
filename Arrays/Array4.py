from numpy import *

arr1=array([1,2,3,4,5])
arr2=array([6,7,8,9,10])

arr1=arr1+5  # Adding 5 to each element

print(arr1)

print("-----------------------------------")

arr3=arr1+arr2 # vectorized opertion

print(arr3)
print("-----------------------------------")

print("Sine values : ",sin(arr1))

print("Cos values : ",cos(arr1))

print("Sine values : ",sqrt(arr1))

print("Sum values : ",sum(arr1))

print("Min values : ",min(arr1))

print("Max values : ",max(arr1))

print("Sorted values : ",sort(arr1))

print("Concatenated values : ",concatenate([arr1,arr2]))