from array import *

arr=array("i",[]) #Empty array

#this array is one dimentional

n=int(input("Enter the length of array : "))

for i in range(n):
    x=int(input("Enter the value : "))
    arr.append(x)

print(arr)

ser=int(input("Enter the number to be searched : "))

k=0
for i in arr:
    if i==ser:
        print("Number found at position ",k)
        break
    k+=1

print(arr.index(ser))