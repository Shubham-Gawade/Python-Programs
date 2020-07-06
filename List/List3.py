a=[1,2,3]
b=[4,5,6]

c=a+b
print(c)

print(c[2:5]) #slicing

print(min(c))
print(max(c))
print(sum(c))
print(len(c))
print(sum(c)/len(c))

str="I am shubham"
list1=str.split()

print(list1)

list1.append("gawade")

print(list1)

print(len(list1))

print(list1[1])

for i in list1:
    print(i,end=" ")
print()

line="first;second;third"

print(line)

print(line.split(";"))