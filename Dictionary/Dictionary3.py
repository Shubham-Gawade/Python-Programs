purse=dict()

purse["money"]=300
purse["candy"]=23
purse["tissues"]=5

print(purse)

print(purse["money"])

purse["candy"]=purse["candy"]+2

print(purse)

counts=dict()
counts1=dict()

names=["A","B","C","B","A","C","B","D"]

for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)

for name in names:
        counts1[name]=counts1.get(name,0)+1
print(counts1)

for key in counts:
    print(key," ",counts[key])

print("-------------------------------")

for key,value in counts.items():
    print(key," ",value)

print("--------------------------------")

lst=list()
tup=tuple()
dic=dict()

print(dir(lst))
print(dir(tup))
print(dir(dic))

print("---------------------------------")

str1="ABC"
lst1=["A","B","C"]
tup1=("A","B","C")

lst1[2]="D"  #mutable
#str1[2]="D"  immmutable
#tup1[2]="D"  immutable