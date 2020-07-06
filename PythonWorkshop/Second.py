#control structure

a=["a","bee","cd"]  #list is a collection of different object

for i in a:
    print(i,int(len(i)))

b=["cd",2]
print(b)

for i in (range(10)):
    print(i,end=" ")
print()

for i in (range(5,10)):
    print(i,end=" ")
print()

for i in (range(0,10,3)):
    print(i,end=" ")
print()

for i in (range(0,10,-1)):
    print(i,end=" ")
print()

def fib(n):
    a,b=0,1
    print(a,end=" ")
    while b<n:
        print(b,end=" ")
        a,b=b,a+b

fib(10)