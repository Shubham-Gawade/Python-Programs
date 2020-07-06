"""
print("Enter the no of elements in the List:")
n=int(input())
listofNumber=[]
#To accept elements of List
print('Enter the elements of List:')
for i in range (n):
    listofNumber.append(input())

#To display elements of list
print('Entered List Element Are:')
for i in range(n):
    print(listofNumber[i])

min=listofNumber[0]
max=listofNumber[0]
sum =0
for i in range(n):
    if(listofNumber[i]<min):
        min=listofNumber[i]
    elif (listofNumber[i]>max):
        max = listofNumber[i]
    sum = sum + int(listofNumber[i])
print('Minimum Element is:'+min)
print('Maximum Element is:'+max)
print('Average of List Elements Are:'+str(sum/n))"""

list=[]
ch=0
while True:
    print("1)Append")
    print("2)Display")
    print("3)Delete")
    print("4)Insert at position")
    print("5)Sort")
    print("6)Search")
    print("7)Exit")
    ch = int(input("Enter your choice :"))

    if(ch==1):
        print("Enter the no of elements in the List:")
        n = int(input())
        print('Enter the elements of List:')
        for i in range(n):
            list.append(int(input()))

    elif (ch == 2):
        print('Entered elements of List:')
        for i in range(n):
            print(list[i],end=" ")
        print()

    elif (ch == 3):
        print(list)
        rem=int(input('Enter element to remove:'))
        list.remove(rem)
        print(list)

    elif (ch == 4):
        num1=int(input('Enter element to insert:'))
        pos=int(input('Enter position to insert:'))
        if num1 in list:
            print("Dublicate element")
        else:
            list.insert(pos,num1)
        print(list)

    elif (ch == 5):
        list.sort()
        print(list)

    elif (ch == 6):
        num2 = int(input('Enter element for search:'))
        print("Position : ",list.index(num2))

    elif (ch == 7):
        break
