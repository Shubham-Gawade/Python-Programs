dict1={1:"abc","2":"def"}
print(dict1)

print(dict1.keys())

print(dict1.values())

def f(x):return x%2!=0 and x%3!=0
print(filter(f,range(2,25)))

def cube(x):return x*x*x
map(cube(3),range(2,10))

#strip function

#List comprehensions

vec=[2,4,6]
print([3*x for  x in vec])
print([3*x for x in vec if x>3])
print([3*x for x in vec if x<2])
print([[x,x**2] for x in vec])

del vec[0]
print(vec)
vec.clear()
print(vec)

#Set is set of maths
b=["a","b","c"]
f=set(b)
print(f)

a=set("abcjhdbkj")
b=set("sgjbddd")
print(a)
print(a-b)