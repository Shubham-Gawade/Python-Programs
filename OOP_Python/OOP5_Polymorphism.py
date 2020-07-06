#Polymorphism -> one thing many forms
# 1)Duck typing
# 2)Operator Overloading
# 3)Method Overloading
# 4)Method Overriding

#----------------------------------------------------------------------------------------------
# x = 5 #In memory we create a space of type integer and x is just a name to that space
# x = "shubham"
# print(x)
#----------------------------------------------------------------------------------------------

#Duck Typing

class PyCharm:

    def  execute(self):
        print("Compiling...")
        print("Running...")

class MyEditor:

    def  execute(self):
        print("Spell check..")
        print("Convention check..")
        print("Compiling...")
        print("Running...")

class Laptop:

    def code(self,ide):
        ide.execute()

ide=MyEditor()
lap1=Laptop()
lap1.code(ide)