#__init__ method -> Constructor
#self -> current objcet

class Computer:

    def __init__(self):
        self.name="shubham"
        self.age=20

    def update(self):
        self.age=25

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

comp1=Computer()
comp2=Computer()

print(id(comp1))
print(id(comp2))

comp2.name="pranav"
comp2.age=20

comp1.update() #comp1 will pass to update

print("Comp1: ",comp1.name,comp1.age)
print("Comp2: ",comp2.name,comp2.age)

if comp1.compare(comp2): #comp1 -> self and comp2 -> other
    print("Their age is same")
else:
    print("Their age is not same")

#Heap Memory -> All objects are created inside it. And it contais address of object
#Size of an object -> Depends on the no of variables and size of each variable
#Who allocates size to object -> costructor
