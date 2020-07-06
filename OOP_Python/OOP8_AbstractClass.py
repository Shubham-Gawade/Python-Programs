#Abstract class and method -> pythod not support abstract class and method directly but we can implement by
# ABC module -> Abstract Base Class -> we can create our own abstract class

from abc import ABC,abstractmethod

class Computer(ABC):  #Abstract class

    @abstractmethod
    def process(self): #Abstract method
        pass

class Laptop(Computer):
    def process(self):  #we must override all abstract method of super class in sub class
        print("Running..")

class Programmer:
    def work(self,com):
        print("Solving bugs")
        com.process()

com1=Laptop()
prog1=Programmer()
prog1.work(com1)

