#Selection Sort

list=[3,2,6,4,8,1]

for i in range(0,len(list)-1):
    min_pos=i
    for j in range(i,len(list)):
        if list[j] < list[min_pos]:
            min_pos=j

    temp = list[i]
    list[i]=list[min_pos]
    list[min_pos]=temp

for i in range(len(list)):
    print(list[i],end=" ")
print()