#Method Overloading -> same name but different parameter list

class Student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b

        return s

s1=Student(45,47)

print(s1.sum(5,9,10))

print("---------------------------------------------------------")

#Method Overriding -> same name and same parameter list

class A:
    def show(self):
        print("In A show")

class B(A):
    def show(self):
        print("In B show")

a1=B()
a1.show()