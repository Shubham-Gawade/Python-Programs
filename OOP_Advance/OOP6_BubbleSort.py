#Bubble Sort

list=[3,2,6,4,8,1]
list1=[3,2,6,4,8,1]

for i in range(0,len(list)-1):
    for j in range(0,len(list)-1):
        if list[j] > list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
            # temp=list[j]
            # list[j]=list[j+1]
            # list[j+1]=temp

for i in range(len(list)):
    print(list[i],end=" ")
print()

print("---------------------------")

list1.sort()

for i in range(len(list)):
    print(list1[i],end=" ")