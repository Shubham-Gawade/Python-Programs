#Types of methods
# 1)Instance method
#    a)Accessor method -> To fetch the value -> getter
#    b)Mutator method -> To modify the value -> setter
# 2)Class method
# 3)Static method

class Student:

    school="mescoe"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):  # working with instance use self
        return self.m1

    def set_m1(self,value):
        self.m1=value

    @classmethod
    def getSchool(cls):   # working with a class variable
        return cls.school

    @staticmethod
    def info():
        print("This is student classs")

s1=Student(45,35,42)
s2=Student(36,41,43)

print("s1 avg: ",s1.avg())
print("s2 avg: ",s2.avg())

print(Student.getSchool())
Student.info()