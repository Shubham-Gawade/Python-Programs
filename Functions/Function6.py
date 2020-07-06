#Filter Map Reduce
from functools import reduce

# 1)Filter

is_even = lambda n: n%2==0

num=[3,2,6,9,1,5,6,2,3]

evens = list(filter(is_even,num))
#evens = list(filter(lambda n: n%2==0,num))
print(evens)

print("-------------------------------------")
# 2)Map

doubles = list(map(lambda n: n*2,evens))
print(doubles)

print("-------------------------------------")
# 3)Reduce

sum=reduce(lambda a,b: a+b,doubles)
print(sum)