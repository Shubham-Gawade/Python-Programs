#Global Keyword
#Scope

a=10  #Global variable -> It can accesible anywhere

def something():
    global a
    a=20   #Local variable
    print("In fun:",a)

something()
print("Outside:",a)

print("------------------------------")

b=10
print(id(b))

def something():
    b=20
    x=globals()["b"]
    print(id(x))
    print("In fun:",b)

    globals()["b"]=15

something()
print("Outside:",b)