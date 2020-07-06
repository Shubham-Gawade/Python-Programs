list1 = [10,20,30]
list2 = [10,20,30]

list3 = [list1,list2]

print(list1)
print(list2)
print(list3)
print()
for i in range (0,2):
    for j in range(0,len(list3[i])):
        print(list3[i][j],end=" ")
    print()
print()

matrix=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

for i in range (0,3):
    for j in range(0,3):
        print(matrix[i][j],end=" ")
    print()
print()

# matrix1=[[],[],[]]
# print("Enter elements : ")
# for i in range (0,len(matrix1)):
#     c1=int(input("Enter column for row "))
#     for j in range(0,c1):
#         matrix1[i].append(int(input("Enter value")))
#
# print("Matrix1 is : ")
# for i in range (0,len(matrix1)):
#     for j in range(0,len(matrix1[i])):
#         print(matrix1[i][j],end=" ")
#     print()

# r=int(input("How many rows you want add : "))
# matrix2=[]
# for i in range (0,r):
#     c1=int(input("Enter column for row "))
#     list = []
#     for j in range(0,c1):
#         list.append(int(input("Enter value ")))
#     matrix2.append(list)
#
# print("Matrix1 is : ")
# for i in range (0,len(matrix2)):
#     for j in range(0,len(matrix2[i])):
#         print(matrix2[i][j],end=" ")
#     print()

m1=[]
print("Enter the matrix element :")
c2=int(input("Enter the no of rows : "))
for i in range(0,c2):
    l33 = []
    m1.append(l33)

for i in  range(0,c2):
    c1=int(input("Enter the column number for row : "))
    for j in range(0,c1):
        m1[i].append(input())
print()
for i in range(0,c2):
    for j in range(0,len(m1[i])):
        print(m1[i][j],end=" ")
    print()