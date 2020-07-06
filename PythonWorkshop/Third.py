"""
    Types : mutanble and immutable
    list
    tuple
    dictionary
    sequnces
    sets
"""

a=["a",5,3.25,4+1j]
print(a)

tuple=(1,2,"b")
print(tuple)

list=[1,2,"b"]
print(list)

k=a[3]
print(k)

strlist=["abc","def","gif"]
for i in strlist:
    for j in i:
        print(j,end=" ")
print()

print(len(strlist))

print(len(strlist[2]))

a=["Mescoe"]
a.append("k")
print(a)

a,b=10,20
(a,b)=(b,a)
print(a)
print(b)

t=(1,2)
print(t)
t=(3,4) #reinitialze
print(t)

t[1]=5 #Error
print(t)