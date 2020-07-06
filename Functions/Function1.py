def greet():
    print("Hello")
    print("good morning")

greet()

print("--------------------------------------")

def add(x,y):
    c=x+y
    return c

ans=add(3,4)
print("Addition : ",ans)

print("----------------------------------------")

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

ans1,ans2=add_sub(4,3) #can return two values
print("Addition : ",ans1)
print("Substraction : ",ans2)

print("------------------------------------------")

#we don't have concept like both
# call by value -> passing value -> it will take different memory
# call by reference -> passing address -> change to one reflects to other

def modify(x):
    print(id(x))
    x = 8
    print(id(x))
    print("x : ", x)

a = 10
print(id(a))
modify(a)
print("a : ", a)
