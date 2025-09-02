class Person:
    def __init__(self, name , age , height , weight):
        self.name=name
        self.age=age
        self.height =height
        self.weight =weight

    def eat(self):
        print("vat kahy")

    def exercise(self):
        raise NotImplementedError # eta dile ai function sub class a implement kortei hobe

class Criketer(Person):
    def __init__(self, name, age, height, weight,team):
        self.team=team
        super().__init__(name, age, height, weight)

    def eat(self):
        print("valo khabar khay")#etai override , parent class ar eat function override korbe
    
    def exercise(self):
        print("valo kore exercise kor beta")

    def __add__(self,other):
        return self.age+other.age
    
    def __len__(self):
        return self.height
 
shamim=Criketer("shamim",13 ,56,98,"bd")
musi=Criketer("musi",36 ,86,88,"bd")
# shamim.eat()
# shamim.exercise()

# plus (+) sign overload 
print(5+9)
print("rasel "+"ahmed")
print([9,8,3,4]+[6,7,8])
print(shamim+musi)
print(len(shamim))