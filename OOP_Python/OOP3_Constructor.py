#Constructor in inheritance

class A:

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("feature1 working")

    def feature2(self):
        print("feature2 working")

class B:

    def __init__(self):
        super().__init__() #To call the init of super class
        print("In B init")

    def feature3(self):
        print("feature3 working")

    def feature4(self):
        print("feature4 working")

a1=B() # If you create object of Sub class it will first try to find init of sub class
       # if it is not found then it will call init of super class



