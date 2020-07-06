#Method Resolution Order(MRO)
#class C(A,B) -> it will prefer to go from left to right to call init method
#Same for functions

class A:  # super class

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("feature1 - A working")

class B:  # super class

    def __init__(self):
        print("In B init")

    def feature1(self):
        print("feature1 - B working")

class C(A,B):  # sub class of A and B

    def __init__(self):
        super().__init__()
        print("In C init")

    def feature5(self):
        print("feature5 working")

a1=C()

a1.feature1()