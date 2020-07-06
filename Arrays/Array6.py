from numpy import *

arr1=array([
    [1,2,3,6,7,3],
    [4,5,6,9,4,2]
])

print(arr1)

print(arr1.dtype) #data type

print(arr1.ndim) # dimension

print(arr1.shape) #(row,column)

arr2=arr1.flatten() #convert to one Dimension

print(arr2)

arr3=arr2.reshape(2,2,3) #two dimentional array, two single dimentional array,three  values

print(arr3)

print("----------------------------------------------------------")

mat=matrix(arr1)

print(mat)

mat1=matrix('1,2,3 ; 4,5,6 ; 7,8,9')
mat2=matrix('7,8,9 ; 1,2,3 ; 4,5,6')

print(mat1)

print(mat1.diagonal())

print(mat1.min())

mat3=mat1+mat2

print(mat3)

mat4=mat1*mat2

print(mat4)

