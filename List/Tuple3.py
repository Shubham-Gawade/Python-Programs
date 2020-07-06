(x,y,z)=(2,3,"Hello")

print(x)
print(z)
print("-----------")

#Error
# (a,b)=(4)
# print(a)

d=dict()
d["A"]=2
d["B"]=3

for (x,y) in d.items():
    print(x, y)

print("-----------")

t=d.items()
print(t)

print("-----------")

#Comparison

print((6,2,3)>(4,5,6))

print((4,6,2)>(3,5,1))

print(("aec","def")<("adf","feg"))

print("--------------")

d={'a':10,'c':20,'b':15,'d':5}

print(d.items())
print(sorted(d.items()))

print("--------------")

for (x,y) in sorted(d.items()):  # sort by key order
    print(x," ",y)

print("---------------")

l=list()

for (x,y) in sorted(d.items()):
    l.append((y,x))

print(l)

print(sorted(l))

print(sorted(l,reverse=True))

print("---------------")

#Assign values
x,y=1,2

print(y)

print("---------------")

x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()

print(y)

print("---------------")

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

print(days[2])