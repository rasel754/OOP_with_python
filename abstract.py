from abc import ABC,abstractmethod
# abstract base class 

class Animal(ABC):
    @abstractmethod #enforce all derived class to have a eat method
    def eat(self):
        print("i need food")

    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name):
        self.name=name
        super().__init__()

    def eat(self):
        print('hey nana i am eating banana')

layka=Monkey("lucky")
layka.eat()
