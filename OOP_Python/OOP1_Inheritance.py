#single and multi level Inheritance

class A:  #super class
    def feature1(self):
        print("feature1 working")

    def feature2(self):
        print("feature2 working")

class B(A):  #sub class of A and super class of C
    def feature3(self):
        print("feature3 working")

    def feature4(self):
        print("feature4 working")

class C(B):  #sub class of B
    def feature5(self):
        print("feature5 working")

a1=A()

b1=B()

c1=C()

a1.feature1()
a1.feature2()
print("------------------")
b1.feature3()
b1.feature1()
print("------------------")
c1.feature1()
