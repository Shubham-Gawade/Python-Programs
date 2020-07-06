#Python support ->functional programming , procedure programming and
# object oriented programming

#Class -> design or blueprint
#Object -> instance of class
#Object -> Atrribute -> variable  and Behaviour -> function

class Computer:

    def config(self):
        print("1tb , 8gb ram , HP")

comp1=Computer()
comp2=Computer()

print(comp1)

Computer.config(comp1) #we pass comp1 bcoz for which object we want to call congig
Computer.config(comp2)

comp1.config() #config will take comp1 as parameter
comp2.config()