#All Values of same type
#Arrays don't have specific type

import array as arr  #Alias

vals=arr.array("i",[1,-2,3])  # i -> typecode -> any number

# b, B, u, h, H, i, I, l, L, q, Q, f or d
# small case -> signed data type
# upper case -> unsigned data type -> 0 to infinity

print(vals)

print(vals.buffer_info())
# (Address , size)

vals.append(4)
print(vals)

print("--------------")

print(vals[0])

print("-------------")

for i in range(len(vals)):
    print(vals[i],end=" ")

print()
print("-------------")

for j in vals:
    print(j,end=" ")
print()
print("-------------")

newArr=arr.array(vals.typecode,(a*a for a in  vals))

print(newArr)

i =0
while i<len(newArr):
    print(newArr[i],end=" ")
    i+=1
print()