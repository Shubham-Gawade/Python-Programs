#Inner class

class Student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()  #You can create object of inner class inside the outer class

    def show(self):
        print(self.name," ",self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=8

        def show(self):
            print(self.brand," ",self.cpu," ",self.ram)

s1=Student("shubham",42)
s2=Student("Dhanshree",43)

s1.show()

lap1=s1.lap
lap2=s2.lap

lap3=Student.Laptop()  # You can create object of inner class outside the outer class proivided you use
                       # outer class name to call it

print(id(lap1))
print(id(lap2))