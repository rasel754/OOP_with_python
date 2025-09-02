class Animal:
    def __init__(self,name):
        self.name=name

    def make_sound(self):
       print("animal making sound")

class Cat(Animal):
    def __init__(self, name):
         super().__init__(name)

    def make_sound(self):
       print("meow meow")
   

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("ghew ghew ")

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        print("hambaa hambaa")

# Polymorphism in action
# animals = [Dog(), Cat(), Cow()]

# for animal in animals:
#     print(animal.make_sound())

don=Cat("real don")
don.make_sound()

shapred=Dog("milon")
shapred.make_sound()

shoan=Cow("shoan")
shoan.make_sound()

parnis=[don,shapred,shoan]

for animal in parnis:
    animal.make_sound()