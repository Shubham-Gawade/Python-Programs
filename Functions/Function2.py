#Types of Argument

def add(a,b):  #formal argument
    c=a+b
    print("c : ",c)

add(5,6)  #actual argument

# actual argument
# 1)Position
def person(name,age):
    print(name)
    print(age)

person("shubham",20)

# 2)Keyword
def person(name, age):
    print(name)
    print(age)

person(age=20,name="shubham")

# 3)Default
def person(name, age=18):
    print(name)
    print(age)

person("shubham")

# 4)Variable length
def sum(a, *b):
    c=a
    for i in b:
        c=c+i
    print(c)

sum(3,4,5,6,7)

#Keyword variable length argument

def person1(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

person1("shubham",age=20,city="pune",mob=9876543)
