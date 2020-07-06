#Types of variables -> instance variable and class(static) variable

#namespace ->it is an area where you create and store object/variable
#1) class namespace
#2) instance namespace

class Car:

    wheels=4  #class variable

    def __init__(self):
        self.mil=10    #instance variable ->As object changes instance variables also changes
        self.com="BMW"

c1=Car()
c2=Car()

c1.mil=8

Car.wheels=5

print("c1: ",c1.com," ",c1.mil," ",c1.wheels)
print("c2: ",c2.com," ",c2.mil," ",c2.wheels)