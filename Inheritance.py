class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
     def bark(self):# "Pass" means that python will just skip this line when running
         print("arf arf Nigga! ")


class Cat(Mammal):
    pass

dog1 = Dog()
dog1.bark()
dog1.walk()  # Walk has now been inherited from the mammal class

