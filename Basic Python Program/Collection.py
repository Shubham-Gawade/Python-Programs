n=(int(input("Enter range : ")))
a = []
for i in range(n):
    a.append(i)

print("Print Elements :")
for i in range(n):
    print(a[i],end=" ")

print()
print(len(a))

b = []
print("Enter Elements :")
for i in range(n):
    b.append(input())

i = n
for i in range(n-1, -1, -1):
    print(b[i], end=" ")

print()
b.reverse()
for i in range(n):
    print(b[i],end=" ")

print()
print("Sorted Element : ")
b.sort()
print(b)

print()
print("Insert Element : ")
b.insert(n+1,10)
print(b)

print()
temp2=int(input("Enter number for count : "))
print(b.count(temp2))



