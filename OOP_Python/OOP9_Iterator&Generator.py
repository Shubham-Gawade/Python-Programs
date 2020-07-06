#Iterator and Generator

num=[1,2,3,4]

it=iter(num)

print(it.__next__())

print(next(it))  # whenever you call next it will preserve old value

for i in num:
    print(i,end=" ")
print()

print("----------------------------------")
#Create your own iterator

class TopTen:

    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
values=TopTen()

print(values.__next__())  # 1
print(next(values))   # 2

for i in values:  # 3 to 10
    print(i)

print("===================================================")
#Generators -> instead of loading 1000 records in memory we use generators and then we can fetch one by one value

def topten():
    yield 6     # this will make your function generator
    yield 3
    yield 5
    yield 7

values=topten()

print(values.__next__())
print(values.__next__())

for i in values:
    print(i)

print("-----------------------------")

def toptensqr():

    n=1
    while n <= 10:
        sq = n*n
        yield sq
        n+=1

values=toptensqr()

for i in values:
    print(i)